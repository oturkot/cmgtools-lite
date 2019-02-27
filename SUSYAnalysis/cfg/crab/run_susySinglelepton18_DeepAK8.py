##########################################################
##       CONFIGURATION FOR TTH MULTILEPTON TREES       ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
import re


#-------- LOAD ALL ANALYZERS -----------

from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

#-------- SET OPTIONS AND REDEFINE CONFIGURATIONS -----------

run80X = getHeppyOption("run80X",False)

runData = getHeppyOption("runData",True)
runMC = getHeppyOption("runMC",False)
runSig = getHeppyOption("runSig",False)



removeJetReCalibration = getHeppyOption("removeJetReCalibration",False)
removeJecUncertainty = getHeppyOption("removeJecUncertainty",False)
doMETpreprocessor = getHeppyOption("doMETpreprocessor",False)
skipT1METCorr = getHeppyOption("skipT1METCorr",False)
forcedSplitFactor = getHeppyOption("splitFactor",-1)
forcedFineSplitFactor = getHeppyOption("fineSplitFactor",-1)
#isTest = getHeppyOption("test",None) != None and not re.match("^\d+$",getHeppyOption("test"))
selectedEvents=getHeppyOption("selectEvents","")
keepGenPart=getHeppyOption("keepGenPart",False)
#test = getHeppyOption("test")
sample = "main"
test = 0
multib = True
zerob = False

# Lepton Skimming
ttHLepSkim.minLeptons = 0
#ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999
#ttHLepSkim.idCut  = ""
#ttHLepSkim.ptCuts = []
if not ttHLepSkim.allowLepTauComb:
    susyCoreSequence.remove(tauAna)
    susyCoreSequence.insert(susyCoreSequence.index(ttHLepSkim)+1, tauAna)

# Run miniIso
lepAna.doMiniIsolation = True
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.miniIsolationPUCorr = 'rhoArea'
lepAna.miniIsolationVetoLeptons = None # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones
lepAna.doIsolationScan = False
lepAna.doMiniIsolation = True if run80X else "precomputed"
lepAna.mu_isoCorr = "deltaBeta"

## MUONS
lepAna.loose_muon_pt  = 10
lepAna.inclusive_muon_pt  = 10
lepAna.loose_muon_id     = "POG_ID_Loose" #same as in core
lepAna.inclusive_muon_id     = "POG_ID_Loose" #same as in core

lepAna.loose_electron_eta = 2.4
lepAna.loose_electron_pt  = 10
lepAna.inclusive_electron_pt  = 10

# Lepton Preselection
### Fall17 V2 is valid for all 2016/17/18 
'''if run80X:
      lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto"
      lepAna.loose_electron_lostHits = 999. # no cut since embedded in ID
      lepAna.loose_electron_dxy    = 999. # no cut since embedded in ID
      lepAna.loose_electron_dz     = 999. # no cut since embedded in ID
      #lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'
      lepAna.inclusive_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_Veto"
      lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
      lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
      lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID
      lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'
'''
lepAna.loose_electron_id = "POG_Cuts_ID_FALL17_94X_v2_ConvVetoDxyDz_Veto"
lepAna.loose_electron_lostHits = 999. # no cut since embedded in ID
lepAna.loose_electron_dxy    = 999. # no cut since embedded in ID
lepAna.loose_electron_dz     = 999. # no cut since embedded in ID

lepAna.inclusive_electron_id  = "POG_Cuts_ID_FALL17_94X_v2_Veto"
lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in I
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID


isolation = "miniIso"


if run80X : 
	jetAna.mcGT     = "Summer16_07Aug2017_V11_MC"
	jetAna.dataGT   = [(1,"Summer16_07Aug2017BCD_V11_DATA"),(276831,"Summer16_07Aug2017EF_V11_DATA"),(278802,"Summer16_07Aug2017GH_V11_DATA")]
	
