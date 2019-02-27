import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### NB: Commented lines refer to samples available in RunIIFall15MiniAODv2 but not yet in RunIISpring16MiniAODv1

### ----------------------------- 25 ns ----------------------------------------

# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)
#TTJets = kreator.makeMCComponent("TTJets", "/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 831.76)
# NOTAVAILYET # TTJets_reHLT = kreator.makeMCComponent("TTJets_reHLT", "/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM", "CMS", ".*root", 831.76)

#TTJets_ext = kreator.makeMCComponent("TTJets_ext", "/TTJets_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76)
#TTJets_LO = kreator.makeMCComponent("TTJets_LO", "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 831.76)
#TT_pow = kreator.makeMCComponent("TT_pow", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 831.762)
#TT_pow_ext3 = kreator.makeMCComponent("TT_pow_ext3", "/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 831.76)
# NOTAVAILYET # TT_pow_ext4 = kreator.makeMCComponent("TT_pow_ext4", "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext4-v1/MINIAODSIM", "CMS", ".*root", 831.76)

TTJets_SingleLeptonFromTbar     = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar"    , "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )
TTJets_SingleLeptonFromTbar_ext = kreator.makeMCComponent("TTJets_SingleLeptonFromTbar_ext", "/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108) )
TTJets_SingleLeptonFromT        = kreator.makeMCComponent("TTJets_SingleLeptonFromT"       , "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
TTJets_SingleLeptonFromT_ext    = kreator.makeMCComponent("TTJets_SingleLeptonFromT_ext"   , "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root", 831.76*(3*0.108)*(1-3*0.108))
TTJets_DiLepton                 = kreator.makeMCComponent("TTJets_DiLepton"                , "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"     , "CMS", ".*root", 831.76*((3*0.108)**2) )
TTJets_DiLepton_ext             = kreator.makeMCComponent("TTJets_DiLepton_ext"            , "/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )

TTLep_pow = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
# NOTAVAILYET # TTLep_pow_ext = kreator.makeMCComponent("TTLep_pow_ext", "/TTTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) )
TTSemiLep_pow = kreator.makeMCComponent("TTSemiLep_pow", "/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 2*831.76*(3*0.108)*(1-3*0.108) )

#
# NOTAVAILYET # TTJets_LO_HT600to800       = kreator.makeMCComponent("TTJets_LO_HT600to800", "/TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 1.610*831.76/502.2)
TTJets_LO_HT600to800_ext   = kreator.makeMCComponent("TTJets_LO_HT600to800_ext", "/TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root", 1.610*831.76/502.2)
# NOTAVAILYET # TTJets_LO_HT800to1200      = kreator.makeMCComponent("TTJets_LO_HT800to1200", "/TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 0.663*831.76/502.2)
TTJets_LO_HT800to1200_ext  = kreator.makeMCComponent("TTJets_LO_HT800to1200_ext", "/TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM",  "CMS", ".*root", 0.663*831.76/502.2)
# NOTAVAILYET # TTJets_LO_HT1200to2500     = kreator.makeMCComponent("TTJets_LO_HT1200to2500", "/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 0.12*831.76/502.2)
TTJets_LO_HT1200to2500_ext = kreator.makeMCComponent("TTJets_LO_HT1200to2500_ext", "/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root", 0.12*831.76/502.2)
# NOTAVAILYET # TTJets_LO_HT2500toInf      = kreator.makeMCComponent("TTJets_LO_HT2500toInf", "/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 0.001430*831.76/502.2)
TTJets_LO_HT2500toInf_ext  = kreator.makeMCComponent("TTJets_LO_HT2500toInf_ext", "/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM",  "CMS", ".*root", 0.001430*831.76/502.2)


TTs = [
#TTJets,
# NOTAVAILYET # TTJets_reHLT,
#TTJets_ext,
#TTJets_LO,
#TT_pow_ext3,
# NOTAVAILYET # TT_pow_ext4,
#TT_pow,
TTJets_SingleLeptonFromTbar,
TTJets_SingleLeptonFromTbar_ext,
TTJets_SingleLeptonFromT,
TTJets_SingleLeptonFromT_ext,
TTJets_DiLepton,
TTJets_DiLepton_ext,
TTLep_pow,
# NOTAVAILYET # TTLep_pow_ext,
TTSemiLep_pow,
# NOTAVAILYET # TTJets_LO_HT600to800,
TTJets_LO_HT600to800_ext,
# NOTAVAILYET # TTJets_LO_HT800to1200,
TTJets_LO_HT800to1200_ext,
# NOTAVAILYET # TTJets_LO_HT1200to2500,
TTJets_LO_HT1200to2500_ext,
# NOTAVAILYET # TTJets_LO_HT2500toInf
TTJets_LO_HT2500toInf_ext
]

# Single top cross sections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
# NOTAVAILYET # TToLeptons_tch_amcatnlo = kreator.makeMCComponent("TToLeptons_tch_amcatnlo", "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root", (136.05+80.97)*0.108*3)
#TToLeptons_tch_amcatnlo_ext = kreator.makeMCComponent("TToLeptons_tch_amcatnlo_ext", "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v1/MINIAODSIM", "CMS", ".*root", (136.05+80.97)*0.108*3) 
# NOTAVAILYET # TToLeptons_tch_powheg = kreator.makeMCComponent("TToLeptons_tch_powheg", "/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", (136.02)*0.108*3)
# NOTAVAILYET # TBarToLeptons_tch_powheg = kreator.makeMCComponent("TBarToLeptons_tch_powheg", "/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 80.95*0.108*3)

# NOTAVAILYET V3#TToLeptons_sch_amcatnlo = kreator.makeMCComponent("TToLeptons_sch_amcatnlo", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", (7.20+4.16)*0.108*3)
# NOTAVAILYET V3#T_sch_amcatnlo = kreator.makeMCComponent("T_sch_amcatnlo", "/ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", (7.20+4.16))

T_tch_powheg = kreator.makeMCComponent("T_tch_powheg", "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root", 136.02) # inclusive sample
TBar_tch_powheg = kreator.makeMCComponent("TBar_tch_powheg", "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root", 80.95) # inclusive sample

TBar_tWch_noFullyHad_ext = kreator.makeMCComponent("TBar_tWch_noFullyHad_ext", "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",19.55)
# not there YET TBar_tWch_noFullyHad      = kreator.makeMCComponent("TBar_tWch_noFullyHad"     , "/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",19.55)
TBar_tWch = kreator.makeMCComponent("TBar_tWch", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root",35.6)
TBar_tWch_ext = kreator.makeMCComponent("TBar_tWch_ext", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", "CMS", ".*root",35.6)


T_tWch_noFullyHad_ext = kreator.makeMCComponent("T_tWch_noFullyHad_ext", "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",19.55)
#T_tWch_noFullyHad      = kreator.makeMCComponent("T_tWch_noFullyHad"     , "/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",19.55)
T_tWch_ext= kreator.makeMCComponent("T_tWch_ext", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", "CMS", ".*root",35.6)
T_tWch= kreator.makeMCComponent("T_tWch", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root",35.6)


#TGJets = kreator.makeMCComponent("TGJets", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.967)
#TGJets_ext = kreator.makeMCComponent("TGJets_ext", "/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.967)
tZq_ll_ext = kreator.makeMCComponent("tZq_ll_ext", "/tZq_ll_4f_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", "CMS", ".*root", 0.0758 )
#tZq_nunu = kreator.makeMCComponent("tZq_nunu", "/tZq_nunu_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 0.1379 )
#tWll = kreator.makeMCComponent("tWll", "/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.01123)
#tWnunu = kreator.makeMCComponent("tWnunu", "/ST_tWnunu_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.01123*1.9822 )

SingleTop = [
# NOTAVAILYET # TToLeptons_tch_amcatnlo,
#TBarToLeptons_tch_amcatnlo,
#TToLeptons_tch_amcatnlo_ext,
# NOTAVAILYET # TToLeptons_tch_powheg,
# NOTAVAILYET # TBarToLeptons_tch_powheg,
#TToLeptons_sch_amcatnlo,
#T_sch_amcatnlo,
TBar_tWch_noFullyHad_ext,
#TBar_tWch_noFullyHad,
TBar_tWch,
T_tWch,
T_tWch_noFullyHad_ext,
#T_tWch_noFullyHad,
T_tch_powheg,
TBar_tch_powheg,
TBar_tWch_ext,
T_tWch_ext,
#TGJets,
#TGJets_ext,
tZq_ll_ext,
#tZq_nunu,
#tWll,
#tWnunu
]


# DY HT bins:
#https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#DY_Z














#DYJetsToLL_M50_HT70to100      =   kreator.makeMCComponent("DYJetsToLL_M50_HT70to100"    , '/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'        ,    "CMS", ".*root", 170.4 *1.23)
DYJetsToLL_M50_HT100to200_ext =   kreator.makeMCComponent("DYJetsToLL_M50_HT100to200", "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"             , "CMS", ".*root", 147.4*1.23)
DYJetsToLL_M50_HT100to200     =   kreator.makeMCComponent("DYJetsToLL_M50_HT100to200_ext", "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",     "CMS", ".*root", 147.4*1.23)
DYJetsToLL_M50_HT200to400     =   kreator.makeMCComponent("DYJetsToLL_M50_HT200to400", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"             , "CMS", ".*root",40.99*1.23)
DYJetsToLL_M50_HT200to400_ext =   kreator.makeMCComponent("DYJetsToLL_M50_HT200to400_ext", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    , "CMS", ".*root",40.99*1.23)
DYJetsToLL_M50_HT400to600     =   kreator.makeMCComponent("DYJetsToLL_M50_HT400to600", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"             , "CMS", ".*root",5.678*1.23)
DYJetsToLL_M50_HT400to600_ext =   kreator.makeMCComponent("DYJetsToLL_M50_HT400to600_ext", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM"    , "CMS", ".*root",5.678*1.23)
# NOTAVAILYET # DYJetsToLL_M50_HT600toInf = kreator.makeMCComponent("DYJetsToLL_M50_HT600toInf", "/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root",2.198*1.23)
# NOTAVAILYET # DYJetsToLL_M50_HT600toInf_ext = kreator.makeMCComponent("DYJetsToLL_M50_HT600toInf_ext", "/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM", "CMS", ".*root",2.198*1.23)
DYJetsToLL_M50_HT600to800     =   kreator.makeMCComponent("DYJetsToLL_M50_HT600to800"   , '/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',           "CMS", ".*root", 1.367*1.23 )
DYJetsToLL_M50_HT800to1200    =   kreator.makeMCComponent("DYJetsToLL_M50_HT800to1200"  , '/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',          "CMS", ".*root", 0.6304*1.23 )
DYJetsToLL_M50_HT1200to2500   =   kreator.makeMCComponent("DYJetsToLL_M50_HT1200to2500" , '/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',         "CMS", ".*root", 0.1514*1.23 )
DYJetsToLL_M50_HT2500toInf    =   kreator.makeMCComponent("DYJetsToLL_M50_HT2500toInf"  , '/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',          "CMS", ".*root", 0.003565*1.23 )


DYJetsM50HT = [
#DYJetsToLL_M50_HT70to100   , 
DYJetsToLL_M50_HT100to200,
DYJetsToLL_M50_HT100to200_ext,
DYJetsToLL_M50_HT200to400,
DYJetsToLL_M50_HT200to400_ext,
DYJetsToLL_M50_HT400to600,
DYJetsToLL_M50_HT400to600_ext,
# NOTAVAILYET # DYJetsToLL_M50_HT600toInf,
# NOTAVAILYET # DYJetsToLL_M50_HT600toInf_ext,
DYJetsToLL_M50_HT600to800  ,
DYJetsToLL_M50_HT800to1200 ,
DYJetsToLL_M50_HT1200to2500,
DYJetsToLL_M50_HT2500toInf ,

]

# DYJets high mass
# Note: The following is really only tau tau
#DYJetsToTauTau_M150_LO = kreator.makeMCComponent("DYJetsToTauTau_M150_LO", "/DYJetsToLL_M-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 6.7)

### W+jets
#WJetsToLNu_HT70to100 = kreator.makeMCComponent("WJetsToLNu_HT70to100", "/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",1319*1.21)
WJetsToLNu_HT100to200 = kreator.makeMCComponent("WJetsToLNu_HT100to200", "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",1345*1.21)
#WJetsToLNu_HT100to200_ext = kreator.makeMCComponent("WJetsToLNu_HT100to200_ext", "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root",1345*1.21)
#WJetsToLNu_HT100to200_ext2 = kreator.makeMCComponent("WJetsToLNu_HT100to200_ext2", "/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root",1345*1.21)
WJetsToLNu_HT200to400 = kreator.makeMCComponent("WJetsToLNu_HT200to400", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",359.7*1.21)
WJetsToLNu_HT200to400_ext = kreator.makeMCComponent("WJetsToLNu_HT200to400_ext", "/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",359.7*1.21)
WJetsToLNu_HT200to400_ext2 = kreator.makeMCComponent("WJetsToLNu_HT200to400_ext2", '/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM' , "CMS", ".*root",359.7*1.21)
WJetsToLNu_HT400to600      = kreator.makeMCComponent("WJetsToLNu_HT400to600", "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",48.91*1.21)
WJetsToLNu_HT400to600_ext  = kreator.makeMCComponent("WJetsToLNu_HT400to600_ext", "/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",48.91*1.21)

WJetsToLNu_HT600to800      = kreator.makeMCComponent("WJetsToLNu_HT600to800",     "/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",12.05*1.21)
WJetsToLNu_HT600to800_ext  = kreator.makeMCComponent("WJetsToLNu_HT600to800_ext", '/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM', "CMS", ".*root",12.05*1.21)

WJetsToLNu_HT800to1200     = kreator.makeMCComponent("WJetsToLNu_HT800to1200",    "/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",5.501*1.21)
WJetsToLNu_HT800to1200_ext = kreator.makeMCComponent("WJetsToLNu_HT800to1200_ext","/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",5.501*1.21)

WJetsToLNu_HT1200to2500    = kreator.makeMCComponent("WJetsToLNu_HT1200to2500",   "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",1.329*1.21)
WJetsToLNu_HT1200to2500_ext = kreator.makeMCComponent("WJetsToLNu_HT1200to2500_ext", "/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",1.329*1.21)

WJetsToLNu_HT2500toInf = kreator.makeMCComponent("WJetsToLNu_HT2500toInf", "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",0.03216*1.21)
WJetsToLNu_HT2500toInf_ext = kreator.makeMCComponent("WJetsToLNu_HT2500toInf_ext", "/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",0.03216*1.21)

WJetsToLNuHT = [
#WJetsToLNu_HT70to100,
WJetsToLNu_HT100to200,
#WJetsToLNu_HT100to200_ext,
#WJetsToLNu_HT100to200_ext2,
WJetsToLNu_HT200to400,
WJetsToLNu_HT200to400_ext,
WJetsToLNu_HT200to400_ext2,
WJetsToLNu_HT400to600,
WJetsToLNu_HT400to600_ext,
WJetsToLNu_HT600to800,
WJetsToLNu_HT600to800_ext,
WJetsToLNu_HT800to1200,
WJetsToLNu_HT800to1200_ext,
WJetsToLNu_HT1200to2500,
WJetsToLNu_HT1200to2500_ext,
WJetsToLNu_HT2500toInf,
WJetsToLNu_HT2500toInf_ext
]












### QCD
# QCD HT bins (cross sections from McM)
#QCD_HT100to200 = kreator.makeMCComponent("QCD_HT100to200", "/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.785*10**7)
QCD_HT200to300 = kreator.makeMCComponent("QCD_HT200to300", "/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",1717000)
QCD_HT200to300_ext = kreator.makeMCComponent("QCD_HT200to300_ext", "/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",1717000)

QCD_HT300to500 = kreator.makeMCComponent("QCD_HT300to500", "/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",351300)
QCD_HT300to500_ext = kreator.makeMCComponent("QCD_HT300to500_ext", "/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",351300)

QCD_HT500to700 = kreator.makeMCComponent("QCD_HT500to700", "/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",31630)
QCD_HT500to700_ext = kreator.makeMCComponent("QCD_HT500to700_ext", "/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",31630)

QCD_HT700to1000 = kreator.makeMCComponent("QCD_HT700to1000", "/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",6802)
#QCD_HT700to1000_ext = kreator.makeMCComponent("QCD_HT700to1000_ext", "/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root",6802)

QCD_HT1000to1500 = kreator.makeMCComponent("QCD_HT1000to1500", "/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",1206)
QCD_HT1000to1500_ext = kreator.makeMCComponent("QCD_HT1000to1500_ext", "/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",1206)

QCD_HT1500to2000 = kreator.makeMCComponent("QCD_HT1500to2000", "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",120.4)
QCD_HT1500to2000_ext = kreator.makeMCComponent("QCD_HT1500to2000_ext", "/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",120.4)

QCD_HT2000toInf = kreator.makeMCComponent("QCD_HT2000toInf", "/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",25.25)
QCD_HT2000toInf_ext = kreator.makeMCComponent("QCD_HT2000toInf_ext", "/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",25.25)


QCDHT = [
#QCD_HT100to200,
QCD_HT200to300,
QCD_HT200to300_ext,
QCD_HT300to500,
QCD_HT300to500_ext,
QCD_HT500to700,
QCD_HT500to700_ext,
QCD_HT700to1000,
#QCD_HT700to1000_ext,
QCD_HT1000to1500,
QCD_HT1000to1500_ext,
QCD_HT1500to2000,
QCD_HT1500to2000_ext,
QCD_HT2000toInf,
QCD_HT2000toInf_ext
]

### DiBosons

# cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson

# NOT YET WWTo2L2Nu = kreator.makeMCComponent("WWTo2L2Nu", "/WWTo2L2Nu_13TeV-powheg-CUETP8M1Down/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root", 10.481 )
# NOT YET WWToLNuQQ = kreator.makeMCComponent("WWToLNuQQ", "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", "CMS", ".*root", 43.53 )
# NOT YET WWToLNuQQ_ext = kreator.makeMCComponent("WWToLNuQQ_ext", "/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 43.53 )
WWTo1L1Nu2Q = kreator.makeMCComponent("WWTo1L1Nu2Q", "/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 49.997 )

#NOT YET Valid ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root", 0.564)
ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 0.564)

ZZTo2L2Q = kreator.makeMCComponent("ZZTo2L2Q", "/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",  3.28)
ZZTo2Q2Nu = kreator.makeMCComponent("ZZTo2Q2Nu", "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",  4.04)
ZZTo4L = kreator.makeMCComponent("ZZTo4L", "/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM", "CMS", ".*root", 1.256)

#ZZTo4L_amcatnlo = kreator.makeMCComponent("ZZTo4L_amcatnlo", "/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 1.212)

WZTo1L3Nu   = kreator.makeMCComponent("WZTo1L3Nu"  , "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"  , "CMS", ".*root", (47.13)*(3*0.108)*(0.2) )
WZTo1L1Nu2Q = kreator.makeMCComponent("WZTo1L1Nu2Q", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",  10.71)
WZTo2L2Q    = kreator.makeMCComponent("WZTo2L2Q"   , "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"   , "CMS", ".*root",  5.60)
WZTo3LNu    = kreator.makeMCComponent("WZTo3LNu"   , "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM", "CMS", ".*root", 4.42965)

WZTo3LNu_amcatnlo = kreator.makeMCComponent("WZTo3LNu_amcatnlo", "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 4.666)

VVTo2L2Nu = kreator.makeMCComponent("VVTo2L2Nu","/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root",  11.95)
VVTo2L2Nu_ext = kreator.makeMCComponent("VVTo2L2Nu_ext" ,"/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM", "CMS", ".*root",  11.95)

DiBosons = [
#WWTo2L2Nu,
#WWToLNuQQ,
#WWToLNuQQ_ext,
WWTo1L1Nu2Q,
ZZTo2L2Nu,
ZZTo2L2Q,
ZZTo2Q2Nu,
ZZTo4L,
#ZZTo4L_amcatnlo,
WZTo1L3Nu,
WZTo1L1Nu2Q,
WZTo2L2Q,
WZTo3LNu,
WZTo3LNu_amcatnlo,
VVTo2L2Nu,
VVTo2L2Nu_ext
]

### TTV
TTWToLNu_ext = kreator.makeMCComponent("TTWToLNu_ext", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", "CMS", ".*root", 0.2043)
TTWToQQ = kreator.makeMCComponent("TTWToQQ", "/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 0.40620)

TTZToQQ = kreator.makeMCComponent("TTZToQQ","/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", "CMS", ".*root", 0.5297)
TTZToLLNuNu_ext     = kreator.makeMCComponent("TTZToLLNuNu_ext", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM", "CMS", ".*root", 0.2529)
TTZToLLNuNu_ext2    = kreator.makeMCComponent("TTZToLLNuNu_ext2", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM", "CMS", ".*root", 0.2529)

#TTZToLLNuNu_m1to10  = kreator.makeMCComponent("TTZToLLNuNu_m1to10","/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.0493)
# https://twiki.cern.ch/twiki/bin/view/CMS/SameSignDilepton2016
#TTZ_LO = kreator.makeMCComponent("TTZ_LO", "/ttZJets_13TeV_madgraphMLM/RunIISummer16MiniAODv2-80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",  0.5297/0.692)
#TTGJets     = kreator.makeMCComponent("TTGJets",    "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.697)
#TTGJets_ext = kreator.makeMCComponent("TTGJets_ext","/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.697)

TTV = [
TTWToLNu_ext,
TTWToQQ,
TTZToQQ,
TTZToLLNuNu_ext,
TTZToLLNuNu_ext2,
#TTZToLLNuNu_m1to10,
#TTGJets,
#TTGJets_ext
]


### ----------------------------- summary ----------------------------------------

mcSamples = TTs + SingleTop  + DYJetsM50HT  + WJetsToLNuHT + QCDHT +  DiBosons + TTV # + [TChiSlepSnu,T1tttt_2016,T5qqqqVV_2016]

samples = mcSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples,localobjs=locals())
