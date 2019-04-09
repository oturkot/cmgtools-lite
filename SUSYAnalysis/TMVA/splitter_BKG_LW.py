#!/usr/bin/env python
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
import sys
import os

TreeName="sf/t"

import argparse
import json

jsonLocation=os.path.dirname(os.path.realpath(__file__)) + '/../macros/samples.json'

#parser = argparse.ArgumentParser(description="Split the MC trees (and optionaly friend trees) for BDT training and evaluation")
parser = argparse.ArgumentParser(description="Split the MC friend trees for BDT training")
parser.add_argument("friend_dir", help="Directory with the friend trees")
parser.add_argument("-y", "--year", type=int, choices=[2016, 16, 2017, 17], default=2016, 
                    help="Year of the samples campaign")
args = parser.parse_args()

if (args.year == 16 or args.year == 2016): 
    sam_year = "2016"
elif (args.year == 17 or args.year == 2017):
    sam_year = "2017"
    
with open(jsonLocation) as json_file:  
    Samples = json.load(json_file)
    
filelist = []
for samp in Samples[sam_year]["MC"] :
    filelist.append('evVarFriend_' + samp + '.root')

# make empty output directories
if (os.path.isdir('Training')):
    os.system('rm -rf Training/')
if (os.path.isdir('Evaluation')):
    os.system('rm -rf Evaluation/')
os.mkdir('Training/')
os.mkdir('Evaluation/')

print 'Filelist length = ', len(filelist)

filemiss = []
for f in filelist :
    if not os.path.isfile(args.friend_dir+"/"+f):
        filemiss.append(f)

if len(filemiss) != 0:
    print 'ERROR ! Missing friend trees files:'
    for fm in filemiss:
        print '      ', fm
else:
    for f in filelist :
        FTrain = ROOT.TFile('Training/'+f, 'RECREATE' )
        FEval = ROOT.TFile( 'Evaluation/'+f, 'RECREATE' )
        file0 = ROOT.TFile.Open(args.friend_dir+"/"+f)
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

