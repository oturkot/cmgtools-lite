import sys,os

#from makeYieldPlots import *
import makeYieldPlots as yp

yp._batchMode = False

if __name__ == "__main__":

    #yp.CMS_lumi.lumi_13TeV = str(2.1) + " fb^{-1}"
    yp.CMS_lumi.lumi_13TeV = "MC"
    yp.CMS_lumi.extraText = "Simulation"

    ## remove '-b' option
    if '-b' in sys.argv:
        sys.argv.remove('-b')
        yp._batchMode = True

    '''
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
        print '# pattern is', pattern
    else:
        print "No pattern given!"
        exit(0)
    '''
    pattern = ""

    #BinMask LTX_HTX_NBX_NJX for canvas names
    basename = os.path.basename(pattern)
    mask = basename.replace("*","X_")

    # Define storage
    yds1 = yp.YieldStore("DilepCorrs")
    #path1 = "Yields/systs/btag/hadFlavour/fixXsec/allSF_noPU/meth1/merged/"
    #path1 = "Yields/wData/jecv7_fixSR/lumi2p25fb/unblind/allSF_noPU/meth1A/merged/"
    path1 = "Yields_DilepCorrYesNo/grid-dilep/merged/"
    yds1.addFromFiles(path1,("lep","sele"))

    yds2 = yp.YieldStore("StdWeights")
    #path2 = "Yields/systs/btag/hadFlavour/fixXsec/allSF_noPU/meth2/merged/"
    #path2 = "Yields/wData/jecv7/lumi2p25fb/unblind/allSF_noPU/meth1A/merged/"
    path2 = "Yields_DilepCorrYesNo/grid/merged/"
    yds2.addFromFiles(path2,("lep","sele"))

    sysCols = [2,4,7,8,3,9,6] + range(10,50)#[1,2,3] + range(4,10)

    # canvs and hists
    hists = []
    canvs = []

    yds1.showStats()
    yds2.showStats()

    # Samples
    #samps = ["EWK","TTJets","TTdiLep","TTsemiLep","WJets","TTV","DY","SingleT"]
    #samps = ["TTJets","WJets","TTV","DY","SingleTop"]
    #samps = ["EWK","TTJets","WJets","SingleT","DY","TTV"]
    samps = ["DY","EWK"]#,"TTJets","TTdiLep","TTsemiLep","WJets","TTV","SingleT"]

#    mass = "mGo1200_mLSP800"; massName = "(1200,800)"
#    signame = "T1tttt_Scan_" + mass
#
#    samps = [signame]

    cat = "Kappa"
    #cat = "SR_MB"

    #logY = True
    logY = False

    for samp in samps:

        print "Making plot for", samp, cat

        # 1
        yp.colorDict[samp+"_1_"+cat] = yp.kBlue
        h1 = yp.makeSampHisto(yds1,samp,cat,samp+"_1_"+cat)
        h1.SetTitle(samp+" (with dilep corr.)")

        # 2
        yp.colorDict[samp+"_2_"+cat] = yp.kRed
        h2 = yp.makeSampHisto(yds2,samp,cat,samp+"_2_"+cat)
        h2.SetTitle(samp+" (std. weights)")
        #h2.SetTitle(samp+" (only btagSF 2)")
        #h2.SetTitle(samp+" (All but PU)")
        #h2.SetTitle(samp+" (PUwgt < 4.)")
        #h2.SetTitle(samp+" (1 hadrFlav)")

        ratio = yp.getRatio(h1,h2)
        ratio.GetYaxis().SetRangeUser(0.9,1.10)
        for i in range(0,ratio.GetNbinsX()):
            print ratio.GetBinContent(i)
            ratio.SetBinError(i,0.0)

        #h1.GetYaxis().SetRangeUser(0.55,1.45)
        if "WJets" in samp and "Kappa" in cat:
            h2.GetYaxis().SetRangeUser(0.05,3.45)
            h1.GetYaxis().SetRangeUser(0.05,3.45)

        hists += [h1,h2,ratio]
        canv = yp.plotHists(cat+"_"+samp,[h1,h2],ratio,"TM", 1200, 600, logY = logY)

        canvs.append(canv)

        if not yp._batchMode:
            answ = raw_input("Enter 'q' to exit: ")
            if "q" in answ: exit(0)

    # Save canvases
    exts = [".pdf",".png"]#,".root"]
    #exts = [".pdf"]

    #odir = "BinPlots/signal/Compare/MET3TeV/allSF_noPU/" + cat + "/"
    odir = "BinPlots/background/Compare/DilepCOrr_YesNo/allSF/" + cat + "/"
    if not os.path.isdir(odir): os.makedirs(odir)

    for canv in canvs:
        for ext in exts:
            cname = odir+mask+canv.GetName()
            if logY: cname += "_log"
            canv.SaveAs(cname+ext)

