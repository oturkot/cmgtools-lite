##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
## In general all modules that are in CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff
## are loaded and executed by default. Settings not overwritten here, will be taken from there.
##########################################################


import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

#JSON
jsonAna.useLumiBlocks = True

#####Move all the definitions used through the config up here, and don't overwrite them later##########
######################################################################################################
#eleID type (cut based  = CBID)
eleID = "CBID"

# Isolation
isolation = "miniIso"
#JEC
jetAna.mcGT = "Summer16_23Sep2016V3_MC"
#jetAna.dataGT = "Summer16_23Sep2016AllV3_DATA"
jetAna.dataGT   = [(1,"Summer16_23Sep2016BCDV3_DATA"),(276831,"Summer16_23Sep2016EFV3_DATA"),(278802,"Summer16_23Sep2016GV3_DATA"),(280919,"Summer16_23Sep2016HV3_DATA")]
##Lets turn everything on for now, at least we know what is applied
#jetAna.addJECShifts = True
#jetAna.smearJets = False
#jetAna.recalibrateJets = True
#jetAna.applyL2L3Residual = "Data"
#metAna.recalibrate = True
##Reapply JEC anyway...
jetAna.addJECShifts = True
jetAna.smearJets = False
jetAna.recalibrateJets = True
jetAna.applyL2L3Residual = "Data"
metAna.recalibrate = True





#-------- HOW TO RUN
sample = 'MC'
#sample = 'data' #default
#sample = 'Signal'

multib = False
zerob = True

#-------- Preprocessor yes/no
cmssw = True

isData = False # default, but will be overwritten below
isSignal = False # default, but will be overwritten below
if sample == 'data':
  isData = True
elif sample == "Signal":
  isSignal = True

#Set this depending on the running mode
test = 1
#0: PRODUCTION (for batch)
#1: Usually for TESTING (single component with single thread)
#2: test all components (1 thread per comp)
#3: run all components (split jobs)
################################################################
###########################

####### Leptons  #####
# lep collection
lepAna.packedCandidates = 'packedPFCandidates'

## ELECTRONS
lepAna.loose_electron_eta = 2.4
lepAna.loose_electron_pt  = 10
lepAna.inclusive_electron_pt  = 10
if eleID == "CBID":
  lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto"
  lepAna.loose_electron_lostHits = 999. # no cut since embedded in ID
  lepAna.loose_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.loose_electron_dz     = 999. # no cut since embedded in ID

  lepAna.inclusive_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_Veto"
  lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

## MUONS
lepAna.loose_muon_pt  = 10
lepAna.inclusive_muon_pt  = 10
lepAna.loose_muon_id     = "POG_ID_Loose" #same as in core
lepAna.inclusive_muon_id     = "POG_ID_Loose" #same as in core

if isolation == "miniIso":
  # do miniIso
  lepAna.doMiniIsolation = True
  lepAna.miniIsolationPUCorr = 'rhoArea'
  lepAna.miniIsolationVetoLeptons = None
  lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
  lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == "relIso03":
  # normal relIso03
  lepAna.ele_isoCorr = "rhoArea"
  lepAna.mu_isoCorr = "rhoArea"

  lepAna.loose_electron_relIso = 0.5
  lepAna.loose_muon_relIso = 0.5

########################
###### ANALYZERS #######
########################

#add LHE ana for HT info
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig

from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
  ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
  minJets25 = 0,
  )

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
  minST = 150,
  )

from CMGTools.TTHAnalysis.analyzers.nIsrAnalyzer import NIsrAnalyzer
NIsrAnalyzer = cfg.Analyzer(
  NIsrAnalyzer, name='NIsrAnalyzer')
## HT skim
from CMGTools.TTHAnalysis.analyzers.ttHHTSkimmer import ttHHTSkimmer
ttHHTSkimmer = cfg.Analyzer(
  ttHHTSkimmer, name='ttHHTSkimmer',
  minHT = 350,
  )

#from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import * # central trigger list
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

#########################
# --- LEPTON SKIMMING ---
#########################

## OTHER LEPTON SKIMMER
anyLepSkim.minLeptons = 0
anyLepSkim.maxLeptons = 999

# GOOD LEPTON SKIMMER -- FROM TTH (in Core already)
ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999

####### JETS #########
jetAna.jetPt = 20
jetAna.jetEta = 2.4

# --- JET-LEPTON CLEANING ---
#jetAna.cleanSelectedLeptons = True
jetAna.minLepPt = 10

