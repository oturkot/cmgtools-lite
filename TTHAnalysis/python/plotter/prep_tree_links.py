#!/usr/bin/env python

#####     author : Oleksii Turkot          #####
#####  institute : DESY                    #####
#####      email : oleksii.turkot@desy.de  #####
#####       date : April 2019              #####

import sys
import os

import argparse
import json

treeDir = 'treeProducerSusySingleLepton'
scriptDir = os.path.dirname(os.path.realpath(__file__)) + '/'

parser = argparse.ArgumentParser(description="Checks the root files of samples trees and friend trees")
parser.add_argument("-mc",    "--mc", nargs='+', help='<Required> List of MC directories', required=True)
parser.add_argument("-d",   "--data", nargs='+', help='<Required> List of Data directories', required=True)
parser.add_argument("-s", "--signal", nargs='+', help='<Required> List of Signal directories', required=True)
parser.add_argument("-f", "--friend", action="store_true", help="Prepare trees or friend trees links")
parser.add_argument("-y",   "--year", type=int, choices=[2016, 16, 2017, 17], default=2016, 
                    help="Year of the samples campaign")
args = parser.parse_args()

if (args.year == 16 or args.year == 2016): 
    sam_year = "2016"
elif (args.year == 17 or args.year == 2017):
    sam_year = "2017"

with open(scriptDir + '../../../SUSYAnalysis/macros/samples.json') as json_file:  
    Samples = json.load(json_file)

outDir = scriptDir
if (args.friend):
    outDir += 'friends/'
else:
    outDir += 'trees/'

# make empty output directory
if  os.path.exists(outDir):
    os.system('rm -rf ' + outDir)
os.mkdir(outDir)

inDirs = {}
inDirs["MC"]     = args.mc
inDirs["Data"]   = args.data
inDirs["Signal"] = args.signal

for sam_type in ["MC", "Data", "Signal"] :
    
    for i, sam_dir in enumerate(inDirs[sam_type]):
        if sam_dir[0] != '/':
            inDirs[sam_type][i] = scriptDir + inDirs[sam_type][i]
    
    for samp in Samples[sam_year][sam_type] :
        
        if (args.friend):
            samp = 'evVarFriend_' + samp + '.root'
        
        for sam_dir in inDirs[sam_type] :
            
            if os.path.exists(sam_dir + '/' + samp) :
                os.system('ln -s ' + sam_dir + '/' + samp + ' ' + outDir + samp)
                break
            
        else:
            print "WARNING: Did not find the " + sam_type + " sample " + samp
    













