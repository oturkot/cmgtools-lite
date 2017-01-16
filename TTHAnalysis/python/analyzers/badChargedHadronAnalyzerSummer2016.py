import operator 
import itertools
import copy

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg

class badChargedHadronAnalyzerSummer2016( Analyzer ):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(badChargedHadronAnalyzerSummer2016,self).__init__(cfg_ana,cfg_comp,looperName)

    def declareHandles(self):
        super(badChargedHadronAnalyzerSummer2016, self).declareHandles()
        self.handles['muons'] = AutoHandle(self.cfg_ana.muons,"std::vector<pat::Muon>")
        self.handles['packedCandidates'] = AutoHandle( self.cfg_ana.packedCandidates, 'std::vector<pat::PackedCandidate>')

    def beginLoop(self, setup):
        super(badChargedHadronAnalyzerSummer2016,self).beginLoop( setup )

    def process(self, event):
        self.readCollections( event.input )
        
        maxDR = 0.0001
        minPtDiffRel = 0.0001
        minMuonTrackRelErr = 2.0
        innerTrackRelErr = 1.0
        minMuPt = 100
        maxSegmentCompatibility = 0.3
        flagged = False

        for muon in self.handles['muons'].product():
            if muon.innerTrack().isNonnull():
                it = muon.innerTrack()
                muonBestTrack = muon.muonBestTrack()
                if muon.pt()<minMuPt and it.pt()<minMuPt: continue
                if not muon.isGlobalMuon(): continue

                if  muon.segmentCompatibility() > maxSegmentCompatibility and \
                    muonBestTrack.ptError()/muonBestTrack.pt() < minMuonTrackRelErr and \
                    it.ptError()/it.pt() < innerTrackRelErr: continue
 
                for c in self.handles['packedCandidates'].product():
                    if abs(c.pdgId()) == 211:
                        # Require very loose similarity in pt (one-sided). 
                        dPtRel =  ( c.pt() - it.pt() )/(0.5*(c.pt() + it.pt()))
                        # Flag the event bad if dR is tiny
                        if deltaR( it.eta(), it.phi(), c.eta(), c.phi() ) < maxDR and abs(dPtRel) < minPtDiffRel:
                            flagged = True
                            break
                if flagged: break
        event.badChargedHadronSummer2016=(not flagged) 
        return True

setattr(badChargedHadronAnalyzerSummer2016,"defaultConfig", cfg.Analyzer(
        class_object = badChargedHadronAnalyzerSummer2016,
        muons='slimmedMuons',
        packedCandidates = 'packedPFCandidates',
        )
)

