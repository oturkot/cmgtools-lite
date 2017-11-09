#!/usr/bin/env python
import sys, glob, os
inDir = sys.argv[1]
dirList = glob.glob(inDir+'/cmg*')
dirListTree = glob.glob(inDir+'/cmg*/tree*root')
dirListTree = [x.replace("/tree.root","") for x in dirListTree]
#print dirList
#print dirListTree
notree = list(set(dirList)-set(dirListTree))
for x in notree:
    print x
