#!/usr/bin/env python

import sys, glob, os
from ROOT import *

# Get lepton SF histograms

# Electrons
f1_ele = TFile.Open('scaleFactors.root', 'read')

h1_ele = f1_ele.Get('GsfElectronToCutBasedSpring15T')
h2_ele = f1_ele.Get('MVAVLooseElectronToMini')

h12_ele = h1_ele.Clone()
h12_ele.Multiply(h2_ele)
h12_ele.SetName('El_CBtight_miniIso0p1_Moriond')
h12_ele.SetTitle('El_CBtight_miniIso0p1_Moriond')
h12_ele.SaveAs('El_CBtight_miniIso0p1_Moriond.root')

# Muons
f1_mu = TFile.Open('TnP_NUM_MediumID_DENOM_generalTracks_VAR_map_pt_eta.root', 'read')
f2_mu = TFile.Open('TnP_NUM_MiniIsoTight_DENOM_MediumID_VAR_map_pt_eta.root', 'read')
f3_mu = TFile.Open('TnP_NUM_TightIP3D_DENOM_MediumID_VAR_map_pt_eta.root', 'read')

h1_mu = f1_mu.Get('SF')
h2_mu = f2_mu.Get('SF')
h3_mu = f3_mu.Get('SF')

h123_mu = h1_mu.Clone()
h123_mu.Multiply(h2_mu)
h123_mu.Multiply(h3_mu)
h123_mu.SetName("Mu_Medium_miniIso0p2_SIP3D_Moriond")
h123_mu.SetTitle("Mu_Medium_miniIso0p2_SIP3D_Moriond")
h123_mu.SaveAs("Mu_Medium_miniIso0p2_SIP3D_Moriond.root")