else : 
	jetAna.mcGT     = "Fall17_17Nov2017_V32_MC"
	jetAna.dataGT   = [(1,"Fall17_17Nov2017B_V32_DATA"),(299337,"Fall17_17Nov2017C_V32_DATA"),(302030,"Fall17_17Nov2017DE_V32_DATA"),(304911,"Fall17_17Nov2017F_V32_DATA")]
	# to activate the EE noise mitigation
	metAna.metCollection     = "slimmedMETsModifiedMET"
	metAna.noPUMetCollection = "slimmedMETsModifiedMET"
	
jetAna.lepSelCut = lambda lep : False # no cleaning of jets with leptons
jetAnaScaleDown.lepSelCut = lambda lep : False # no cleaning of jets with leptons
jetAnaScaleUp.lepSelCut = lambda lep : False # no cleaning of jets with leptons
jetAna.copyJetsByValue = True # do not remove this
metAna.copyMETsByValue = True # do not remove this
jetAna.doQG = True
jetAna.jetPt = 20
jetAna.jetEta = 2.4
jetAna.minLepPt = 10
jetAna.doQG = True
isoTrackAna.setOff = False
isoTrackAna.doRelIsolation = True
genAna.allGenTaus = True
jetAna.applyL2L3Residual = "Data"
if not removeJecUncertainty:
    jetAna.addJECShifts = True
    jetAna.jetPtOrUpOrDnSelection = True
    jetAnaScaleDown.copyJetsByValue = True # do not remove this
    jetAnaScaleDown.doQG = False
    metAnaScaleDown.copyMETsByValue = True # do not remove this
    jetAnaScaleUp.copyJetsByValue = True # do not remove this
    jetAnaScaleUp.doQG = False
    metAnaScaleUp.copyMETsByValue = True # do not remove this
    susyCoreSequence.insert(susyCoreSequence.index(jetAna)+1, jetAnaScaleDown)
    susyCoreSequence.insert(susyCoreSequence.index(jetAna)+1, jetAnaScaleUp)
    susyCoreSequence.insert(susyCoreSequence.index(metAna)+1, metAnaScaleDown)
    susyCoreSequence.insert(susyCoreSequence.index(metAna)+1, metAnaScaleUp)


if isolation == "miniIso": 
    if run80X:
         lepAna.doMiniIsolation = True
         lepAna.miniIsolationPUCorr = 'rhoArea'
         lepAna.miniIsolationVetoLeptons = None
         lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
         lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
    else:
         lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4 and muon.sip3D() < 8
         lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4 and elec.sip3D() < 8
elif isolation == None:
    lepAna.loose_muon_isoCut     = lambda muon : True
    lepAna.loose_electron_isoCut = lambda elec : True
elif isolation == "absIso04":
    lepAna.loose_muon_isoCut     = lambda muon : muon.relIso04*muon.pt() < 10 and muon.sip3D() < 8
    lepAna.loose_electron_isoCut = lambda elec : elec.relIso04*elec.pt() < 10 and elec.sip3D() < 8
else:
    # nothing to do, will use normal relIso03
    pass

# Switch off slow photon MC matching
photonAna.do_mc_match = False

# Loose Tau configuration
tauAna.loose_ptMin = 20
tauAna.loose_etaMax = 2.3
tauAna.loose_decayModeID = "decayModeFindingNewDMs"
tauAna.loose_tauID = "decayModeFindingNewDMs"
tauAna.loose_vetoLeptons = False # no cleaning with leptons in production
#    jetAna.cleanJetsFromTaus = True
#    jetAnaScaleUp.cleanJetsFromTaus = True
#    jetAnaScaleDown.cleanJetsFromTaus = True


#-------- ADDITIONAL ANALYZERS -----------

## Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## JetTau analyzer, to be called (for the moment) once bjetsMedium are produced
from CMGTools.TTHAnalysis.analyzers.ttHJetTauAnalyzer import ttHJetTauAnalyzer
ttHJetTauAna = cfg.Analyzer(
    ttHJetTauAnalyzer, name="ttHJetTauAnalyzer",
    )

