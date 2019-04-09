#!/usr/bin/env python
import sys,os

from math import *
from ROOT import *

#def dumpCounts(tree,cname = "counts.txt", grandTotEvents = 0):
def dumpCounts(tree,cname = "counts.txt"):

    hCounts = TH2F("hCounts","Mass scan",1000,1,2001,1000,-1,2001)
    hWeights = TH2F("hWeights","Mass scan",1000,1,2001,1000,-1,2001)

    #var = "mLSP:mGo" # for friend tree
    var = "GenSusyMNeutralino:GenSusyMGluino" # for cmg tuple

    tree.Draw(var + '>>' + hCounts.GetName(),"","goff")
    tree.Draw(var + '>>' + hWeights.GetName(),"genWeight","goff")
    
#    if (grandTotEvents == 0):
    totalEvts = hCounts.GetEntries()
    print 'Total produced events:', totalEvts
#    else:
#        totalEvts = grandTotEvents

    cntDict = {}

    # round up to 5
    base = 5

    for xbin in range(1,hCounts.GetNbinsX()+1):
        for ybin in range(1,hCounts.GetNbinsY()+1):

            cnt = hCounts.GetBinContent(xbin,ybin)
            if cnt == 0: continue

            wgt = hWeights.GetBinContent(xbin,ybin)

            mGo = hCounts.GetXaxis().GetBinCenter(xbin)
            #mGo = hCounts.GetXaxis().GetBinLowEdge(xbin)
            mLSP = hCounts.GetYaxis().GetBinCenter(ybin)
            #mLSP = hCounts.GetYaxis().GetBinLowEdge(ybin)

            # round up to base (5)
            mGo = int(base * round(mGo/base))
            mLSP = int(base * round(mLSP/base))

            #print "Found %i entries for mass point %i,%i" %(cnt, mGo,mLSP)
            cntDict[(mGo,mLSP)] = (cnt,wgt)

    # write file
    with open(cname,"a") as cfile:

        #cfile.write("Total\t" + str(totalEvts) + "\n")
        cfile.write("#mGo\tmLSP\tTotal\tTotGenW\tCountsSMS\tGenWeightSMS\n")

        for point in cntDict:

            #write only count for each point
            #line = "%i\t%i\t%i\n" %(point[0],point[1],cntDict[point])

            # write count, weight and total for each point
            line = "%i\t%i\t%i\t%i\t%i\t%.3f\n" %(point[0],point[1],totalEvts,totalEvts,cntDict[point][0],cntDict[point][1])

            cfile.write(line)

    #raw_input("exit")
    
    
def dumpCounts_LWt03 (tree, cntDict = None, grandTotEvents = 0):
    
    hCounts = TH2F("hCounts","Mass scan",1000,1,2001,1000,-1,2001)
    hWeights = TH2F("hWeights","Mass scan",1000,1,2001,1000,-1,2001)

    #var = "mLSP:mGo" # for friend tree
    var = "GenSusyMNeutralino:GenSusyMGluino" # for cmg tuple

    tree.Draw(var + '>>' + hCounts.GetName(),"","goff")
    tree.Draw(var + '>>' + hWeights.GetName(),"genWeight","goff")
    
    totalEvts = hCounts.GetEntries()
    print 'Total produced events:', totalEvts
    grandTotEvents += totalEvts

    # round up to 5
    base = 5

    for xbin in range(1,hCounts.GetNbinsX()+1):
        for ybin in range(1,hCounts.GetNbinsY()+1):

            cnt = hCounts.GetBinContent(xbin,ybin)
            if cnt == 0: continue

            wgt = hWeights.GetBinContent(xbin,ybin)

            mGo = hCounts.GetXaxis().GetBinCenter(xbin)
            mLSP = hCounts.GetYaxis().GetBinCenter(ybin)

            mGo = int(base * round(mGo/base))
            mLSP = int(base * round(mLSP/base))
            
            if (mGo,mLSP) in cntDict:
                cntDict[(mGo,mLSP)] += (cnt,wgt)
            else:
                cntDict[(mGo,mLSP)] = (cnt,wgt)
    
    return cntDict, grandTotEvents


