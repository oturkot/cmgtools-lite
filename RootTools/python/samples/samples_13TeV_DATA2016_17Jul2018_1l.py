import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

run_range = (271036, 284044)
label = "_runs%s_%s"%(run_range[0], run_range[1])



### ----------------------------- Run2016B v2 17Jul2018 ----------------------------------------

JetHT_Run2016B_17Jul2018_v2       = kreator.makeDataComponent("JetHT_Run2016B_17Jul2018_v2"      , "/JetHT/Run2016B-17Jul2018_ver2-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_17Jul2018_v2       = kreator.makeDataComponent("HTMHT_Run2016B_17Jul2018_v2"      , "/HTMHT/Run2016B-17Jul2018_ver2-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_17Jul2018_v2         = kreator.makeDataComponent("MET_Run2016B_17Jul2018_v2"        , "/MET/Run2016B-17Jul2018_ver2-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_17Jul2018_v2 = kreator.makeDataComponent("SingleElectron_Run2016B_17Jul2018_v2", "/SingleElectron/Run2016B-17Jul2018_ver2-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_17Jul2018_v2  = kreator.makeDataComponent("SingleMuon_Run2016B_17Jul2018_v2" , "/SingleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_17Jul2018_v2= kreator.makeDataComponent("SinglePhoton_Run2016B_17Jul2018_v2"  , "/SinglePhoton/Run2016B-17Jul2018_ver2-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_17Jul2018_v2    = kreator.makeDataComponent("DoubleEG_Run2016B_17Jul2018_v2"   , "/DoubleEG/Run2016B-17Jul2018_ver2-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_17Jul2018_v2     = kreator.makeDataComponent("MuonEG_Run2016B_17Jul2018_v2"     , "/MuonEG/Run2016B-17Jul2018_ver2-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_17Jul2018_v2  = kreator.makeDataComponent("DoubleMuon_Run2016B_17Jul2018_v2" , "/DoubleMuon/Run2016B-17Jul2018_ver2-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016B_17Jul2018_v2  = kreator.makeDataComponent("Tau_Run2016B_17Jul2018_v2" , "/Tau/Run2016B-17Jul2018_ver2-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016B_17Jul2018_v2 = [JetHT_Run2016B_17Jul2018_v2, HTMHT_Run2016B_17Jul2018_v2, MET_Run2016B_17Jul2018_v2, SingleElectron_Run2016B_17Jul2018_v2, SingleMuon_Run2016B_17Jul2018_v2]#, SinglePhoton_Run2016B_17Jul2018_v2, DoubleEG_Run2016B_17Jul2018_v2, MuonEG_Run2016B_17Jul2018_v2, DoubleMuon_Run2016B_17Jul2018_v2, Tau_Run2016B_17Jul2018_v2]
dataSamples_Run2016B_17Jul2018_v2_1l = [MET_Run2016B_17Jul2018_v2, SingleElectron_Run2016B_17Jul2018_v2, SingleMuon_Run2016B_17Jul2018_v2]#, SinglePhoton_Run2016B_17Jul2018_v2, DoubleEG_Run2016B_17Jul2018_v2, MuonEG_Run2016B_17Jul2018_v2, DoubleMuon_Run2016B_17Jul2018_v2, Tau_Run2016B_17Jul2018_v2]

### ----------------------------- Run2016C 17Jul2018 ----------------------------------------

JetHT_Run2016C_17Jul2018          = kreator.makeDataComponent("JetHT_Run2016C_17Jul2018"         , "/JetHT/Run2016C-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016C_17Jul2018          = kreator.makeDataComponent("HTMHT_Run2016C_17Jul2018"         , "/HTMHT/Run2016C-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016C_17Jul2018            = kreator.makeDataComponent("MET_Run2016C_17Jul2018"           , "/MET/Run2016C-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016C_17Jul2018 = kreator.makeDataComponent("SingleElectron_Run2016C_17Jul2018", "/SingleElectron/Run2016C-17Jul2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_17Jul2018     = kreator.makeDataComponent("SingleMuon_Run2016C_17Jul2018"    , "/SingleMuon/Run2016C-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016C_17Jul2018   = kreator.makeDataComponent("SinglePhoton_Run2016C_17Jul2018"  , "/SinglePhoton/Run2016C-17Jul2018-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016C_17Jul2018       = kreator.makeDataComponent("DoubleEG_Run2016C_17Jul2018"      , "/DoubleEG/Run2016C-17Jul2018-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016C_17Jul2018         = kreator.makeDataComponent("MuonEG_Run2016C_17Jul2018"        , "/MuonEG/Run2016C-17Jul2018-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016C_17Jul2018     = kreator.makeDataComponent("DoubleMuon_Run2016C_17Jul2018"    , "/DoubleMuon/Run2016C-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016C_17Jul2018            = kreator.makeDataComponent("Tau_Run2016C_17Jul2018"           , "/Tau/Run2016C-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016C_17Jul2018 = [JetHT_Run2016C_17Jul2018, HTMHT_Run2016C_17Jul2018, MET_Run2016C_17Jul2018, SingleElectron_Run2016C_17Jul2018, SingleMuon_Run2016C_17Jul2018]#, SinglePhoton_Run2016C_17Jul2018, DoubleEG_Run2016C_17Jul2018, MuonEG_Run2016C_17Jul2018, DoubleMuon_Run2016C_17Jul2018, Tau_Run2016C_17Jul2018]
dataSamples_Run2016C_17Jul2018_1l = [MET_Run2016C_17Jul2018, SingleElectron_Run2016C_17Jul2018, SingleMuon_Run2016C_17Jul2018]#, SinglePhoton_Run2016C_17Jul2018, DoubleEG_Run2016C_17Jul2018, MuonEG_Run2016C_17Jul2018, DoubleMuon_Run2016C_17Jul2018, Tau_Run2016C_17Jul2018]


### ----------------------------- Run2016D 17Jul2018 v2 ----------------------------------------

JetHT_Run2016D_17Jul2018          = kreator.makeDataComponent("JetHT_Run2016D_17Jul2018"         , "/JetHT/Run2016D-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016D_17Jul2018          = kreator.makeDataComponent("HTMHT_Run2016D_17Jul2018"         , "/HTMHT/Run2016D-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016D_17Jul2018            = kreator.makeDataComponent("MET_Run2016D_17Jul2018"           , "/MET/Run2016D-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016D_17Jul2018 = kreator.makeDataComponent("SingleElectron_Run2016D_17Jul2018", "/SingleElectron/Run2016D-17Jul2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016D_17Jul2018     = kreator.makeDataComponent("SingleMuon_Run2016D_17Jul2018"    , "/SingleMuon/Run2016D-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016D_17Jul2018   = kreator.makeDataComponent("SinglePhoton_Run2016D_17Jul2018"  , "/SinglePhoton/Run2016D-17Jul2018-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016D_17Jul2018       = kreator.makeDataComponent("DoubleEG_Run2016D_17Jul2018"      , "/DoubleEG/Run2016D-17Jul2018-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016D_17Jul2018         = kreator.makeDataComponent("MuonEG_Run2016D_17Jul2018"        , "/MuonEG/Run2016D-17Jul2018-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016D_17Jul2018     = kreator.makeDataComponent("DoubleMuon_Run2016D_17Jul2018"    , "/DoubleMuon/Run2016D-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016D_17Jul2018            = kreator.makeDataComponent("Tau_Run2016D_17Jul2018"           , "/Tau/Run2016D-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016D_17Jul2018 = [JetHT_Run2016D_17Jul2018, HTMHT_Run2016D_17Jul2018, MET_Run2016D_17Jul2018, SingleElectron_Run2016D_17Jul2018, SingleMuon_Run2016D_17Jul2018]#, SinglePhoton_Run2016D_17Jul2018, DoubleEG_Run2016D_17Jul2018, MuonEG_Run2016D_17Jul2018, DoubleMuon_Run2016D_17Jul2018, Tau_Run2016D_17Jul2018]
dataSamples_Run2016D_17Jul2018_1l = [MET_Run2016D_17Jul2018, SingleElectron_Run2016D_17Jul2018, SingleMuon_Run2016D_17Jul2018]#, SinglePhoton_Run2016D_17Jul2018, DoubleEG_Run2016D_17Jul2018, MuonEG_Run2016D_17Jul2018, DoubleMuon_Run2016D_17Jul2018, Tau_Run2016D_17Jul2018]

### ----------------------------- Run2016E 17Jul2018 v2 ----------------------------------------

JetHT_Run2016E_17Jul2018          = kreator.makeDataComponent("JetHT_Run2016E_17Jul2018"         , "/JetHT/Run2016E-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016E_17Jul2018          = kreator.makeDataComponent("HTMHT_Run2016E_17Jul2018"         , "/HTMHT/Run2016E-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016E_17Jul2018            = kreator.makeDataComponent("MET_Run2016E_17Jul2018"           , "/MET/Run2016E-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016E_17Jul2018 = kreator.makeDataComponent("SingleElectron_Run2016E_17Jul2018", "/SingleElectron/Run2016E-17Jul2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_17Jul2018     = kreator.makeDataComponent("SingleMuon_Run2016E_17Jul2018"    , "/SingleMuon/Run2016E-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016E_17Jul2018   = kreator.makeDataComponent("SinglePhoton_Run2016E_17Jul2018"  , "/SinglePhoton/Run2016E-17Jul2018-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016E_17Jul2018       = kreator.makeDataComponent("DoubleEG_Run2016E_17Jul2018"      , "/DoubleEG/Run2016E-17Jul2018-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016E_17Jul2018         = kreator.makeDataComponent("MuonEG_Run2016E_17Jul2018"        , "/MuonEG/Run2016E-17Jul2018-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_17Jul2018     = kreator.makeDataComponent("DoubleMuon_Run2016E_17Jul2018"    , "/DoubleMuon/Run2016E-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016E_17Jul2018            = kreator.makeDataComponent("Tau_Run2016E_17Jul2018"           , "/Tau/Run2016E-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016E_17Jul2018 = [JetHT_Run2016E_17Jul2018, HTMHT_Run2016E_17Jul2018, MET_Run2016E_17Jul2018, SingleElectron_Run2016E_17Jul2018, SingleMuon_Run2016E_17Jul2018]#, SinglePhoton_Run2016E_17Jul2018, DoubleEG_Run2016E_17Jul2018, MuonEG_Run2016E_17Jul2018, DoubleMuon_Run2016E_17Jul2018, Tau_Run2016E_17Jul2018]
dataSamples_Run2016E_17Jul2018_1l = [MET_Run2016E_17Jul2018, SingleElectron_Run2016E_17Jul2018, SingleMuon_Run2016E_17Jul2018]#, SinglePhoton_Run2016E_17Jul2018, DoubleEG_Run2016E_17Jul2018, MuonEG_Run2016E_17Jul2018, DoubleMuon_Run2016E_17Jul2018, Tau_Run2016E_17Jul2018]


### ----------------------------- Run2016F 17Jul2018 v1 ----------------------------------------

JetHT_Run2016F_17Jul2018          = kreator.makeDataComponent("JetHT_Run2016F_17Jul2018"         , "/JetHT/Run2016F-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016F_17Jul2018          = kreator.makeDataComponent("HTMHT_Run2016F_17Jul2018"         , "/HTMHT/Run2016F-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016F_17Jul2018            = kreator.makeDataComponent("MET_Run2016F_17Jul2018"           , "/MET/Run2016F-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016F_17Jul2018 = kreator.makeDataComponent("SingleElectron_Run2016F_17Jul2018", "/SingleElectron/Run2016F-17Jul2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016F_17Jul2018     = kreator.makeDataComponent("SingleMuon_Run2016F_17Jul2018"    , "/SingleMuon/Run2016F-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016F_17Jul2018   = kreator.makeDataComponent("SinglePhoton_Run2016F_17Jul2018"  , "/SinglePhoton/Run2016F-17Jul2018-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016F_17Jul2018       = kreator.makeDataComponent("DoubleEG_Run2016F_17Jul2018"      , "/DoubleEG/Run2016F-17Jul2018-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016F_17Jul2018         = kreator.makeDataComponent("MuonEG_Run2016F_17Jul2018"        , "/MuonEG/Run2016F-17Jul2018-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016F_17Jul2018     = kreator.makeDataComponent("DoubleMuon_Run2016F_17Jul2018"    , "/DoubleMuon/Run2016F-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016F_17Jul2018            = kreator.makeDataComponent("Tau_Run2016F_17Jul2018"           , "/Tau/Run2016F-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)

dataSamples_Run2016F_17Jul2018 = [JetHT_Run2016F_17Jul2018, HTMHT_Run2016F_17Jul2018, MET_Run2016F_17Jul2018, SingleElectron_Run2016F_17Jul2018, SingleMuon_Run2016F_17Jul2018]#, SinglePhoton_Run2016F_17Jul2018, DoubleEG_Run2016F_17Jul2018, MuonEG_Run2016F_17Jul2018, DoubleMuon_Run2016F_17Jul2018, Tau_Run2016F_17Jul2018]
dataSamples_Run2016F_17Jul2018_1l = [MET_Run2016F_17Jul2018, SingleElectron_Run2016F_17Jul2018, SingleMuon_Run2016F_17Jul2018]#, SinglePhoton_Run2016F_17Jul2018, DoubleEG_Run2016F_17Jul2018, MuonEG_Run2016F_17Jul2018, DoubleMuon_Run2016F_17Jul2018, Tau_Run2016F_17Jul2018]

### ----------------------------- Run2016G 17Jul2018 v1 ----------------------------------------

JetHT_Run2016G_17Jul2018          = kreator.makeDataComponent("JetHT_Run2016G_17Jul2018"         , "/JetHT/Run2016G-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016G_17Jul2018          = kreator.makeDataComponent("HTMHT_Run2016G_17Jul2018"         , "/HTMHT/Run2016G-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016G_17Jul2018            = kreator.makeDataComponent("MET_Run2016G_17Jul2018"           , "/MET/Run2016G-17Jul2018-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016G_17Jul2018 = kreator.makeDataComponent("SingleElectron_Run2016G_17Jul2018", "/SingleElectron/Run2016G-17Jul2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016G_17Jul2018     = kreator.makeDataComponent("SingleMuon_Run2016G_17Jul2018"    , "/SingleMuon/Run2016G-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016G_17Jul2018   = kreator.makeDataComponent("SinglePhoton_Run2016G_17Jul2018"  , "/SinglePhoton/Run2016G-17Jul2018-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016G_17Jul2018       = kreator.makeDataComponent("DoubleEG_Run2016G_17Jul2018"      , "/DoubleEG/Run2016G-17Jul2018-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016G_17Jul2018        = kreator.makeDataComponent("MuonEG_Run2016G_17Jul2018"        , "/MuonEG/Run2016G-17Jul2018-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016G_17Jul2018     = kreator.makeDataComponent("DoubleMuon_Run2016G_17Jul2018"    , "/DoubleMuon/Run2016G-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016G_17Jul2018     = kreator.makeDataComponent("Tau_Run2016G_17Jul2018"    , "/Tau/Run2016G-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016G_17Jul2018 = [JetHT_Run2016G_17Jul2018, HTMHT_Run2016G_17Jul2018, MET_Run2016G_17Jul2018, SingleElectron_Run2016G_17Jul2018, SingleMuon_Run2016G_17Jul2018]#, SinglePhoton_Run2016G_17Jul2018, DoubleEG_Run2016G_17Jul2018, MuonEG_Run2016G_17Jul2018, DoubleMuon_Run2016G_17Jul2018, Tau_Run2016G_17Jul2018]
dataSamples_Run2016G_17Jul2018_1l = [MET_Run2016G_17Jul2018, SingleElectron_Run2016G_17Jul2018, SingleMuon_Run2016G_17Jul2018]#, SinglePhoton_Run2016G_17Jul2018, DoubleEG_Run2016G_17Jul2018, MuonEG_Run2016G_17Jul2018, DoubleMuon_Run2016G_17Jul2018, Tau_Run2016G_17Jul2018]

### ----------------------------- Run2016H 17Jul2018_ver2-v1 ----------------------------------------

JetHT_Run2016H_17Jul2018_v1          = kreator.makeDataComponent("JetHT_Run2016H_17Jul2018_v1"         , "/JetHT/Run2016H-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016H_17Jul2018_v1          = kreator.makeDataComponent("HTMHT_Run2016H_17Jul2018_v1"         , "/HTMHT/Run2016H-17Jul2018-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016H_17Jul2018_v1            = kreator.makeDataComponent("MET_Run2016H_17Jul2018_v1"           , "/MET/Run2016H-17Jul2018-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016H_17Jul2018_v1 = kreator.makeDataComponent("SingleElectron_Run2016H_17Jul2018_v1", "/SingleElectron/Run2016H-17Jul2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016H_17Jul2018_v1     = kreator.makeDataComponent("SingleMuon_Run2016H_17Jul2018_v1"    , "/SingleMuon/Run2016H-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016H_17Jul2018_v1   = kreator.makeDataComponent("SinglePhoton_Run2016H_17Jul2018_v1"  , "/SinglePhoton/Run2016H-17Jul2018-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016H_17Jul2018_v1       = kreator.makeDataComponent("DoubleEG_Run2016H_17Jul2018_v1"      , "/DoubleEG/Run2016H-17Jul2018-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016H_17Jul2018_v1        = kreator.makeDataComponent("MuonEG_Run2016H_17Jul2018_v1"        , "/MuonEG/Run2016H-17Jul2018-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016H_17Jul2018_v1     = kreator.makeDataComponent("DoubleMuon_Run2016H_17Jul2018_v1"    , "/DoubleMuon/Run2016H-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)
Tau_Run2016H_17Jul2018_v1     = kreator.makeDataComponent("Tau_Run2016H_17Jul2018_v1"    , "/Tau/Run2016H-17Jul2018-v1/MINIAOD"    , "CMS", ".*root", json)

dataSamples_Run2016H_17Jul2018_v1 = [JetHT_Run2016H_17Jul2018_v1, HTMHT_Run2016H_17Jul2018_v1, MET_Run2016H_17Jul2018_v1, SingleElectron_Run2016H_17Jul2018_v1, SingleMuon_Run2016H_17Jul2018_v1]#, SinglePhoton_Run2016H_17Jul2018_v1, DoubleEG_Run2016H_17Jul2018_v1, MuonEG_Run2016H_17Jul2018_v1, DoubleMuon_Run2016H_17Jul2018_v1, Tau_Run2016H_17Jul2018_v1]
dataSamples_Run2016H_17Jul2018_v1_1l = [MET_Run2016H_17Jul2018_v1, SingleElectron_Run2016H_17Jul2018_v1, SingleMuon_Run2016H_17Jul2018_v1]

### Summary of 17Jul2018
dataSamples_17Jul2018 = dataSamples_Run2016B_17Jul2018_v2 + dataSamples_Run2016C_17Jul2018 + dataSamples_Run2016D_17Jul2018 + dataSamples_Run2016E_17Jul2018 + dataSamples_Run2016F_17Jul2018 + dataSamples_Run2016G_17Jul2018 + dataSamples_Run2016H_17Jul2018_v1 
dataSamples_17Jul2018_1l = dataSamples_Run2016B_17Jul2018_v2_1l + dataSamples_Run2016C_17Jul2018_1l + dataSamples_Run2016D_17Jul2018_1l + dataSamples_Run2016E_17Jul2018_1l + dataSamples_Run2016F_17Jul2018_1l + dataSamples_Run2016G_17Jul2018_1l + dataSamples_Run2016H_17Jul2018_v1_1l 


dataSamples = dataSamples_17Jul2018
samples = dataSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
