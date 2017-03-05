from CMGTools.TTHAnalysis.treeReAnalyzer import *
import ROOT

ROOT.gROOT.ProcessLine(".L ../python/tools/WPolarizationVariation.C+")
ROOT.gROOT.ProcessLine(".L ../python/tools/TTbarPolarization.C+")
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.AutoLibraryLoader.enable()


def getLV(p4):
    if p4 != None: return ROOT.LorentzVector(p4.Px(),p4.Py(),p4.Pz(),p4.E())
    else: return p4

def getGenWandLepton(event):

    wP4 = None
    lepP4 = None

    genParts = [p for p in Collection(event,"GenPart","nGenPart")]
    genLeps = filter(lambda l:abs(l.pdgId) in [11,13,15], genParts)

    if len(genLeps) == 0:
        print "no gen lepton found!"
        return wP4, lepP4

    lFromW = filter(lambda w:abs(w.motherId)==24, genLeps)

    if len(lFromW) == 0:
        print "no gen W found!", genLeps
        return wP4, lepP4

    elif len(lFromW)>1:
        print 'this should not have happened'
        return wP4, lepP4

    elif len(lFromW) == 1:

        genLep = lFromW[0]
        genW = genParts[genLep.motherIndex]

        wP4 = getLV(genW.p4())
        lepP4 = getLV(genLep.p4())

        #print genW.p4().M(),genLep.p4().M()
        #print wP4.M(),lepP4.M()

    return wP4, lepP4

def getGenTopWLepton(event):

    topP4 = None
    wP4 = None
    lepP4 = None

    genParts = [p for p in Collection(event,"GenPart","nGenPart")]
    genLeps = filter(lambda l:abs(l.pdgId) in [11,13,15], genParts)

    if len(genLeps) == 0:
        #print "no gen lepton found!" # happens in TTJets ;)
        return topP4, wP4, lepP4

    lFromW = filter(lambda w:abs(w.motherId)==24, genLeps)

    if len(lFromW) == 0:
        print "no gen W found!", genLeps
        return topP4, wP4, lepP4

    elif len(lFromW) > 2:
        print "More than 2 W's found!"
        return topP4, wP4, lepP4

    elif len(lFromW) == 1:

        genLep = lFromW[0]
        genW = genParts[genLep.motherIndex]
        genTop = genParts[genW.motherIndex]

        topP4 = getLV(genTop.p4())
        wP4 = getLV(genW.p4())
        lepP4 = getLV(genLep.p4())

        return topP4, wP4, lepP4

    elif len(lFromW) == 2:
        match = False

        if event.nLepGood > 0:
            leadLep = Collection(event,"LepGood","nLepGood")[0]

            for genLep in lFromW:
                if leadLep.charge == genLep.charge:
                    match == True

                    genW = genParts[genLep.motherIndex]
                    genTop = genParts[genW.motherIndex]

                    topP4 = getLV(genTop.p4())
                    wP4 = getLV(genW.p4())
                    lepP4 = getLV(genLep.p4())

                    return topP4, wP4, lepP4

        if not match:
            print 'No match at all!'
            return topP4, wP4, lepP4

    return topP4, wP4, lepP4

def getWPolWeights(event, sample):

    wUp = 1
    wDown = 1

    if "TTJets" in sample: #W polarization in TTbar
        topP4, wP4, lepP4 = getGenTopWLepton(event)

        if topP4 != None:
            #print topP4.M(), wP4.M(), lepP4.M()
            cosTheta = ROOT.ttbarPolarizationAngle(topP4, wP4, lepP4)
            #print cosTheta
            wUp = (1. + 0.05*(1.-cosTheta)**2) * 1./(1.+0.05*2./3.) * (1./1.0323239521945559)
            wDown = (1. - 0.05*(1.-cosTheta)**2) * 1./(1.-0.05*2./3.) * (1.034553190276963956)

    elif "WJets" in sample: #W polarization in WJets
        wP4, lepP4 = getGenWandLepton(event)

        if wP4 != None:
            #print wP4.M(), lepP4.M()
            cosTheta = ROOT.WjetPolarizationAngle(wP4, lepP4)
            #print cosTheta
            wUp = (1. + 0.1*(1.-cosTheta)**2) * 1./(1.+0.1*2./3.) * (1./1.04923678332724659)
            wDown = (1. - 0.1*(1.-cosTheta)**2) * 1./(1.-0.1*2./3.) * (1.05627060952003952)

    #print wUp, wDown

    return wUp, wDown

