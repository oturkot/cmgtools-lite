#!/usr/bin/env python

#####     author : Oleksii Turkot          #####
#####  institute : DESY                    #####
#####      email : oleksii.turkot@desy.de  #####
#####       date : March 2019              #####

import sys
import os
from rootpy.io import root_open
# turn off warning and error messages:
from rootpy import log
log["/ROOT.TFile"].setLevel(log.CRITICAL)

import argparse
import json

treeDir = 'treeProducerSusySingleLepton'

parser = argparse.ArgumentParser(description="Checks the root files of samples trees and friend trees")
parser.add_argument("tree_dir", help="Directory with the merged tree samples")
parser.add_argument("friend_dir", help="Directory with the merged friend trees")
parser.add_argument("-y", "--year", type=int, choices=[2016, 16, 2017, 17], default=2016, 
                    help="Year of the samples campaign")
group = parser.add_mutually_exclusive_group()
group.add_argument("-mc", "--mc", action="store_true")
group.add_argument("-d", "--data", action="store_true")
group.add_argument("-s", "--signal", action="store_true")
args = parser.parse_args()
    
if (args.mc):
    sam_type = "MC"
elif (args.data):
    sam_type = "Data"
elif (args.signal):
    sam_type = "Signal"
else:
    sam_type = "MC"
    
if (args.year == 16 or args.year == 2016): 
    sam_year = "2016"
elif (args.year == 17 or args.year == 2017):
    sam_year = "2017"
        

print 'Checking', sam_year, sam_type, 'samples with trees stored in', args.tree_dir, 'and friend trees in', args.friend_dir

with open('samples.json') as json_file:  
    Samples = json.load(json_file)

print '    N samples = ', len(Samples[sam_year][sam_type])

tree_miss = []
friend_miss = []

for samp in Samples[sam_year][sam_type] :
    
    sttreefile = args.tree_dir + '/' + samp + '/' + treeDir + '/tree.root'
    if not os.path.isfile(sttreefile):
        tree_miss.append(samp)
    else:
        try:
            rootTMP = root_open(sttreefile)
        except Exception as e:
            print 'Could not open file: ', sttreefile
            tree_miss.append(samp)
        else:
            
            stfriendfile = args.friend_dir + '/' + 'evVarFriend_' + samp + '.root'
            if not os.path.isfile(stfriendfile):
                friend_miss.append(samp)
            else:
                try:
                    rootTMP = root_open(stfriendfile)
                except Exception as e:
                    print 'Could not open file: ', stfriendfile
                    friend_miss.append(samp)
    

if len(tree_miss) != 0:
    print '\nWARNING ! Missing tree files: \n'
    for tm in tree_miss:
        print tm
    print ''
    
if len(friend_miss) != 0:
    print '\nWARNING ! Missing friend trees: \n'
    for fm in friend_miss:
        print fm
    print ''
    
if len(tree_miss) == 0 and len(friend_miss) == 0:
    print '\n    All trees seem to be ready. \n'



