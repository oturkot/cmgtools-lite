# COMPONENT CREATOR
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()
# QCD HT bins (cross sections from McM)
QCD_HT100to200 = kreator.makeMCComponent("QCD_HT100to200", "/QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.463e+07*1.13073)
QCD_HT200to300 = kreator.makeMCComponent("QCD_HT200to300", "/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 1.553e+06*1.1056)
QCD_HT300to500 = kreator.makeMCComponent("QCD_HT300to500", "/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 347500*1.01094)
QCD_HT500to700 = kreator.makeMCComponent("QCD_HT500to700", "/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 29930*1.0568)
QCD_HT700to1000 = kreator.makeMCComponent("QCD_HT700to1000", "/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 6370*1.06782)
QCD_HT1000to1500 = kreator.makeMCComponent("QCD_HT1000to1500", "/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1100*1.09636)
QCD_HT1500to2000 = kreator.makeMCComponent("QCD_HT1500to2000", "/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 98.71)
QCD_HT2000toInf = kreator.makeMCComponent("QCD_HT2000toInf", "/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 20.2)

QCDHT = [
    QCD_HT100to200,
    QCD_HT200to300,
    QCD_HT300to500,
    QCD_HT500to700,
    QCD_HT700to1000,
    QCD_HT1000to1500,
    QCD_HT1500to2000,
    QCD_HT2000toInf,
]



# ====== W + Jets ======
WJetsToLNu_LO = kreator.makeMCComponent("WJetsToLNu_LO","/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 3* 20508.9)
WJetsToLNu_LO_ext = kreator.makeMCComponent("WJetsToLNu_LO_ext","/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", "CMS", ".*root", 3* 20508.9)

## LO XSec from genXSecAna times NNLO/LO XSec for inclusive W+jets

### W+jets
WJetsToLNu_HT100to200 = kreator.makeMCComponent("WJetsToLNu_HT100to200", "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",1345*1.21)
WJetsToLNu_HT200to400 = kreator.makeMCComponent("WJetsToLNu_HT200to400", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",359.7*1.21)
WJetsToLNu_HT400to600 = kreator.makeMCComponent("WJetsToLNu_HT400to600", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",48.91*1.21)
WJetsToLNu_HT600to800 = kreator.makeMCComponent("WJetsToLNu_HT600to800", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",12.05*1.21)
WJetsToLNu_HT800to1200  = kreator.makeMCComponent("WJetsToLNu_HT800to1200", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",5.501*1.21)
WJetsToLNu_HT1200to2500 = kreator.makeMCComponent("WJetsToLNu_HT1200to2500", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",1.329*1.21)
WJetsToLNu_HT2500toInf  = kreator.makeMCComponent("WJetsToLNu_HT2500toInf", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", "CMS", ".*root",0.03216*1.21)


WJetsToLNuHT = [
WJetsToLNu_HT100to200,
WJetsToLNu_HT200to400,
WJetsToLNu_HT400to600,
WJetsToLNu_HT600to800,
WJetsToLNu_HT800to1200,
WJetsToLNu_HT1200to2500,
WJetsToLNu_HT2500toInf,
]


# ====== Z + Jets ======
## Cross sections from getXSecAnalyzer times k-factor 1.08 from ratio of FEWZ to inclusive DYJetsToLL_M50_LO
DYJetsToLL_M50_HT100to200      = kreator.makeMCComponent("DYJetsToLL_M50_HT100to200",       "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM",       "CMS", ".*root", 161.1*1.08)
DYJetsToLL_M50_HT200to400_ext1 = kreator.makeMCComponent("DYJetsToLL_M50_HT200to400_ext1",  "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM",   "CMS", ".*root", 161.1*1.08)
DYJetsToLL_M50_HT200to400      = kreator.makeMCComponent("DYJetsToLL_M50_HT200to400",       "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",       "CMS", ".*root", 49.32*1.08)
DYJetsToLL_M50_HT400to600      = kreator.makeMCComponent("DYJetsToLL_M50_HT400to600",       "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM",       "CMS", ".*root", 7.021*1.08)
DYJetsToLL_M50_HT400to600_ext1 = kreator.makeMCComponent("DYJetsToLL_M50_HT400to600_ext1",  "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM",  "CMS", ".*root", 7.021*1.08)
DYJetsToLL_M50_HT600to800      = kreator.makeMCComponent("DYJetsToLL_M50_HT600to800",       "/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM",       "CMS", ".*root", 1.743*1.08 )
DYJetsToLL_M50_HT800to1200     = kreator.makeMCComponent("DYJetsToLL_M50_HT800to1200",      "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM",      "CMS", ".*root", 0.8082*1.08 )
DYJetsToLL_M50_HT1200to2500    = kreator.makeMCComponent("DYJetsToLL_M50_HT1200to2500",     "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM",     "CMS", ".*root", 0.1925*1.08 )
DYJetsToLL_M50_HT2500toInf     = kreator.makeMCComponent("DYJetsToLL_M50_HT2500toInf",      "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM",      "CMS", ".*root", 0.003486*1.08 )

DYJetsToLLM50HT = [
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,#     DYJetsToLL_M50_HT200to400_ext1,
    DYJetsToLL_M50_HT400to600,#     DYJetsToLL_M50_HT400to600_ext1,
    DYJetsToLL_M50_HT600to800,
    DYJetsToLL_M50_HT800to1200,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf,
]

DYs = DYJetsToLLM50HT  







# ====== TT INCLUSIVE =====
# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)
TTJets = kreator.makeMCComponent("TTJets", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76, fracNegWeights=0.319)
#TTJets_LO = kreator.makeMCComponent("TTJets_LO", "/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76)
#TT_pow = kreator.makeMCComponent("TTbar", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 831.762)
TTJets_SingleLeptonFromTbar     = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar"    , "/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )
TTJets_SingleLeptonFromT        = kreator.makeMCComponent("TTJets_SingleLeptonFromT"       , "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
TTJets_DiLepton                 = kreator.makeMCComponent("TTJets_DiLepton"                , "/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     , "CMS", ".*root", 831.76*((3*0.108)**2) )
# Xsec from XsecDB (not available YET)
TTJets_SingleLeptonFromTbar_genMET     = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar_genMET"    , "/TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )
#TTJets_SingleLeptonFromTbar_genMET_ext = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar_genMET_ext", "/TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
TTJets_SingleLeptonFromT_genMET        = kreator.makeMCComponent("TTJets_SingleLeptonFromT_genMET"       , "/TTJets_SingleLeptFromT_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
TTJets_DiLepton_genMET                 = kreator.makeMCComponent("TTJets_DiLepton_genMET"                 , "/TTJets_DiLept_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"     , "CMS", ".*root", 831.76*((3*0.108)**2) )
#
TTJets_LO_HT600to800       = kreator.makeMCComponent("TTJets_LO_HT600to800",  "/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1.610*831.76/502.2)
TTJets_LO_HT800to1200      = kreator.makeMCComponent("TTJets_LO_HT800to1200", "/TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.663*831.76/502.2)
TTJets_LO_HT1200to2500     = kreator.makeMCComponent("TTJets_LO_HT1200to2500","/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.12*831.76/502.2)
TTJets_LO_HT2500toInf      = kreator.makeMCComponent("TTJets_LO_HT2500toInf", "/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", "CMS", ".*root", 0.001430*831.76/502.2)


TTs = [
#TTJets,

TTJets_SingleLeptonFromTbar,
TTJets_SingleLeptonFromT,
TTJets_DiLepton,
TTJets_LO_HT600to800,
TTJets_LO_HT800to1200,
TTJets_LO_HT1200to2500,
TTJets_LO_HT2500toInf,
#TTJets_SingleLeptonFromTbar_genMET,  
#TTJets_SingleLeptonFromTbar_genMET_ext,
#TTJets_SingleLeptonFromT_genMET,
#TTJets_DiLepton_genMET,       

]

# ====== SINGLE TOP ======
# Single top cross sections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
TToLeptons_sch_amcatnlo = kreator.makeMCComponent("TToLeptons_sch", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", (7.20+4.16)*0.108*3)
T_tch_powheg = kreator.makeMCComponent("T_tch_powheg", "/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 136.02) # inclusive sample
TBar_tch_powheg = kreator.makeMCComponent("TBar_tch_powheg", "/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 80.95) # inclusive sample

TBar_tWch_ext1 = kreator.makeMCComponent("TBar_tWch_ext1", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root",19.55)
TBar_tWch_ext2 = kreator.makeMCComponent("TBar_tWch_ext2", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",19.55)
TBar_tWch      = kreator.makeMCComponent("TBar_tWch"     , "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",19.55)
T_tWch_ext1 = kreator.makeMCComponent("T_tWch_ext1", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",19.55)
T_tWch      = kreator.makeMCComponent("T_tWch"     , "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",19.55)

SingleTop = [
TToLeptons_sch_amcatnlo,
T_tch_powheg,
TBar_tch_powheg,
#TBar_tWch_ext1,
#TBar_tWch_ext2,
TBar_tWch,
#T_tWch_ext1,
T_tWch,
]


### TTV
TTWToLNu = kreator.makeMCComponent("TTWToLNu", "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.2043)
TTWToQQ = kreator.makeMCComponent("TTWToQQ", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 0.40620)
TTZToQQ = kreator.makeMCComponent("TTZToQQ","/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 0.5297)
TTZToLLNuNu = kreator.makeMCComponent("TTZToLLNuNu","/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.2529)
# https://twiki.cern.ch/twiki/bin/view/CMS/SameSignDilepton2016
TTZ_LO = kreator.makeMCComponent("TTZ_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",  0.5297/0.692)

TTV = [
TTWToLNu,
TTWToQQ,
TTZToQQ,
TTZToLLNuNu,
TTZ_LO,
]


# ===  DI-BOSONS
# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson

WWTo2L2Nu = kreator.makeMCComponent("WWTo2L2Nu", "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 10.481 )
WWToLNuQQ = kreator.makeMCComponent("WWToLNuQQ", "/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 43.53 )
WWToLNuQQ_ext = kreator.makeMCComponent("WWToLNuQQ_ext", "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root", 43.53 )
WWTo1L1Nu2Q = kreator.makeMCComponent("WWTo1L1Nu2Q", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 49.997 )

ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.564)
ZZTo2L2Q = kreator.makeMCComponent("ZZTo2L2Q", "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",  3.28)
ZZTo2Q2Nu = kreator.makeMCComponent("ZZTo2Q2Nu", "/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",  4.04)
ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 0.564)

WZTo1L3Nu   = kreator.makeMCComponent("WZTo1L3Nu"  , "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"  , "CMS", ".*root", (47.13)*(3*0.108)*(0.2) )
WZTo1L1Nu2Q = kreator.makeMCComponent("WZTo1L1Nu2Q", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",  10.71)
WZTo2L2Q    = kreator.makeMCComponent("WZTo2L2Q"   , "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM" , "CMS", ".*root",  5.60)
#WZTo3LNu = kreator.makeMCComponent("WZTo3LNu", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 4.42965)
WZTo3LNu_amcatnlo = kreator.makeMCComponent("WZTo3LNu_amcatnlo", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 4.666)

DiBosons = [
WWTo2L2Nu,
WWToLNuQQ,
#WWToLNuQQ_ext,
WWTo1L1Nu2Q,
ZZTo2L2Nu,
ZZTo2L2Q,
ZZTo2Q2Nu,
ZZTo2L2Nu,
WZTo1L3Nu,
WZTo1L1Nu2Q,
WZTo2L2Q,
WZTo3LNu_amcatnlo,
]


# ----------------------------- summary ----------------------------------------


mcSamples = QCDHT + WJetsToLNuHT + DYs + TTs + SingleTop + TTV + DiBosons


samples = mcSamples

# ---------------------------------------------------------------------

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, localobjs=locals())
