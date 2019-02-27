# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

# ----------------------------- 2017 pp run  ----------------------------------------
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json=dataDir+'/json/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

#json = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

run_range = (294927, 306462)
label = "_runs%s_%s" % (run_range[0], run_range[1])

# ----------------------------- Run2017B 31Mar2018 ----------------------------------------

JetHT_Run2017B_31Mar2018 = kreator.makeDataComponent("JetHT_Run2017B_31Mar2018", "/JetHT/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
HTMHT_Run2017B_31Mar2018 = kreator.makeDataComponent("HTMHT_Run2017B_31Mar2018", "/HTMHT/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MET_Run2017B_31Mar2018 = kreator.makeDataComponent("MET_Run2017B_31Mar2018", "/MET/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleElectron_Run2017B_31Mar2018 = kreator.makeDataComponent("SingleElectron_Run2017B_31Mar2018", "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017B_31Mar2018 = kreator.makeDataComponent("SingleMuon_Run2017B_31Mar2018", "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#SinglePhoton_Run2017B_31Mar2018 = kreator.makeDataComponent("SinglePhoton_Run2017B_31Mar2018", "/SinglePhoton/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleEG_Run2017B_31Mar2018 = kreator.makeDataComponent("DoubleEG_Run2017B_31Mar2018", "/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#MuonEG_Run2017B_31Mar2018 = kreator.makeDataComponent("MuonEG_Run2017B_31Mar2018", "/MuonEG/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleMuon_Run2017B_31Mar2018 = kreator.makeDataComponent("DoubleMuon_Run2017B_31Mar2018", "/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#Tau_Run2017B_31Mar2018 = kreator.makeDataComponent("Tau_Run2017B_31Mar2018", "/Tau/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

dataSamples_Run2017B_31Mar2018 = [JetHT_Run2017B_31Mar2018, HTMHT_Run2017B_31Mar2018, MET_Run2017B_31Mar2018, SingleElectron_Run2017B_31Mar2018, SingleMuon_Run2017B_31Mar2018]#, SinglePhoton_Run2017B_31Mar2018, DoubleEG_Run2017B_31Mar2018, MuonEG_Run2017B_31Mar2018, DoubleMuon_Run2017B_31Mar2018, Tau_Run2017B_31Mar2018]
dataSamples_Run2017B_31Mar2018_1l = [MET_Run2017B_31Mar2018, SingleElectron_Run2017B_31Mar2018, SingleMuon_Run2017B_31Mar2018]#, SinglePhoton_Run2017B_31Mar2018, DoubleEG_Run2017B_31Mar2018, MuonEG_Run2017B_31Mar2018, DoubleMuon_Run2017B_31Mar2018, Tau_Run2017B_31Mar2018]

# ----------------------------- Run2017C 31Mar2018 ----------------------------------------

JetHT_Run2017C_31Mar2018 = kreator.makeDataComponent("JetHT_Run2017C_31Mar2018", "/JetHT/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
HTMHT_Run2017C_31Mar2018 = kreator.makeDataComponent("HTMHT_Run2017C_31Mar2018", "/HTMHT/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MET_Run2017C_31Mar2018 = kreator.makeDataComponent("MET_Run2017C_31Mar2018", "/MET/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleElectron_Run2017C_31Mar2018 = kreator.makeDataComponent("SingleElectron_Run2017C_31Mar2018", "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017C_31Mar2018 = kreator.makeDataComponent("SingleMuon_Run2017C_31Mar2018", "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#SinglePhoton_Run2017C_31Mar2018 = kreator.makeDataComponent("SinglePhoton_Run2017C_31Mar2018", "/SinglePhoton/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleEG_Run2017C_31Mar2018 = kreator.makeDataComponent("DoubleEG_Run2017C_31Mar2018", "/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#MuonEG_Run2017C_31Mar2018 = kreator.makeDataComponent("MuonEG_Run2017C_31Mar2018", "/MuonEG/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleMuon_Run2017C_31Mar2018 = kreator.makeDataComponent("DoubleMuon_Run2017C_31Mar2018", "/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#Tau_Run2017C_31Mar2018 = kreator.makeDataComponent("Tau_Run2017C_31Mar2018", "/Tau/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

dataSamples_Run2017C_31Mar2018 = [JetHT_Run2017C_31Mar2018, HTMHT_Run2017C_31Mar2018, MET_Run2017C_31Mar2018, SingleElectron_Run2017C_31Mar2018, SingleMuon_Run2017C_31Mar2018]#, SinglePhoton_Run2017C_31Mar2018, DoubleEG_Run2017C_31Mar2018, MuonEG_Run2017C_31Mar2018, DoubleMuon_Run2017C_31Mar2018, Tau_Run2017C_31Mar2018]
dataSamples_Run2017C_31Mar2018_1l = [MET_Run2017C_31Mar2018, SingleElectron_Run2017C_31Mar2018, SingleMuon_Run2017C_31Mar2018]#, SinglePhoton_Run2017C_31Mar2018, DoubleEG_Run2017C_31Mar2018, MuonEG_Run2017C_31Mar2018, DoubleMuon_Run2017C_31Mar2018, Tau_Run2017C_31Mar2018]


# ----------------------------- Run2017D 31Mar2018 ----------------------------------------

JetHT_Run2017D_31Mar2018 = kreator.makeDataComponent("JetHT_Run2017D_31Mar2018", "/JetHT/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
HTMHT_Run2017D_31Mar2018 = kreator.makeDataComponent("HTMHT_Run2017D_31Mar2018", "/HTMHT/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MET_Run2017D_31Mar2018 = kreator.makeDataComponent("MET_Run2017D_31Mar2018", "/MET/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleElectron_Run2017D_31Mar2018 = kreator.makeDataComponent("SingleElectron_Run2017D_31Mar2018", "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017D_31Mar2018 = kreator.makeDataComponent("SingleMuon_Run2017D_31Mar2018", "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#SinglePhoton_Run2017D_31Mar2018 = kreator.makeDataComponent("SinglePhoton_Run2017D_31Mar2018", "/SinglePhoton/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleEG_Run2017D_31Mar2018 = kreator.makeDataComponent("DoubleEG_Run2017D_31Mar2018", "/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#MuonEG_Run2017D_31Mar2018 = kreator.makeDataComponent("MuonEG_Run2017D_31Mar2018", "/MuonEG/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleMuon_Run2017D_31Mar2018 = kreator.makeDataComponent("DoubleMuon_Run2017D_31Mar2018", "/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#Tau_Run2017D_31Mar2018 = kreator.makeDataComponent("Tau_Run2017D_31Mar2018", "/Tau/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

dataSamples_Run2017D_31Mar2018 = [JetHT_Run2017D_31Mar2018, HTMHT_Run2017D_31Mar2018, MET_Run2017D_31Mar2018, SingleElectron_Run2017D_31Mar2018, SingleMuon_Run2017D_31Mar2018]#, SinglePhoton_Run2017D_31Mar2018, DoubleEG_Run2017D_31Mar2018, MuonEG_Run2017D_31Mar2018, DoubleMuon_Run2017D_31Mar2018, Tau_Run2017D_31Mar2018]
dataSamples_Run2017D_31Mar2018_1l = [MET_Run2017D_31Mar2018, SingleElectron_Run2017D_31Mar2018, SingleMuon_Run2017D_31Mar2018]#, SinglePhoton_Run2017D_31Mar2018, DoubleEG_Run2017D_31Mar2018, MuonEG_Run2017D_31Mar2018, DoubleMuon_Run2017D_31Mar2018, Tau_Run2017D_31Mar2018]

# ----------------------------- Run2017E 31Mar2018 ----------------------------------------

JetHT_Run2017E_31Mar2018 = kreator.makeDataComponent("JetHT_Run2017E_31Mar2018", "/JetHT/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
HTMHT_Run2017E_31Mar2018 = kreator.makeDataComponent("HTMHT_Run2017E_31Mar2018", "/HTMHT/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MET_Run2017E_31Mar2018 = kreator.makeDataComponent("MET_Run2017E_31Mar2018", "/MET/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleElectron_Run2017E_31Mar2018 = kreator.makeDataComponent("SingleElectron_Run2017E_31Mar2018", "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017E_31Mar2018 = kreator.makeDataComponent("SingleMuon_Run2017E_31Mar2018", "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#SinglePhoton_Run2017E_31Mar2018 = kreator.makeDataComponent("SinglePhoton_Run2017E_31Mar2018", "/SinglePhoton/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleEG_Run2017E_31Mar2018 = kreator.makeDataComponent("DoubleEG_Run2017E_31Mar2018", "/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#MuonEG_Run2017E_31Mar2018 = kreator.makeDataComponent("MuonEG_Run2017E_31Mar2018", "/MuonEG/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleMuon_Run2017E_31Mar2018 = kreator.makeDataComponent("DoubleMuon_Run2017E_31Mar2018", "/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#Tau_Run2017E_31Mar2018 = kreator.makeDataComponent("Tau_Run2017E_31Mar2018", "/Tau/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

dataSamples_Run2017E_31Mar2018 = [JetHT_Run2017E_31Mar2018, HTMHT_Run2017E_31Mar2018, MET_Run2017E_31Mar2018, SingleElectron_Run2017E_31Mar2018, SingleMuon_Run2017E_31Mar2018]#, SinglePhoton_Run2017E_31Mar2018, DoubleEG_Run2017E_31Mar2018, MuonEG_Run2017E_31Mar2018, DoubleMuon_Run2017E_31Mar2018, Tau_Run2017E_31Mar2018]
dataSamples_Run2017E_31Mar2018_1l = [MET_Run2017E_31Mar2018, SingleElectron_Run2017E_31Mar2018, SingleMuon_Run2017E_31Mar2018]#, SinglePhoton_Run2017E_31Mar2018, DoubleEG_Run2017E_31Mar2018, MuonEG_Run2017E_31Mar2018, DoubleMuon_Run2017E_31Mar2018, Tau_Run2017E_31Mar2018]


# ----------------------------- Run2017F 31Mar2018 ----------------------------------------

JetHT_Run2017F_31Mar2018 = kreator.makeDataComponent("JetHT_Run2017F_31Mar2018", "/JetHT/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
HTMHT_Run2017F_31Mar2018 = kreator.makeDataComponent("HTMHT_Run2017F_31Mar2018", "/HTMHT/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MET_Run2017F_31Mar2018 = kreator.makeDataComponent("MET_Run2017F_31Mar2018", "/MET/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleElectron_Run2017F_31Mar2018 = kreator.makeDataComponent("SingleElectron_Run2017F_31Mar2018", "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017F_31Mar2018 = kreator.makeDataComponent("SingleMuon_Run2017F_31Mar2018", "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#SinglePhoton_Run2017F_31Mar2018 = kreator.makeDataComponent("SinglePhoton_Run2017F_31Mar2018", "/SinglePhoton/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleEG_Run2017F_31Mar2018 = kreator.makeDataComponent("DoubleEG_Run2017F_31Mar2018", "/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#MuonEG_Run2017F_31Mar2018 = kreator.makeDataComponent("MuonEG_Run2017F_31Mar2018", "/MuonEG/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#DoubleMuon_Run2017F_31Mar2018 = kreator.makeDataComponent("DoubleMuon_Run2017F_31Mar2018", "/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
#Tau_Run2017F_31Mar2018 = kreator.makeDataComponent("Tau_Run2017F_31Mar2018", "/Tau/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

dataSamples_Run2017F_31Mar2018 = [JetHT_Run2017F_31Mar2018, HTMHT_Run2017F_31Mar2018, MET_Run2017F_31Mar2018, SingleElectron_Run2017F_31Mar2018, SingleMuon_Run2017F_31Mar2018]#, SinglePhoton_Run2017F_31Mar2018, DoubleEG_Run2017F_31Mar2018, MuonEG_Run2017F_31Mar2018, DoubleMuon_Run2017F_31Mar2018, Tau_Run2017F_31Mar2018]
dataSamples_Run2017F_31Mar2018_1l = [MET_Run2017F_31Mar2018, SingleElectron_Run2017F_31Mar2018, SingleMuon_Run2017F_31Mar2018]#, SinglePhoton_Run2017F_31Mar2018, DoubleEG_Run2017F_31Mar2018, MuonEG_Run2017F_31Mar2018, DoubleMuon_Run2017F_31Mar2018, Tau_Run2017F_31Mar2018]

# Summary of 31Mar2018
dataSamples_31Mar2018 = dataSamples_Run2017B_31Mar2018 + dataSamples_Run2017C_31Mar2018 + dataSamples_Run2017D_31Mar2018 + dataSamples_Run2017E_31Mar2018 + dataSamples_Run2017F_31Mar2018
dataSamples_31Mar2018_1l = dataSamples_Run2017B_31Mar2018_1l + dataSamples_Run2017C_31Mar2018_1l + dataSamples_Run2017D_31Mar2018_1l + dataSamples_Run2017E_31Mar2018_1l + dataSamples_Run2017F_31Mar2018_1l

dataSamples = dataSamples_31Mar2018
dataSamples_1l = dataSamples_31Mar2018_1l

samples = dataSamples

# ---------------------------------------------------------------------

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples)
