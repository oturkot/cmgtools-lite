#!/usr/bin/env python

from ROOT import TMVA, TFile, TString,TTree
from array import array
from subprocess import call
from os.path import isfile
import os
import sys
path = "@FPATH"
# Setup TMVA
TMVA.Tools.Instance()
TMVA.PyMethodBase.PyInitialize()
reader = TMVA.Reader("Color:!Silent")

variables =["Lep_pdgId","Lep_pt","Lep_eta","Lep_phi","Lep_relIso","Lep_miniIso","Lep2_pt","MET","MT","dPhi","LT","HT","nJets","nBJet","Jet1_pt","Jet2_pt","nBJetDeep","FatJet1_pt","FatJet2_pt","FatJet1_eta","FatJet2_eta","FatJet1_phi","FatJet2_phi","FatJet1_mass","FatJet2_mass","nDeepTop_loose","nDeepTop_medium","nDeepTop_tight"]
numVariables = len(variables)
# Load data
data_in = TFile.Open(path)
tree_in = data_in.Get('sf/t')
outFname = path.split("/")[-1]
out_path = sys.argv[-1]
if not os.path.exists(out_path): 
	os.makedirs(out_path)
	
branches = {}

for branch in tree_in.GetListOfBranches():
    if not (branch.GetName() in variables): continue 
    branchName = branch.GetName()
    branches[branchName] = array('f', [-999])
    reader.AddVariable(branchName, branches[branchName])
    tree_in.SetBranchAddress(branchName, branches[branchName])

BDT = array("f", [-999])
fout = TFile(out_path+'/'+outFname,"RECREATE")
sf = fout.mkdir("sf")
sf.cd()
t = tree_in.CloneTree(0)
bran = t.Branch("BDT",BDT,"BDT/F")
#t.Branch( 'PyKeras', PyKeras ,'PyKeras/F')
# Book methods
reader.BookMVA('BDT', TString('dataset/weights/TMVAClassification_BDT.weights.xml'))
# Print some example classifications
print('Some example classifications:')
for i in range(tree_in.GetEntries()):
    tree_in.GetEntry(i)
    BDT[0] = reader.EvaluateMVA('BDT')
    bran.Fill()
    t.Fill()
t.Write()
#fout.Delete("t")
#fout.Write()
fout.Close()