## JetAna
jetAna.doQG = True

## Iso Track #use basic relIso for now
isoTrackAna.setOff = False
isoTrackAna.doRelIsolation = True

# store all taus by default
genAna.allGenTaus = True


if sample == "MC":

  print 'Going to process MC'
  print 'If It fails due to susy masses please comment out necessary lines in TTHAnalysis/python/analyzers/treeProducerSusyCore.py for now'

  # apply a loose lepton skim to MC
  anyLepSkim.minLeptons = 1

  from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *

  #pick the file you want to run on
  selectedComponents = [WJetsToLNuHT]
#  [TTJets_SingleLeptonFromTbar,TTJets_SingleLeptonFromTbar_ext,TTJets_SingleLeptonFromT,TTJets_DiLepton,TTJets_DiLepton_ext,

  if test==1:
    # test a single component, using a single thread.
    comp = WJetsToLNuHT[0]
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
    # PRODUCTION
    # run on everything that is defined in selectedComponents

    #selectedComponents =  [TTJets_LO , TTJets_LO_HT600to800, TTJets_LO_HT800to1200, TTJets_LO_HT1200to2500, TTJets_LO_HT2500toInf] + QCDHT + WJetsToLNuHT + SingleTop + DYJetsM50HT + TTV
    selectedComponents = WJetsToLNuHT+DiBosons+DYJetsM50HT

    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)

elif sample == "Signal":

  print 'Going to process Signal, assuming it is FastSim'

  # Set FastSim JEC
  jetAna.mcGT = "Spring16_FastSimV1_MC"

  #### REMOVE JET ID FOR FASTSIM
  jetAna.relaxJetId = True

  # modify skim (noe leptons skim)
  anyLepSkim.minLeptons = 0

  from CMGTools.RootTools.samples.samples_80x_signal import *
  if multib: selectedComponents = [SMS_T1tttt_TuneCUETP8M1]
  if zerob: selectedComponents = [SMS_T5qqqqVV_TuneCUETP8M1]
  if multib and zerob : print "Warning ! Both zero b and multi b is set to  True, you will be running Zero b signals ;) Cheers from Ece"
  if not (multib or zerob) : print 8*"*", "Error ! Choose a signal to process", 8*"*"

  if test==1:
    # test a single component, using a single thread.
    if multib: comp  = SMS_T1tttt_TuneCUETP8M1
    if zerob: comp  = SMS_T5qqqqVV_TuneCUETP8M1
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
    # PRODUCTION
    # run on everything
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)



elif sample == "data":

  print 'Going to process DATA'

  # modify skim
  anyLepSkim.minLeptons = 1

  # central samples
  from CMGTools.RootTools.samples.samples_13TeV_Moriond2017 import *
  #selectedComponents = [JetHT_Run2016B_23Sep2016, HTMHT_Run2016B_23Sep2016, MET_Run2016B_23Sep2016, SingleElectron_Run2016B_23Sep2016, SingleMuon_Run2016B_23Sep2016, SinglePhoton_Run2016B_23Sep2016, DoubleEG_Run2016B_23Sep2016, MuonEG_Run2016B_23Sep2016, DoubleMuon_Run2016B_23Sep2016, Tau_Run2016B_23Sep2016]
  selectedComponents = [SingleElectron_Run2016H_03Feb2017_v2]
  #selectedComponents = [
  #                      SingleElectron_Run2016B_23Sep2016,\
  #                      SingleElectron_Run2016C_23Sep2016_v1,\
  #                      SingleElectron_Run2016D_23Sep2016_v1,\
  #                      SingleElectron_Run2016E_23Sep2016_v1,\
  #                      SingleElectron_Run2016F_23Sep2016_v1,\
  #                      SingleElectron_Run2016G_23Sep2016_v1,\
  #                      ]
  MET_03Feb2017 = [MET_Run2016B_03Feb2017_v2, MET_Run2016C_03Feb2017, MET_Run2016D_03Feb2017, MET_Run2016E_03Feb2017, MET_Run2016F_03Feb2017, MET_Run2016G_03Feb2017, MET_Run2016H_03Feb2017_v2, MET_Run2016H_03Feb2017_v3]
  SingleElectron_03Feb2017 = [SingleElectron_Run2016B_03Feb2017_v2, SingleElectron_Run2016C_03Feb2017, SingleElectron_Run2016D_03Feb2017, SingleElectron_Run2016E_03Feb2017, SingleElectron_Run2016F_03Feb2017, SingleElectron_Run2016G_03Feb2017, SingleElectron_Run2016H_03Feb2017_v2, SingleElectron_Run2016H_03Feb2017_v3]
  SingleMuon_03Feb2017 = [SingleMuon_Run2016B_03Feb2017_v2, SingleMuon_Run2016C_03Feb2017, SingleMuon_Run2016D_03Feb2017, SingleMuon_Run2016E_03Feb2017, SingleMuon_Run2016F_03Feb2017, SingleMuon_Run2016G_03Feb2017, SingleMuon_Run2016H_03Feb2017_v2, SingleMuon_Run2016H_03Feb2017_v3]

  selectedComponents = MET_03Feb2017 + SingleElectron_03Feb2017 + SingleMuon_03Feb2017