## Insert the SV analyzer in the sequence
#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna), ttHSVAna)
#ttHSVAna.preselection = lambda ivf : abs(ivf.dxy.value())<2 and ivf.cosTheta>0.98
for M in badMuonAna, badMuonAnaMoriond2017, badCloneMuonAnaMoriond2017, badChargedHadronAna:#isoTrackAna,
    susyCoreSequence.remove(M)

from CMGTools.TTHAnalysis.analyzers.treeProducerTTH import * 

#add LHE ana for HT info
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig
## Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
      ttHFatJetAna)

# Add anyLepSkimmer
from CMGTools.TTHAnalysis.analyzers.anyLepSkimmer import anyLepSkimmer
anyLepSkim = cfg.Analyzer(
    anyLepSkimmer, name='anyLepSkimmer',
    minLeptons = 0,
    maxLeptons = 999,
)

## Single lepton + ST skim
from CMGTools.TTHAnalysis.analyzers.ttHSTSkimmer import ttHSTSkimmer
ttHSTSkimmer = cfg.Analyzer(
  ttHSTSkimmer, name='ttHSTSkimmer',
  minST = 0,
  )

from CMGTools.TTHAnalysis.analyzers.nIsrAnalyzer import NIsrAnalyzer
NIsrAnalyzer = cfg.Analyzer(
  NIsrAnalyzer, name='NIsrAnalyzer')
  
## HT skim
from CMGTools.TTHAnalysis.analyzers.ttHHTSkimmer import ttHHTSkimmer
ttHHTSkimmer = cfg.Analyzer(
  ttHHTSkimmer, name='ttHHTSkimmer',
  minHT = 0,
  )


if not removeJecUncertainty:
    ttH_globalObjects.update({
            "met_jecUp" : NTupleObject("met_jecUp", metType, help="PF E_{T}^{miss}, after type 1 corrections (JEC plus 1sigma)"),
            "met_jecDown" : NTupleObject("met_jecDown", metType, help="PF E_{T}^{miss}, after type 1 corrections (JEC minus 1sigma)"),
            })

## Tree Producer
from CMGTools.TTHAnalysis.analyzers.treeProducerSusySingleLepton import *
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusySingleLepton',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects =susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)
if getHeppyOption("reduceMantissa",False) in (True,"True","true","yes","1"):
    print 'Activating reduceMantissa!'
    setLossyFloatCompression(10,16)

## histo counter
susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer), susyCounter)


if not skipT1METCorr:
    if doMETpreprocessor: 
        print "WARNING: you're running the MET preprocessor and also Type1 MET corrections. This is probably not intended."
    jetAna.calculateType1METCorrection = True
    metAna.recalibrate = "type1"
    jetAnaScaleUp.calculateType1METCorrection = True
    metAnaScaleUp.recalibrate = "type1"
    jetAnaScaleDown.calculateType1METCorrection = True
    metAnaScaleDown.recalibrate = "type1"


#-------- SAMPLES AND TRIGGERS -----------

if run80X : 
	from CMGTools.RootTools.samples.triggers_13TeV_Spring15_1l import *
