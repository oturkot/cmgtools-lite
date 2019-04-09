#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
import sys
import os
path = sys.argv[-1]
TreeName="sf/t"

filelist=['evVarFriend_DYJetsToLL_M50_HT100to200_ext.root','evVarFriend_QCD_HT300to500.root','evVarFriend_TBar_tWch_noFullyHad_ext.root',
          'evVarFriend_WJetsToLNu_HT100to200.root','evVarFriend_DYJetsToLL_M50_HT100to200.root','evVarFriend_QCD_HT500to700_ext.root',
          'evVarFriend_TBar_tWch.root','evVarFriend_WJetsToLNu_HT1200to2500_ext.root','evVarFriend_DYJetsToLL_M50_HT1200to2500.root',
          'evVarFriend_QCD_HT500to700.root','evVarFriend_T_tch_powheg.root','evVarFriend_WJetsToLNu_HT1200to2500.root',
          'evVarFriend_DYJetsToLL_M50_HT200to400_ext.root','evVarFriend_QCD_HT700to1000.root','evVarFriend_TTJets_DiLepton_ext.root',
          'evVarFriend_WJetsToLNu_HT200to400_ext2.root','evVarFriend_DYJetsToLL_M50_HT200to400.root','evVarFriend_TTJets_DiLepton.root',
          'evVarFriend_WJetsToLNu_HT200to400_ext.root','evVarFriend_DYJetsToLL_M50_HT2500toInf.root','evVarFriend_TTJets_LO_HT1200to2500_ext.root',
          'evVarFriend_WJetsToLNu_HT200to400.root','evVarFriend_DYJetsToLL_M50_HT400to600_ext.root','evVarFriend_TTJets_LO_HT2500toInf_ext.root',
          'evVarFriend_WJetsToLNu_HT2500toInf_ext.root','evVarFriend_DYJetsToLL_M50_HT400to600.root','evVarFriend_TTJets_LO_HT600to800_ext.root',
          'evVarFriend_WJetsToLNu_HT2500toInf.root','evVarFriend_DYJetsToLL_M50_HT600to800.root','evVarFriend_TTJets_LO_HT800to1200_ext.root',
          'evVarFriend_WJetsToLNu_HT400to600_ext.root','evVarFriend_DYJetsToLL_M50_HT800to1200.root','evVarFriend_TTJets_SingleLeptonFromTbar_ext.root',
          'evVarFriend_WJetsToLNu_HT400to600.root','evVarFriend_TTJets_SingleLeptonFromTbar.root','evVarFriend_WJetsToLNu_HT600to800_ext.root',
          'evVarFriend_TTJets_SingleLeptonFromT_ext.root','evVarFriend_WJetsToLNu_HT600to800.root','evVarFriend_TTJets_SingleLeptonFromT.root',
          'evVarFriend_WJetsToLNu_HT800to1200_ext.root','evVarFriend_TTLep_pow.root','evVarFriend_WJetsToLNu_HT800to1200.root','evVarFriend_TTSemiLep_pow.root',
          'evVarFriend_WWTo1L1Nu2Q.root','evVarFriend_T_tWch_ext.root','evVarFriend_WZTo1L1Nu2Q.root','evVarFriend_T_tWch_noFullyHad_ext.root',
          'evVarFriend_WZTo1L3Nu.root','evVarFriend_QCD_HT1000to1500_ext.root','evVarFriend_T_tWch.root','evVarFriend_WZTo2L2Q.root',
          'evVarFriend_QCD_HT1000to1500.root','evVarFriend_TTWToLNu_ext.root','evVarFriend_WZTo3LNu_amcatnlo.root','evVarFriend_QCD_HT1500to2000_ext.root',
          'evVarFriend_TTWToQQ.root','evVarFriend_WZTo3LNu.root','evVarFriend_QCD_HT1500to2000.root','evVarFriend_TTZToLLNuNu_ext2.root',
          'evVarFriend_ZZTo2L2Nu.root','evVarFriend_QCD_HT2000toInf_ext.root','evVarFriend_TTZToLLNuNu_ext.root','evVarFriend_ZZTo2L2Q.root',
          'evVarFriend_QCD_HT2000toInf.root','evVarFriend_TTZToQQ.root','evVarFriend_ZZTo2Q2Nu.root','evVarFriend_QCD_HT200to300_ext.root',
          'evVarFriend_tZq_ll_ext.root','evVarFriend_ZZTo4L.root','evVarFriend_QCD_HT200to300.root','evVarFriend_TBar_tch_powheg.root','evVarFriend_VVTo2L2Nu_ext.root',
          'evVarFriend_QCD_HT300to500_ext.root','evVarFriend_TBar_tWch_ext.root','evVarFriend_VVTo2L2Nu.root']

for f in filelist : 
    FTrain = ROOT.TFile('Training/'+f, 'RECREATE' )
    FEval = ROOT.TFile( 'Evaluation/'+f, 'RECREATE' )
    file0 = ROOT.TFile.Open(path+"/"+f)
    t = file0.Get(TreeName)
    t.SetBranchStatus("*", 1)
    sfdirT = FTrain.mkdir('sf')
    sfdirT.cd()
    outTreeT = t.CloneTree(0)
    sfdirE = FEval.mkdir('sf')
    sfdirE.cd()
    outTreeE = t.CloneTree(0)
    print 'going to crop 20% = ', t.GetEntries() * 20 / 100,' out of : ' , t.GetEntries() , ' from this file : ', f 
    for i in range(t.GetEntries()):
        t.GetEntry(i)
        if i <= t.GetEntries() * 20 /100 : 
            outTreeT.Fill()
        elif i > t.GetEntries() * 20 /100 : 
            outTreeE.Fill()
    print ' now writting the output for' , f
    outTreeT.AutoSave()
    outTreeE.AutoSave()
    FTrain.Write()
    FEval.Write()
    FTrain.Close()
    FEval.Close()