def writeCounts_LWt03 (cntDict, grandTotEvents, cname = "counts.txt"):
    
    with open(cname,"a") as cfile:

        #cfile.write("Total\t" + str(totalEvts) + "\n")
        cfile.write("#mGo\tmLSP\tTotal\tTotGenW\tCountsSMS\tGenWeightSMS\n")

        for point in cntDict:
            # write count, weight and total for each point
            line = "%i\t%i\t%i\t%i\t%i\t%.3f\n" %(point[0],point[1],grandTotEvents,grandTotEvents,cntDict[point][0],cntDict[point][1])

            cfile.write(line)


def dumpTree_LWt03 (fileName, cntDict = None, grandTotEvents = 0):
    tfile  = TFile(fileName, "READ")

    if not tfile:
        print "Couldn't open the file"
        exit(0)
        
    tree = tfile.Get('tree')

    cntDict, grandTotEvents = dumpCounts_LWt03(tree, cntDict, grandTotEvents)

    tfile.Close()
    
    return cntDict, grandTotEvents


#def dumpTree(fileName, cname = "counts.txt", grandTotEvents = 0):
def dumpTree(fileName, cname = "counts.txt"):
    tfile  = TFile(fileName, "READ")

    if not tfile:
        print "Couldn't open the file"
        exit(0)

    ## Get tree from file
    # for friend trees
    #tree = tfile.Get('sf/t')
    # for cmg trees
    tree = tfile.Get('tree')

#    dumpCounts(tree,cname,grandTotEvents)
    dumpCounts(tree,cname)

    tfile.Close()


def dumpTrees(fileList):

    cname = "counts_T1tttt_2016_LWt03.txt"

    # overwrite file
    cf = open(cname,"w"); cf.close()
    
##    # Merge the trees from the fileList
##    treelist = TList()
##    for i,fname in enumerate(fileList):
##        tfile  = TFile(fname, "READ")
##        if not tfile:
##            print "Couldn't open the file ", fname
##            exit(0)
##        tree = tfile.Get('tree')
##        treelist.Add(tree)
##    
##    newtree = TTree.MergeTrees(treelist)
        
##    dumpCounts(newtree,cname)
    
#    #count the total number of events in all files:
#    grandTotEvents = 0
#    for i,fname in enumerate(fileList):
#        tfile  = TFile(fname, "READ")
#        if not tfile:
#            print "Couldn't open the file ", fname
#            exit(0)
#        tree = tfile.Get('tree')
#        grandTotEvents += tree.GetEntries()
#    
#    print 'Total produced events:', grandTotEvents
    
    cntDict = {}
    grandTotEvents = 0
    
    for i,fname in enumerate(fileList):
        mass = fname

        parts = fname.split("/")
        for part in parts:
            if "mGo" in part and "mLSP" in part: mass = part

        #print "Counts for", os.path.basename(fname)
        print "Counts for", mass, "[%i/%i]" %(i+1,len(fileList))
##        dumpTree(fname,cname,grandTotEvents)
#        dumpTree(fname,cname)
        cntDict, grandTotEvents = dumpTree_LWt03 (fname, cntDict, grandTotEvents)
        print 80 *"-"
        
    writeCounts_LWt03 (cntDict, grandTotEvents, cname)
    

def dumpChain(fileList):

    #ch = TChain("sf/t")
    ch = TChain("tree")

    for f in fileList:
        ch.Add(f)

    print "Got %i files" % len(fileList),
    print "with %i events" % ch.GetEntries()

    dumpCounts(ch)

if __name__ == "__main__":

    if '-b' in sys.argv:
        sys.argv.remove('-b')

    if len(sys.argv) > 1:
        fileList = sys.argv[1:]
        #print '#fileName is', fileName
    else:
        print '#No file names given'
        exit(0)

    #dumpChain(fileList)
    dumpTrees(fileList)

    print 'Finished'
