#!/usr/bin/env python
import sys
import os
path = sys.argv[-1]

rootlist = os.listdir(path)
for f in rootlist : 
	sF = f.replace(".root","").replace("evVarFriend_","")
	Stri = 'TString '+sF+'=inputFolder+'+"\""+f+"\";"
	TF = 'TFile *input_'+sF+";"
	op = "input_"+sF+"=TFile::Open("+sF+");"
	TT = "TTree *tree_"+sF+"=(TTree*)input_"+sF+"->Get(\"sf/t\");"
	DL = "dataloader->AddBackgroundTree(tree_"+sF+"		,	1);"
	print Stri
	print TF
	print op
	print TT 
	print DL
