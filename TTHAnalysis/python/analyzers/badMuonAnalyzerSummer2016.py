import operator 
import itertools
import copy

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg

class badMuonAnalyzerSummer2016( Analyzer ):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(badMuonAnalyzerSummer2016,self).__init__(cfg_ana,cfg_comp,looperName)
        self.minMuPt = cfg_ana.minMuPt
        self.flagName = 'badMuonSummer2016_'+cfg_ana.postFix if cfg_ana.postFix!='' else 'badMuonSummer2016'

    def declareHandles(self):
        super(badMuonAnalyzerSummer2016, self).declareHandles()
        self.handles['muons'] = AutoHandle(self.cfg_ana.muons,"std::vector<pat::Muon>")
        self.handles['packedCandidates'] = AutoHandle( self.cfg_ana.packedCandidates, 'std::vector<pat::PackedCandidate>')

    def beginLoop(self, setup):
        super(badMuonAnalyzerSummer2016,self).beginLoop( setup )

    def process(self, event):
        self.readCollections( event.input )
        
        maxDR = 0.001
        suspiciousAlgo=14
        minDZ = 0.1
        minPtErr = 2.0
        innerTrackRelErr = 1.0
        maxSegmentCompatibility = 0.3
        flagged = False
        event.crazyMuon = []

        for muon in self.handles['muons'].product():
            ##### check the muon inner and globaTrack
            if muon.innerTrack().isNonnull():
                it = muon.innerTrack()
                muonBestTrack = muon.muonBestTrack()
                if muon.pt()<self.minMuPt and it.pt()<self.minMuPt : continue
                if not (it.originalAlgo()==suspiciousAlgo and it.algo()==suspiciousAlgo ): continue
                if not muon.isGlobalMuon(): continue
                if muon.segmentCompatibility() > maxSegmentCompatibility and \
                    muonBestTrack.ptError()/muonBestTrack.pt() < minPtErr and \
                    it.ptError()/it.pt() < minPtErr: continue

                for c in self.handles['packedCandidates'].product():
                    if abs(c.pdgId()) == 13:
                        if c.pt()<self.minMuPt : continue
                        if deltaR( muon.eta(), muon.phi(), c.eta(), c.phi() ) < maxDR:
                            flagged = True
                            event.crazyMuon.append(muon)
                            break
            if flagged: break

                
        setattr( event, self.flagName,  (not flagged) )
        return True

    def printInfo(self, event):
 
        if len(event.crazyMuon)>0:
#            print 'found muon: run=', event.run,' lumi=', event.lumi,' event',event.eventId
            print 'met=',event.met.pt(),' metphi=',event.met.phi()
            print 'number of muons: ',len(event.crazyMuon)
            print ' muon candidate pt: ',event.crazyMuon[0].pt(),' phi=',event.crazyMuon[0].phi()
            print ' muon candidate eta: ',event.crazyMuon[0].eta()
            print ' pdgId candidate : ',event.crazyMuon[0].pdgId()
            print ' trackHighPurity: ',event.crazyMuon[0].trackHighPurity()
            print ' dz: ',event.crazyMuon[0].dz()
            print ' fromPV: ',event.crazyMuon[0].fromPV()
            print ' ptError: ',event.crazyMuon[0].pseudoTrack().ptError(),';relativeError',event.crazyMuon[0].pseudoTrack().ptError()/event.crazyMuon[0].pseudoTrack().pt()
            print ' chi2: ',event.crazyMuon[0].pseudoTrack().normalizedChi2()
            print ' algo: ',event.crazyMuon[0].algo(),' originalAlgo',event.crazyMuon[0].originalAlgo()
            print '----------------'
            print '----------------'

setattr(badMuonAnalyzerSummer2016,"defaultConfig", cfg.Analyzer(
        class_object = badMuonAnalyzerSummer2016,
        packedCandidates = 'packedPFCandidates',
        minMuPt = 100,
        postFix = '',
        )
)