#  susyCoreSequence.insert(susyCoreSequence.index(metAna),
#      [metAnaEGClean, metAnaMuEGClean, metAnaUncorr] )
  susyCoreSequence.insert(susyCoreSequence.index(metAna),
      metAnaEGClean )
  susyCoreSequence.insert(susyCoreSequence.index(metAna),
      metAnaMuEGClean )
  susyCoreSequence.insert(susyCoreSequence.index(metAna),
      metAnaUncorr )

  if test!=0 and jsonAna in susyCoreSequence: susyCoreSequence.remove(jsonAna)
  if test==1:
    # test one component (2 thread)
    comp = SingleElectron_Run2016H_03Feb2017_v2
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



## PDF weights
PDFWeights = []
#PDFWeights = [ ("CT10",53), ("MSTW2008lo68cl",41), ("NNPDF21_100",101) ]
#PDFWeights = [ ("CT10nlo",53),("MSTW2008nlo68cl",41),("NNPDF30LO",101),("NNPDF30_nlo_nf_5_pdfas",103), ("NNPDF30_lo_as_0130",101)]
#PDFWeights = [ ("NNPDF30_lo_as_0130",101) ]
# see for TTJets  https://github.com/cms-sw/genproductions/blob/c41ab29f3d86c9e53df8b0d76c12cd519adbf013/bin/MadGraph5_aMCatNLO/cards/production/13TeV/tt0123j_5f_ckm_LO_MLM/tt0123j_5f_ckm_LO_MLM_run_card.dat#L52
# and then https://lhapdf.hepforge.org/pdfsets.html

#--------- Tree Producer
from CMGTools.TTHAnalysis.analyzers.treeProducerSusySingleLepton import *
treeProducer = cfg.Analyzer(
  AutoFillTreeProducer, name='treeProducerSusySingleLepton',
  vectorTree = True,
  saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
  defaultFloatType = 'F', # use Float_t for floating point
  PDFWeights = PDFWeights,
  globalVariables = susySingleLepton_globalVariables,
  globalObjects = susySingleLepton_globalObjects,
  collections = susySingleLepton_collections,
  )


if isSignal:
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

#-------- SEQUENCE
#add anyLepSkim directly after lepAna
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1, anyLepSkim)
sequence = cfg.Sequence(susyCoreSequence+[
    LHEAna,
    NIsrAnalyzer,
    ttHEventAna,
    ttHHTSkimmer,
    ttHSTSkimmer,
    treeProducer,
    ])

if isData:
  sequence.remove(anyLepSkim)
  sequence.remove(NIsrAnalyzer)
  sequence.remove(ttHSTSkimmer)
if not isSignal:
  sequence.remove(susyScanAna)

#remove all skims for signal
if isSignal:
 sequence.remove(anyLepSkim)
 sequence.remove(ttHHTSkimmer)
 sequence.remove(ttHSTSkimmer)
 sequence.remove(eventFlagsAna)
## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='treeProducerSusySingleLepton/tree.root',
    #fname='susyCounter/counts.root',
    option='recreate'
    )
outputService.append(output_service)

from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
preprocessor = None
if cmssw:
    fname = "$CMSSW_BASE/src/CMGTools/SUSYAnalysis/cfg/runBTaggingSlimPreprocessor_cfg.py"
    jetAna.jetCol = 'selectedUpdatedPatJets'
#    fname = "$CMSSW_BASE/src/CMGTools/SUSYAnalysis/cfg/MetType1_jec_Spring16_25nsV6_MC.py"
    preprocessor = CmsswPreprocessor(fname)#, addOrigAsSecondary=False)

print "running"
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
         sequence = sequence,
         services = outputService,
         preprocessor=preprocessor,
         events_class = Events)