#-------- TRIGGERS -----------
	triggerFlagsAna.triggerBits = {
		## hadronic
		'HT350' : triggers_HT350,
		'HT600' : triggers_HT600,
		'HT800' : triggers_HT800,
		'HT900' : triggers_HT900,
		'MET170' : triggers_MET170,
		'HT350MET120' : triggers_HT350MET120,
		'HT350MET100' : triggers_HT350MET100,
		'HTMET' : triggers_HT350MET100 + triggers_HT350MET120,
		'PFJet450' : triggers_pfjet450,
		'AK4PFJet450' : triggers_ak4pfjet450,
		'AK8PFJet450' : triggers_ak8pfjet450,
		'CaloJet500' : triggers_calojet500,
		
		##MET test
		'MET170_HBHE' : triggers_MET170_HBHECleaned,
		'MET170_BH' : triggers_MET170_BeamHaloCleaned,
		'MET170_HBHE_BH' : triggers_MET170_HBHE_BeamHaloCleaned,
		'MET190_TypeOne_HBHE_BH' : triggers_METTypeOne190_HBHE_BeamHaloCleaned,
		
		'MET100MHT100' : triggers_MET100MHT100,
		'MET110MHT110' : triggers_MET110MHT110,
		'MET120MHT120' : triggers_MET120MHT120,
		
		'highMHTMET' : triggers_highMHTMET,
		## muon
		'SingleMu' : triggers_1mu,
		'IsoMu27' : triggers_1mu,
		'IsoMu20' : triggers_1mu20,
		'IsoMu24' : triggers_1mu24,
		'Mu45eta2p1' : trigger_1mu_noiso_r,
		'Mu50' : trigger_1mu_noiso_w,
		'MuHT600' : triggers_mu_ht600,
		'MuHT400MET70' : triggers_mu_ht400_met70,
		'MuHT350MET70' : triggers_mu_ht350_met70,
		'MuHT350MET50' : triggers_mu_ht350_met50,
		'MuHT350' : triggers_mu_ht350,
		'MuHT400' : triggers_mu_ht400,
		'Mu50HT400' : triggers_mu50_ht400,
		'MuHTMET' : triggers_mu_ht350_met70 + triggers_mu_ht400_met70,
		'MuMET120' : triggers_mu_met120,
		'MuHT400B': triggers_mu_ht400_btag,
		## electrons
		'IsoEle32' : triggers_1el,
		'IsoEle23' : triggers_1el23,
		'IsoEle22' : triggers_1el22,
		'IsoEle27T' : triggers_1el27WPTight,
		'Ele105' : trigger_1el_noiso,
		'Ele115' : trigger_1el_noiso_115,
		'Ele50PFJet165' :   trigger_1el_noiso_jet165,
		'EleHT600' : triggers_el_ht600,
		'EleHT400MET70' : triggers_el_ht400_met70,
		'EleHT350MET70' : triggers_el_ht350_met70,
		'EleHT350MET50' : triggers_el_ht350_met50,
		'EleHT350' : triggers_el_ht350,
		'EleHT400' : triggers_el_ht400,
		'Ele50HT400' : triggers_el50_ht400,
		'EleHTMET' : triggers_el_ht350_met70 + triggers_el_ht400_met70,
		'EleHT200' :triggers_el_ht200,
		'EleHT400B': triggers_el_ht400_btag
	}
	
else : 
	from CMGTools.RootTools.samples.triggers_13TeV_2017_1l import *
	triggerFlagsAna.triggerBits = {
		'HT350' : triggers_HT350,
		'HT590' : triggers_HT590,
		'HT780' : triggers_HT780,
		'HT890' : triggers_HT890,
		'PFJet450' : triggers_pfjet450,
		'AK4PFJet450' : triggers_ak4pfjet450,
		'AK8PFJet450' : triggers_ak8pfjet450,
		'CaloJet500' : triggers_calojet500,
		##MET test
		'MET100MHT100' : triggers_MET100MHT100,
		'MET110MHT110' : triggers_MET110MHT110,
		'MET120MHT120' : triggers_MET120MHT120,
		'highMHTMET' : triggers_highMHTMET,
		## muon
		'SingleMu' : triggers_1mu,
		'IsoMu27' : triggers_1mu,
		'IsoMu20' : triggers_1mu20,
		'IsoMu24' : triggers_1mu24,
		'Mu45eta2p1' : trigger_1mu_noiso_r,
		'Mu50' : trigger_1mu_noiso_w,
		'MuHT600' : triggers_mu_ht600,
		'MuHT450MET50' : triggers_mu_ht450_met50,
		'MuHT450' : triggers_mu_ht450,
		'Mu50HT450' : triggers_mu50_ht450,
		'MuHTMET' : triggers_mu_ht450_met50,
		'MuHT450B': triggers_mu_ht450_btag,
		## electrons
		'IsoEle32' : triggers_1el,
		'IsoEle35' : triggers_1el35,
		'IsoEle27T' : triggers_1el27WPTight,
		'Ele115' : trigger_1el_noiso_115,
		'Ele50PFJet165' :   trigger_1el_noiso_jet165,
		'EleHT600' : triggers_el_ht600,
		'EleHT450MET50' : triggers_el_ht450_met50,
		'EleHT450' : triggers_el_ht450,
		'Ele50HT450' : triggers_el50_ht450,
		'EleHTMET' : triggers_el_ht450_met50,
		'EleHT450B': triggers_el_ht450_btag
	}
