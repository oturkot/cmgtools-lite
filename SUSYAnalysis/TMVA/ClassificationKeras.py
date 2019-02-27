#!/usr/bin/env python

from ROOT import TMVA, TFile, TTree, TCut
from subprocess import call
from os.path import isfile

from keras.utils import plot_model

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.regularizers import l2
from keras import initializers
from keras.optimizers import Adam, SGD
from os import environ
environ['KERAS_BACKEND'] = 'tensorflow'

import os
import sys
path = sys.argv[-1]

# function for getting all the root files inside directory 
def find_all_matching(substring, path):
    result = []
    for root, dirs, files in os.walk(path):
        for thisfile in files:
            if substring in thisfile:
                result.append(os.path.join(root, thisfile ))
    return result

#### variables to train with 
variables =["Lep_pdgId","Lep_pt","Lep_eta","Lep_phi","Lep_relIso","Lep_miniIso","Lep2_pt","MET","MT","dPhi","LT","HT","nJets","nBJet","Jet1_pt","Jet2_pt","nBJetDeep","FatJet1_pt","FatJet2_pt","FatJet1_eta","FatJet2_eta","FatJet1_phi","FatJet2_phi","FatJet1_mass","FatJet2_mass","nDeepTop_loose","nDeepTop_medium","nDeepTop_tight"]
#variables =["Lep_pt","Lep2_pt","MET","MT","dPhi","HT","nJets","nBJet","Jet1_pt","Jet2_pt"]
numVariables = len(variables)

# Setup TMVA
TMVA.Tools.Instance()
TMVA.PyMethodBase.PyInitialize()

# output file 
output = TFile.Open('TMVA.root', 'RECREATE')
# TMVA factory 
factory = TMVA.Factory('TMVAClassification', output,
                       '!V:!Silent:Color:DrawProgressBar:Transformations=I:AnalysisType=Classification')
# Load data
# background files
bkg_files = find_all_matching('.root',path)
# signal files 
Signal1_in = TFile.Open('SMS_T1tttt_1750_1000_fr/evVarFriend_SMS_T1tttt_1750_1000.root')
Signal2_in = TFile.Open('Friends_for_MVA/training/evVarFriend_T1tttt_MiniAOD_15_10.root')

# intiate the dataloader
dataloader = TMVA.DataLoader('dataset')
# signal tree name
signal1 = Signal1_in.Get('sf/t')
signal2 = Signal2_in.Get('sf/t')

# get the list of branches ---> corresponding to the variable names mentioned above 
for branch in signal1.GetListOfBranches():
	if branch.GetName() in variables: 
		dataloader.AddVariable(branch.GetName())

# preselections 
sigCuts = TCut("nLep == 1 && Lep_pt > 25 && Selected == 1 &&  nVeto == 0 && nJets30Clean >= 3 && Jet2_pt > 80 &&  HT > 500 && LT > 250")
bkgCuts = TCut("nLep == 1 && Lep_pt > 25 && Selected == 1 &&  nVeto == 0 && nJets30Clean >= 3 && Jet2_pt > 80 &&  HT > 500 && LT > 250")

# load the signal tree 
dataloader.AddSignalTree(signal1, 1.0)
dataloader.AddSignalTree(signal2, 1.0)

# load the BKG tree 
names = []
for f in bkg_files : 
	if "T1tttt_" in f : continue
	name = f.split('/')[-1].replace("evVarFriend_","").replace(".root","")
	names.append(name)
	vars()[name] = TFile.Open(str(f))
	background = vars()[name].Get('sf/t')
	dataloader.AddBackgroundTree(background, 1.0)

# weight expressions for sig. and bkg
dataloader.SetBackgroundWeightExpression('Xsec')
dataloader.SetSignalWeightExpression('susyXsec')
dataloader.PrepareTrainingAndTestTree(sigCuts,
                                      'nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V')

# Generate model
# Define model
#model = Sequential()
# input layer
#model.add(Dense(256, kernel_initializer='uniform', activation='relu', input_dim=numVariables))
#model.add(Dense(256, kernel_initializer='uniform', activation='relu'))
#model.add(Dense(256, kernel_initializer='uniform', activation='relu'))
#model.add(Dense(2, kernel_initializer='uniform', activation='sigmoid'))
 
 # Set loss and optimizer
#model.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy',])

# Store model to file
#model.save('model.h5')
#model.summary()
#plot_model(model, to_file='model.png')

# Book methods
#factory.BookMethod(dataloader, TMVA.Types.kFisher, 'Fisher',
#                   '!H:!V:Fisher:VarTransform=D,G')
#factory.BookMethod(dataloader, TMVA.Types.kPyKeras, 'PyKeras',
#                   'H:!V:VarTransform=D,G:FilenameModel=model.h5:NumEpochs=10:BatchSize=32:Tensorboard=./logs',)
factory.BookMethod( dataloader,  TMVA.Types.kBDT, "BDT",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" )

# Run training, test and evaluation
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