class EventVars1LWeightsForSystematics:
    def __init__(self):
        self.branches = [
            # Top related
            "GenTopPt", "GenAntiTopPt", "TopPtWeight","TopPtWeightII", "GenTTBarPt", "GenTTBarWeight",
            # ISR
            "ISRTTBarWeight", "GenGGPt", "ISRSigUp", "ISRSigDown",
            # DiLepton
            "DilepNJetCorr", #to shift central value 
            "DilepNJetWeightConstUp", "DilepNJetWeightSlopeUp", "DilepNJetWeightConstDn", "DilepNJetWeightSlopeDn",
            # W polarisation
            "WpolWup","WpolWdown",
            'nISRtt','nISRttweight','nISRttweightsyst_up', 'nISRttweightsyst_down',
            # PDF related -- Work In Progress
            #"pdfW","pdfW_Up","pdfW_Down",
            # Scale uncertainty
            #"scaleW","scaleW_up","scaleW_down"
            ]

    def listBranches(self):
        return self.branches[:]

    def __call__(self,event,base={}):
        if event.isData: return {}

        # prepare output
        ret = {}
        for name in self.branches:
            #print name
            if type(name) is tuple:
                ret[name] = []
            elif type(name) is str:
                ret[name] = -999.0
            else:
                print "could not identify"
        #print ret

        #### W polarisation
        wPolWup, wPolWdown = getWPolWeights(event, self.sample)
        ret['WpolWup'] = wPolWup
        ret['WpolWdown'] = wPolWdown

        ### PDF VARS
        #"Pdfw","Pdfw_Up","Pdfw_Down"

        pdfWup= 1
        pdfWdown = 1
        pdfWcentr = 1

        '''
        if hasattr(event,"LHEweight_wgt"):
        pdfWmin = 99
        pdfWmax = 0
        #lheWgts = [w for w in Collection(event,"LHEweight_wgt","nLHEweight")]

        ret['pdfW'] = pdfWcentr
        ret['pdfW_Up'] = pdfWup
        ret['pdfW_Down'] = pdfWup
        '''

        ### TOP RELATED VARS
        genParts = [l for l in Collection(event,"GenPart","nGenPart")]

        GenTopPt = -999
        GenTopIdx = -999
        GenAntiTopPt = -999
        GenAntiTopIdx = -999
        TopPtWeight = 1.
        TopPtWeightII = 1.
        GenTTBarPt = -999
        GenTTBarWeight = 1.
        ISRTTBarWeight = 1.
        GenGGPt = -999
        ISRSigUp = 1.
        ISRSigDown = 1.

        nGenTops = 0
        GluinoIdx = []
        for i_part, genPart in enumerate(genParts):
            if genPart.pdgId ==  6:
                GenTopPt = genPart.pt
                GenTopIdx = i_part
            if genPart.pdgId == -6:
                GenAntiTopPt = genPart.pt
                GenAntiTopIdx = i_part
            if abs(genPart.pdgId) ==  6: nGenTops+=1

            if genPart.pdgId == 1000021:
                GluinoIdx.append(i_part)

        if len(GluinoIdx)==2:
            GenGluinoGluinop4 = genParts[GluinoIdx[0]].p4()+ genParts[GluinoIdx[1]].p4()
            GenGluinoGluinoPt = GenGluinoGluinop4.Pt()
            GenGGPt = GenGluinoGluinoPt
            if GenGluinoGluinoPt > 400: ISRSigUp = 1.15; ISRSigDown = 0.85
            if GenGluinoGluinoPt > 600: ISRSigUp = 1.30; ISRSigDown = 0.70


        if GenTopPt!=-999 and GenAntiTopPt!=-999 and nGenTops==2:
            SFTop     = exp(0.156    -0.00137*GenTopPt    )
            SFAntiTop = exp(0.156    -0.00137*GenAntiTopPt)

            SFTopII     = exp(0.0615    -0.0005*GenTopPt    )
            SFAntiTopII = exp(0.0615    -0.0005*GenAntiTopPt)

            TopPtWeight = sqrt(SFTop*SFAntiTop)
            TopPtWeightII = sqrt(SFTopII*SFAntiTopII)
            if TopPtWeight<0.5: TopPtWeight=0.5
            if TopPtWeightII<0.5: TopPtWeightII=0.5

            if GenAntiTopIdx!=-999 and GenTopIdx!=-999:
                GenTTBarp4 = genParts[GenTopIdx].p4()+ genParts[GenAntiTopIdx].p4()
                GenTTBarPt = GenTTBarp4.Pt()
                if GenTTBarPt>120: GenTTBarWeight= 0.95
                if GenTTBarPt>150: GenTTBarWeight= 0.90
                if GenTTBarPt>250: GenTTBarWeight= 0.80
                if GenTTBarPt>400: GenTTBarWeight= 0.70
                if GenTTBarPt>400: ISRTTBarWeight = 0.85
                if GenTTBarPt>600: ISRTTBarWeight = 0.7

        ####################################
        ### For DiLepton systematics
        # values in sync with AN2015_207_v3
        #        Const weight
        # const: 0.85 +-0.06
        #        16%

        '''
        constVariation=0.16
        wmean = 5.82 - 0.5
        # slope: 0.03 +/-0.05
        slopevariation = sqrt(0.03*0.03 +0.05*0.05)

        #2016 update
        constVariation=0.16
        slopevariation = sqrt(0.05*0.05 +0.04*0.04)
        wmean = 5.54 - 0.5

        #2016 update with 4/fb
        constVariation= sqrt(0.06*0.06 +0.03*0.03)
        slopevariation = sqrt(0.06*0.06 +0.02*0.02)
        wmean = 5.62 - 0.5

        #2016 update with 7.7/fb
        constVariation= sqrt(0.04*0.04 +0.02*0.02)
        slopevariation = sqrt(0.07*0.07 +0.02*0.02)
        wmean = 5.67 - 0.5
        '''

        #2016 update with 35.9/fb
        #https://indico.cern.ch/event/611061/contributions/2464202/attachments/1406419/2149049/diLepStudy.pdf
        constVariation= sqrt(0.030*0.030 +0.023*0.023)
        slopevariation = sqrt(0.017*0.017 +0.014*0.014)
        wmean = 6.93 - 0.5

        if "nJets30Clean" in base: nJets30Clean = base["nJets30Clean"]
        else: nJets30Clean = event.nJet

        sumnGenLepTau=0
        for i in range(0,event.ngenTau):
            if abs(event.genTau_grandmotherId[i])==6 and abs(event.genTau_motherId[i])==24: sumnGenLepTau+=1
        for i in range(0,event.ngenLep):
            if abs(event.genLep_grandmotherId[i])==6 and abs(event.genLep_motherId[i])==24: sumnGenLepTau+=1