triggerFlagsAna.unrollbits = False
triggerFlagsAna.saveIsUnprescaled = False
triggerFlagsAna.checkL1Prescale = False

from CMGTools.RootTools.samples.configTools import printSummary, configureSplittingFromTime, cropToLumi, prescaleComponents, insertEventSelector, mergeExtensions
from CMGTools.RootTools.samples.autoAAAconfig import *

#-------- SEQUENCE -----------
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1, anyLepSkim)
sequence = cfg.Sequence(susyCoreSequence+[
    LHEAna,
    NIsrAnalyzer,
    ttHEventAna,
    ttHHTSkimmer,
    ttHSTSkimmer,
    treeProducer,
    ])

if runMC:

  print 'Going to process MC'
  print 'If It fails due to susy masses please comment out necessary lines in TTHAnalysis/python/analyzers/treeProducerSusyCore.py for now'

  # apply a loose lepton skim to MC
  anyLepSkim.minLeptons = 1

  if run80X:
         from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv3_1l import *
  else: 
         from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD_1l import *

  #pick the file you want to run on
  selectedComponents = mcSamples
#  [TTJets_SingleLeptonFromTbar,TTJets_SingleLeptonFromTbar_ext,TTJets_SingleLeptonFromT,TTJets_DiLepton,TTJets_DiLepton_ext,
  if test==1:
    # test a single component, using a single thread.
    comp = WJetsToLNuHT[5]
    comp.files = comp.files[:1]
    selectedComponents = [comp]
    comp.splitFactor = 1
  elif test==2:
    # test all components (1 thread per component).
    for comp in selectedComponents:
      comp.splitFactor = 1
      comp.fineSplitFactor = 1
      comp.files = comp.files[:1]
  elif test==3:
    # run all components (1 thread per component).
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  elif test==0:
    selectedComponents = mcSamples
    #selectedComponents = [WJetsToLNuHT[1]]
    #selectedComponents = mcSamples
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  susyCoreSequence.remove(susyScanAna)
  treeProducer.globalVariables+=[
       NTupleVariable("lheHT", lambda ev : ev.lheHT, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer"),
       NTupleVariable("lheHTIncoming", lambda ev : ev.lheHTIncoming, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)"),
       NTupleVariable("nIsr", lambda ev : ev.nIsr, mcOnly=True, help="Number of ISR jets not matched to gen particles"),
    ]


elif runSig:

  print 'Going to process Signal, assuming it is FastSim'
  
  # Set FastSim JEC
  jetAna.mcGT = "Spring16_FastSimV1_MC"
  # No MET correcton 
  metAna.metCollection     = "slimmedMETs"
  metAna.noPUMetCollection = "slimmedMETs"
  #jetAna.mcGT = "Spring16_25nsFastSimV1_MC"
  #### REMOVE JET ID FOR FASTSIM
  jetAna.relaxJetId = True

  # modify skim (noe leptons skim)
  anyLepSkim.minLeptons = 0

  from CMGTools.RootTools.samples.samples_94X_signal import *
  if multib: 
      if run80X : 
          selectedComponents = [SMS_T1tttt_TuneCUETP8M1]
      else : 
          selectedComponents = [SMS_T1tttt_TuneCP2]
  
  if zerob: selectedComponents = [SMS_T5qqqqVV_TuneCUETP8M1]
  if multib and zerob : print "Warning ! Both zero b and multi b is set to  True, you will be running Zero b signals ;) Cheers from Ece"
  if not (multib or zerob) : print 8*"*", "Error ! Choose a signal to process", 8*"*"

  if test==1:
    # test a single component, using a single thread.
    if multib: comp  = SMS_T1tttt_TuneCP2
    if zerob: comp  = SMS_T5qqqqVV_TuneCUETP8M1
    comp.files = comp.files[:2]
    selectedComponents = [comp]
    comp.splitFactor = 1
  elif test==2:
    # test all components (1 thread per component).
    for comp in selectedComponents:
      comp.splitFactor = 1
      comp.fineSplitFactor = 1
      comp.files = comp.files[:1]
  elif test==3:
    # run all components (1 thread per component).
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  elif test==0:
    # PRODUCTION
    # run on everything
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)

  susyCoreSequence.insert(susyCoreSequence.index(susyScanAna)+1,
        susyCounter)
  # change scan mass parameters
  if multib:
    susyCounter.SUSYmodel = 'T1tttt'
  if zerob:
    susyCounter.SUSYmodel = 'T5qqqq'
  susyCounter.SMS_mass_1 = "genSusyMGluino"
  susyCounter.SMS_mass_2 = "genSusyMNeutralino"
  susyCounter.SMS_varying_masses = ['genSusyMGluino','genSusyMNeutralino']
  sequence.remove(anyLepSkim)
  sequence.remove(ttHHTSkimmer)
  sequence.remove(ttHSTSkimmer)
  sequence.remove(eventFlagsAna)
  sequence.remove(triggerFlagsAna)
  treeProducer.globalVariables+=[
       NTupleVariable("GenSusyMGluino", lambda ev : ev.genSusyMGluino, int, mcOnly=True, help="Susy Gluino mass"),
       NTupleVariable("GenSusyMNeutralino", lambda ev : ev.genSusyMNeutralino, int, mcOnly=True, help="Susy Neutralino mass"),
       NTupleVariable("nIsr", lambda ev : ev.nIsr, mcOnly=True, help="Number of ISR jets not matched to gen particles"),
    ]
  


if runData : # For running on data

  print 'Going to process DATA'

  # modify skim
  anyLepSkim.minLeptons = 1

  # central samples
  if run80X:
      from CMGTools.RootTools.samples.samples_13TeV_DATA2016_17Jul2018_1l import *
      selectedComponents = dataSamples_17Jul2018_1l
  else : 
      from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import *
      selectedComponents = dataSamples_31Mar2018_1l
  
  if test!=0 and jsonAna in susyCoreSequence: susyCoreSequence.remove(jsonAna)
  if test==1:
    # test one component (2 thread)
    comp = selectedComponents[3]
#    comp.files = comp.files[:1]
    comp.files = comp.files[10:11]
    selectedComponents = [comp]
    comp.splitFactor = len(comp.files)
  elif test==2:
    # test all components (1 thread per component).
    for comp in selectedComponents:
      comp.splitFactor = 1
      comp.fineSplitFactor = 1
      comp.files = comp.files[10:11]
  elif test==3:
    # run all components (10 files per component).
    for comp in selectedComponents:
      comp.files = comp.files[20:30]
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  elif test==0:
    # PRODUCTION
    # run on everything
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  sequence.remove(anyLepSkim)
  sequence.remove(NIsrAnalyzer)
  sequence.remove(ttHSTSkimmer)
  susyCoreSequence.remove(susyScanAna)

if removeJetReCalibration:
    jetAna.recalibrateJets = False
    jetAnaScaleUp.recalibrateJets = False
    jetAnaScaleDown.recalibrateJets = False