#        if (event.ngenLep+event.ngenTau)==2: #would like to restore this behavior...
        if sumnGenLepTau==2:
            ret['DilepNJetCorr']          = 1.030-0.017*(nJets30Clean-wmean)
            ret['DilepNJetWeightConstUp'] = 1-constVariation
            ret['DilepNJetWeightSlopeUp'] = 1+ (nJets30Clean-wmean)*slopevariation
            ret['DilepNJetWeightConstDn'] = 1+constVariation
            ret['DilepNJetWeightSlopeDn'] = 1- (nJets30Clean-wmean)*slopevariation
        else:
            ret['DilepNJetCorr']          = 1.
            ret['DilepNJetWeightConstUp'] = 1.
            ret['DilepNJetWeightSlopeUp'] = 1.
            ret['DilepNJetWeightConstDn'] = 1.
            ret['DilepNJetWeightSlopeDn'] = 1.


        ret['GenTopPt'] = GenTopPt
        ret['GenAntiTopPt'] = GenAntiTopPt
        ret['TopPtWeight']  = TopPtWeight
        ret['TopPtWeightII']  = TopPtWeightII
        ret['GenTTBarPt']  = GenTTBarPt
        ret['GenTTBarWeight'] = GenTTBarWeight
        ret['ISRTTBarWeight' ]  = ISRTTBarWeight
        ret['GenGGPt'] = GenGGPt
        ret['ISRSigUp' ]  = ISRSigUp
        ret['ISRSigDown'] = ISRSigDown


        #implement Moriond17 version
        # of Ana and Manuels nISR jet reweighting, very similar to eventVars_1l_signal.py
        # print self.sample
        nISRweight = 1
        nISRweightsyst_up =  1
        nISRweightsyst_down = 1
        if 'TTJets' in self.sample:
            nISR = 0
            if hasattr(event,'nIsr'): nISR = event.nIsr
            nISRforWeights = int(nISR)
            if nISR > 6:
                nISRforWeights = 6

            ret['nISR'] = int(nISR)
            ISRweights = { 0: 1, 1 : 0.920, 2 : 0.821, 3 : 0.715, 4 : 0.662, 5 : 0.561, 6 : 0.511}
            ISRweightssyst = { 0: 0.0, 1 : 0.040, 2 : 0.090, 3 : 0.143, 4 : 0.169, 5 : 0.219, 6 : 0.244}


            # ------ Forwarded Message --------
            # Subject: Re: question for ttbar ISR reweighting
            # Date: Sat, 14 Jan 2017 20:24:14 +0100
            # From: Manuel Franco Sevilla <manuel.franco.sevilla@cern.ch>
            #The [Nom, Up, Down] values we find for the events with Nisr = 0 are:
            #[1.090, 1.043, 1.141]: TTJets_Tune
            #[1.096, 1.046, 1.151]: TTJets_SingleLeptFromT
            #[1.116, 1.055, 1.185]: TTJets_DiLept
            C_ISR = 1.090
            C_ISR_up   = 1.043
            C_ISR_down = 1.141
            nISRweight = C_ISR * ISRweights[nISRforWeights]
            nISRweightsyst_up   =  C_ISR_up   * (ISRweights[nISRforWeights] + ISRweightssyst[nISRforWeights])
            nISRweightsyst_down =  C_ISR_down * (ISRweights[nISRforWeights] - ISRweightssyst[nISRforWeights])

        ret['nISRttweight'] = nISRweight
        ret['nISRttweightsyst_up'] = nISRweightsyst_up
        ret['nISRttweightsyst_down'] = nISRweightsyst_down

        return ret

if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = EventVars1LWeightsForSystematics()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
#            tree.Show(0)
            print self.sf(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)