if forcedSplitFactor>0 or forcedFineSplitFactor>0:
    if forcedFineSplitFactor>0 and forcedSplitFactor!=1: raise RuntimeError, 'splitFactor must be 1 if setting fineSplitFactor'
    for c in selectedComponents:
        if forcedSplitFactor>0: c.splitFactor = forcedSplitFactor
        if forcedFineSplitFactor>0: c.fineSplitFactor = forcedFineSplitFactor

if selectedEvents!="":
    events=[ int(evt) for evt in selectedEvents.split(",") ]
    print "selecting only the following events : ", events
    eventSelector= cfg.Analyzer(
        EventSelector,'EventSelector',
        toSelect = events
        )
    susyCoreSequence.insert(0, eventSelector)

#preprocessor = None

#-------- HOW TO RUN -----------

if test == '80X-Data':
    json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
    DoubleMuon = kreator.makeDataComponent("DoubleMuon_Run2016H_run283885", "/DoubleMuon/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", run_range = (283885,283885), triggers = triggers_mumu)
    DoubleEG = kreator.makeDataComponent("DoubleEG_Run2016H_run283885", "/DoubleEG/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", run_range = (283885,283885), triggers = triggers_ee)
    DoubleMuon.files = [ 'root://eoscms//eos/cms/store/data/Run2016H/DoubleMuon/MINIAOD/PromptReco-v2/000/283/885/00000/5A21CC75-D09D-E611-BFDC-FA163E163D77.root' ]
    DoubleEG.files = [ 'root://eoscms//eos/cms/store/data/Run2016H/DoubleEG/MINIAOD/PromptReco-v2/000/283/885/00000/743981FC-949D-E611-836E-FA163EC09DF2.root' ]
    selectedComponents = [ DoubleMuon, DoubleEG ]
    for comp in selectedComponents:
        comp.json = json
        tmpfil = os.path.expandvars("/tmp/$USER/%s" % os.path.basename(comp.files[0]))
        if not os.path.exists(tmpfil): os.system("xrdcp %s %s" % (comp.files[0],tmpfil)) 
        comp.files = [tmpfil]
        comp.splitFactor = 1
        comp.fineSplitFactor = 4

if not getHeppyOption("keepLHEweights",False):
    if "LHE_weights" in treeProducer.collections: treeProducer.collections.pop("LHE_weights")
    if lheWeightAna in sequence: sequence.remove(lheWeightAna)
    susyCounter.doLHE = False


## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='treeProducerSusySingleLepton/tree.root',
    option='recreate'
    )    
outputService.append(output_service)

################### Preprocessing (DeepAK8) ##########################################
from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
#if run80X:
#     fname1="$CMSSW_BASE/src/NNKit/FatJetNN/test/FatJetNN_80X.py"
if runMC and not run80X: 
    fname1="./FatJetNN_94X_MC.py"
elif runData and not run80X : 
    fname1="./FatJetNN_94X_data.py"
else : 
    fname1="./FatJetNN_94X.py"
    
preprocessor = CmsswPreprocessor(fname1)

ttHFatJetAna.jetCol="deepntuplizer"
#jetAna.jetCol = 'selectedUpdatedPatJets'
##################################################################################################

selectComponents = getHeppyOption('selectComponents',None)
if selectComponents:
    for comp in selectedComponents[:]:
        if not any(re.search(p.strip(),comp.name) for p in selectComponents.split(",")):
            selectedComponents.remove(comp)

# print summary of components to process
printSummary(selectedComponents)

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
#event_class = EOSEventsWithDownload if not preprocessor else Events
event_class = Events
EOSEventsWithDownload.aggressive = 2 # always fetch if running on Wigner
EOSEventsWithDownload.long_cache = getHeppyOption("long_cache",False)
if getHeppyOption("nofetch") or getHeppyOption("isCrab"):
    event_class = Events
    if preprocessor: preprocessor.prefetch = False
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = outputService, 
                     preprocessor = preprocessor, 
                     events_class = event_class)
