#!/usr/bin/env python
import sys
lumi = "36"
from yieldClass import *
from ROOT import *

def printLatexHeader(nCol, f, caption, sideways = 0):
    print type(sideways)
    nCol = nCol + 4
    print f.name
    name = f.name.replace('yields','').replace('.tex','').replace('_','')
    name = name.replace('SR','signal region')
    name = name.replace('CR','control region')
    name = name.replace('MB',', main band')
    name = name.replace('SB',', side band')
    print name
    if sideways == 1:
        f.write('\\begin{sidewaystable}[ht] \n ')
    else:
        f.write('\\begin{table}[ht] \n ')

    f.write('\\tiny \n')
    f.write('\\caption{'+caption+'} \n')
    f.write('\\begin{center} \n')

    f.write('\\label{tab:'+f.name.replace('.tex','')+'} \n')
    f.write('\\begin{tabular}{|' + (nCol *'%(align)s | ') % dict(align = 'c') + '} \n')
    f.write('\\hline \n')


def printLatexFooter(f, sideways = 0):
    f.write('\\hline \n')
    f.write('\\end{tabular} \n')
    f.write('\\end{center} \n')
    if sideways > 0:
        f.write('\\end{sidewaystable} \n ')
    else:
        f.write('\\end{table} \n')

if __name__ == "__main__":

    ## remove '-b' option
    if '-b' in sys.argv:
        sys.argv.remove('-b')
        _batchMode = True

    if len(sys.argv) > 1:
        pattern = sys.argv[1]
        print '# pattern is', pattern
    else:
        print "No pattern given!"
        exit(0)

    # Include systematic uncertainties?
    doSys = True

    ## Create Yield Storage

    yds6 = YieldStore("lepYields")
    yds9 = YieldStore("lepYields")
    yds5 = YieldStore("lepYields")
    ydsFew6 = YieldStore("lepYields")
    ydsFew9 = YieldStore("lepYields")

#    a = "YieldsJune12/lumi2p571/"
#    a = "Moriond17_Spring16_RealnISRWeight_IsoTrack_v2/*/"
    #a = "Moriond17_Spring16_RealnISRWeight_IsoTrack_5p2_RunGgeq279931/*/"
    #a = "Moriond17_Spring16_All_Jan15/*/"
    #a = 'makeBinYields05/*/'
    for folder in ['grid-dilep', 'scan']:
        a = '{}/{}/'.format(pattern, folder)

        b = a + 'merged/LT'
        btagMethod = ""
        globfiles = b+"*NJ6*"
        yds6.addFromFiles(globfiles,("lep","sele"))
        globfiles = b+"*NJ9*"
        yds9.addFromFiles(globfiles,("lep","sele"))
        b = a + 'merged4f5/LT'
        globfiles = b+"*NJ5*"
        yds5.addFromFiles(globfiles,("lep","sele"))

        b = a + 'mergedFew/LT'
        globfiles = b+"*NJ6i*"
        ydsFew6.addFromFiles(globfiles,("lep","sele"))
        globfiles = b+"*NJ9*"
        ydsFew9.addFromFiles(globfiles,("lep","sele"))

    yds9.showStats()

    #pattern = 'arturstuff/grid/merged/LT\*NJ6\*'
    printSamps = ['TTsemiLep','TTdiLep','TTV','SingleT', 'WJets', 'DY', 'QCD','VV','background','T1t$^4$ 1.9$/$0.1','T1t$^4$ 1.4$/$1.1']
#    printSamps = ['TTJets','TTV','SingleTop', 'WJets', 'DY','EWK','T1t$^4$ 1.5$/$0.1','T1t$^4$ 1.2$/$0.8']

    if 1 ==1:
        cats = ('SR_MB', 'CR_MB', 'SR_SB', 'CR_SB')
        for cat in cats:
            f =  open('yields' + cat +btagMethod+'.tex','w')
            samps = [('TTsemiLep',cat),('TTdiLep',cat),('TTV',cat), ('SingleT',cat), ('WJets',cat), ('DY',cat), ('QCD',cat),('VV',cat), ('background',cat),
                     ('T1tttt_Scan_mGo1900_mLSP100',cat),('T1tttt_Scan_mGo1400_mLSP1100',cat)]
#            samps = [('TTJets',cat),('TTV',cat), ('SingleTop',cat), ('WJets',cat), ('DY',cat), ('EWK',cat),
#                     ('T1tttt_Scan_mGo1500_mLSP100',cat),('T1tttt_Scan_mGo1200_mLSP800',cat)]
            caption ='Expected event yields in ' + cat.replace('_','\\_') + ' for the multi-b analysis in the search bins as defined in Table~\\ref{tab:def_sr_multi-b}. The following weights are applied to these MC predictions: only nISR weights for \\ttbar. The \\DF is adjusted for each \\LT bin. The contribution of dileptonic \\ttbar events is shown separately, where leptons can be either electrons, muons, or taus.'
            printLatexHeader(len(samps), f, caption, 1)
            srcr = cat.replace('_MB','').replace('_SB','')
            sbmb = cat.replace('SR_','').replace('CR_','')
            label = 'Expected events in '+srcr+' for '+lumi+' fb$^{-1}$ for '+sbmb.replace('MB','$n_{jet}$ 6,8 ').replace('SB','$n_{jet}$ 4,5 for 6,8')
            yds6.printLatexTable(samps, printSamps, label,f, doSys)
            label = 'Expected events in SR for '+lumi+' fb$^{-1}$ for '+sbmb.replace('MB','$n_{jet}$ $\\geq 9$').replace('SB','$n_{jet}$ 4,5 for $\\geq 9$')
            yds9.printLatexTable(samps, printSamps, label, f, doSys)
            printLatexFooter(f, 1)
            f.close()

    f =  open('yields_bckgAllbins' + cat +btagMethod+'.tex','w')
#    samps = [('background','SR_MB'),('T1tttt_Scan_mGo1800_mLSP100','SR_MB'),('T1tttt_Scan_mGo1200_mLSP800','SR_MB'),
#             ('background','CR_MB'),('T1tttt_Scan_mGo1800_mLSP100','CR_MB'),('T1tttt_Scan_mGo1200_mLSP800','CR_MB'),
#             ('background','SR_SB'),('T1tttt_Scan_mGo1800_mLSP100','SR_SB'),('T1tttt_Scan_mGo1200_mLSP800','SR_SB'),
#             ('background','CR_SB'),('T1tttt_Scan_mGo1800_mLSP100','CR_SB'),('T1tttt_Scan_mGo1200_mLSP800','CR_SB')]
#    printSamps = ['background SR\_MB','T1t$^4$ 1.8$/$0.1 SR\_MB','T1t$^4$ 1.2$/$0.8 SR\_MB',
#                  'background CR\_MB','T1t$^4$ 1.8$/$0.1 CR\_MB','T1t$^4$ 1.2$/$0.8 CR\_MB',
#                  'background SR\_SB','T1t$^4$ 1.8$/$0.1 SR\_SB','T1t$^4$ 1.2$/$0.8 SR\_SB',
#                  'background CR\_SB','T1t$^4$ 1.8$/$0.1 CR\_SB','T1t$^4$ 1.2$/$0.8 CR\_SB',]

    samps = [('background','SR_MB'),
             ('background','CR_MB'),
             ('background','SR_SB'),
             ('background','CR_SB')]
    printSamps = ['background SR\_MB',
                  'background CR\_MB',
                  'background SR\_SB',
                  'background CR\_SB']
    caption = 'Expected event yields in the four analysis regions SR\_MB, CR\_MB, SR\_SB, CR\_SB The bin names refer to the previously defined SR\_MB regions, however we follow the merging strategy described. i.e. NB2i\_SB for NB2\/NB3i\_MB and NB1i\_SB for HT4i\_MB'
    printLatexHeader(len(samps), f, caption, 1)
    label = 'Expected events in the four ABCD regions SR\_MB, CR\_MB, SR\_SB, CR\_SB for '+lumi+' fb$^{-1}$ for $n_{jet}$ 6,8'
    yds6.printLatexTable(samps, printSamps, label,f, doSys)
    label = 'Expected events in the four ABCD regions SR\_MB, CR\_MB, SR\_SB, CR\_SB, for '+lumi+' fb$^{-1}$ for $n_{jet}$ $\geq$ 9'
    yds9.printLatexTable(samps, printSamps, label, f, doSys)
    printLatexFooter(f, 1)
    f.close()



    '''print "Prepare dileptonic printout by calculating"
    yds6.divideTwoYieldDictsForRatio('DLCR_MB','SR_MB','DLCR_MB_RelSize')
    yds6.divideTwoYieldDictsForRatio('DLCR_SB','SR_SB','DLCR_SB_RelSize')
    yds9.divideTwoYieldDictsForRatio('DLCR_MB','SR_MB','DLCR_MB_RelSize')
    yds9.divideTwoYieldDictsForRatio('DLCR_SB','SR_SB','DLCR_SB_RelSize')

    yds6.divideTwoYieldDictsForRatio('COPYALL','COPYALL','dummy', False, 'background','data')
    yds9.divideTwoYieldDictsForRatio('COPYALL','COPYALL','dummy', False, 'background','data')

    yds6.divideTwoYieldDictsForRatio('COPYALL','COPYALL','dummy', False, 'DiLep_Inc','background')
    yds9.divideTwoYieldDictsForRatio('COPYALL','COPYALL','dummy', False, 'DiLep_Inc','background')

    yds6.divideTwoYieldDictsForRatio('COPYALL','COPYALL','dummy', False, 'TTdiLep','background')
    yds9.divideTwoYieldDictsForRatio('COPYALL','COPYALL','dummy', False, 'TTdiLep','background')


    OutputHelperList = []
    OutputHelperList.append(OutputHelper(('background','SR_MB'),"all bkg(SR)"))
    OutputHelperList.append(OutputHelper(('DiLep_Inc','SR_MB_RTo_background'),"dilept.(SR)","percentage"))
    OutputHelperList.append(OutputHelper(('TTdiLep','SR_MB_RTo_background'),"ttbar dilept(SR)","percentage"))

    OutputHelperList.append(OutputHelper(('DiLep_Inc','SR_MB'),"Dilept. bkg(SR)"))
#    OutputHelperList.append(OutputHelper(('TTdiLep','SR_MB'),"ttbar dilept. bkg(SR)"))
#    OutputHelperList.append(OutputHelper(('DiLep_Inc','DLCR_MB'),"Dilept. bkg(DLCR)"))
    OutputHelperList.append(OutputHelper(('background','DLCR_MB'),"all bkg(DLCR)"))
    OutputHelperList.append(OutputHelper(('DiLep_Inc','DLCR_MB_RTo_background'),"dilept.(DLCR)","percentage"))
    OutputHelperList.append(OutputHelper(('data','DLCR_MB'),"data(DLCR)"))
#    OutputHelperList.append(OutputHelper(('background','DLCR_MB_RelDataMC'),"MCData(DLCR)","percentage"))
    OutputHelperList.append(OutputHelper(('background','DLCR_MB_RTo_data'),"MCData(DLCR)","percentage"))
    OutputHelperList.append(OutputHelper(('background','CR_MB_RTo_data'),"MCData(CR\_MB)", "percentage"))
#    OutputHelperList.append(OutputHelper(('TTdiLep','DLCR_MB_RelSize'),"rel. size (DLCR) ttdilep", "percentage"))
    OutputHelperList.append(OutputHelper(('DiLep_Inc','DLCR_MB_RelSize'),"rel. size (DLCR)","percentage"))
#    OutputHelperList.append(OutputHelper(('data','DLCR_MB_RelSize'),"rel. size (DLCR)data", "percentage"))

    f =  open('yieldsDLCRComparison.tex','w')
    printLatexHeader(len(OutputHelperList), f)
    yds6.showStats()
    label = 'Yield comparison for DL CR vs. signal region for 2.1 fbinv for njet 6,8 '
    yds6.printLatexTableEnh(OutputHelperList, label,f)
    label = 'Yield comparison for DL CR vs. signal region for 2.1 fbinv for njet $\\geq 9$'
    yds9.printLatexTableEnh(OutputHelperList, label, f)
    printLatexFooter(f)
    '''
    f =  open('4to5j_preditiction.tex','w')
    label = 'Counts and Rcs from 4jet sideband used to predict events in a 5jet signal region $5j_{SR} = Rcs^{4j,data} \\times \\kappa^{EWK, MC} \\times 5j_{CR}$'
    #in case one wants more details
    #printSamps = ['data 4j, SR','data 4j, CR','QCD 4j,CR','(data-QCD) 4j, CR','data 4j, Rcs$^{EWK}$','$\\kappa^{EWK}$, MC','data 5j, CR','QCD 5j, CR','(data-QCD) 5j, CR', 'data 5j, pred', 'data 5j, SR']
    #samps = [('data_QCDsubtr','SR_SB'),('data','CR_SB'),('data_QCDpred','CR_SB'),('data_QCDsubtr','CR_SB'),('data_QCDsubtr','Rcs_SB'),('EWK','Kappa'),('data','CR_MB'),('data_QCDpred','CR_MB'),('data_QCDsubtr','CR_MB'),('data_QCDsubtr','SR_MB_predict'), ('data','SR_MB')]
    printSamps = ['data 4j, SR','(data-QCD) 4j, CR','data 4j, Rcs$^{EWK}$','$\\kappa^{EWK}$, MC','(data-QCD) 5j, CR'
    , 'data 5j, pred', 'data 5j, SR']
    samps = [('data_QCDsubtr','SR_SB'),('data_QCDsubtr','CR_SB'),('data_QCDsubtr','Rcs_SB'),('EWK','Kappa'),('data_QCDsubtr','CR_MB'),
            ('data_QCDsubtr','SR_MB_predict'), ('data','SR_MB')]
    caption =' Test of the background prediction method using the exclusive 4 jet category as a side band to predict the expected number of events in the signal regin of an exclusive 5 jet main band.'
    printLatexHeader(len(samps), f,caption,1)
    yds5.printLatexTable(samps, printSamps, label,f, False)
    printLatexFooter(f, 1)
    f.close()

    caption = 'Background prediction based on the [4,5] jet sideband in the [6,8] and $\geq$ 9 jet signal regions. The observed events in the SR, MB are still blinded.'
    f =  open('4to68_4to9j_prediction.tex','w')

    printLatexHeader(len(samps), f, caption, 1)

    samps = [('data_QCDsubtr','SR_SB'),('data_QCDsubtr','CR_SB'),('data_QCDsubtr','Rcs_SB'),('EWK','Kappa'),('data_QCDsubtr','CR_MB'),
            ('data_QCDsubtr','SR_MB_predict'), ('data','SR_MB')]
    label = 'SB, MB, and predictions for '+lumi+' fb$^{-1}$ for $n_{jet}$ 6,8 '
    printSamps = ['data 45j, SR','(data-QCD) 4j5, CR','data 4j5, Rcs$^{EWK}$','$\\kappa^{EWK}$, MC','(data-QCD) 68j, CR', 'data 68j, pred (val $\pm$ stat $\pm$ syst)', 'data 68j, SR']

    yds6.printLatexTable(samps, printSamps, label,f, doSys)
    label = 'SB, MB, and predictions for '+lumi+'fb$^{-1}$ for njet $\\geq 9$'
    printSamps = ['data 45j, SR','(data-QCD) 4j5, CR','data 4j5, Rcs$^{EWK}$','$\\kappa^{EWK}$, MC','(data-QCD) 9ij, CR', 'data 9ij, pred (val $\pm$ stat $\pm$ syst)', 'data 9ij, SR']
    yds9.printLatexTable(samps, printSamps, label, f, doSys)
    printLatexFooter(f, 1)
    f.close()

    caption = 'Background prediction for aggregate signal regions.'
    f =  open('fewbins_prediction.tex','w')

    printLatexHeader(len(samps), f, caption,1)

    samps = [('data_QCDsubtr','SR_SB'),('data_QCDsubtr','CR_SB'),('data_QCDsubtr','Rcs_SB'),('EWK','Kappa'),('data_QCDsubtr','CR_MB'),
            ('data_QCDsubtr','SR_MB_predict'), ('data','SR_MB')]
    label = 'SB, MB, and predictions for '+lumi+' fb$^{-1}$ for $n_{jet}$ 6,8 '
    printSamps = ['data 45j, SR','(data-QCD) 4j5, CR','data 4j5, Rcs$^{EWK}$','$\\kappa^{EWK}$, MC','(data-QCD) 68j, CR', 'data 68j, pred (val $\pm$ stat)', 'data 68j, SR']
    ydsFew6.printLatexTable(samps, printSamps, label,f, doSys, True)
    printSamps = ['data 45j, SR','(data-QCD) 4j5, CR','data 4j5, Rcs$^{EWK}$','$\\kappa^{EWK}$, MC','(data-QCD) 9ij, CR', 'data 9ij, pred (val $\pm$ stat)', 'data 9ij, SR']
    ydsFew9.printLatexTable(samps, printSamps, label, f, doSys, True)
    printLatexFooter(f, 1)
    f.close()

    caption = 'Expected MC events for the aggregate SR including two signal benchmark points.'
    f =  open('fewbins_small_prediction.tex','w')

    printLatexHeader(len(samps), f, caption,0)

    samps = [('EWK','SR_MB'),('T1tttt_Scan_mGo1900_mLSP100','SR_MB'),('T1tttt_Scan_mGo1400_mLSP1100','SR_MB')]
    label = 'SB, MB, and predictions for '+lumi+' fb$^{-1}$ for $n_{jet}$ 6,8 '
    printSamps = ['MC 6ij','T1tttt 1.9/0.1','T1tttt 1.4/1.1']
    ydsFew6.printLatexTable(samps, printSamps, label,f, False)
    printSamps = ['MC 9ij','T1tttt 1.9/0.1','T1tttt 1.4/1.1']
    ydsFew9.printLatexTable(samps, printSamps, label, f, False)
    printLatexFooter(f, 0)
    f.close()


    f =  open('RCS_mc.tex','w')
    caption = 'Rcs values from SB and MB and kappa'
    lable = 'Rcs values from SB and MB and kappa'

    printSamps = ['$R_{CS}$ [6,8] jets','$R_{CS}$ [4,5] jets','$\kappa$']#, '(Data-QCD) $R_{CS}$ [4,5] jets']
    samps = [('EWK','Rcs_MB'),('EWK','Rcs_SB'),('EWK','Kappa')]#,('data_QCDsubtr','Rcs_SB')]
    printLatexHeader(len(samps), f, caption,0)
    yds6.printLatexTable(samps, printSamps, label,f, doSys)
    printSamps = ['$R_{CS}$ $\geq$ 9 jets','$R_{CS}$ [4,5] jets','$\kappa$']#,'(Data-QCD) $R_{CS}$ [4,5] jets']
    samps = [('EWK','Rcs_MB'),('EWK','Rcs_SB'),('EWK','Kappa')]#,('data_QCDsubtr','Rcs_SB')]
    yds9.printLatexTable(samps, printSamps, label,f, doSys)
    printLatexFooter(f,0)
    f.close()


    f =  open('tabelforLimits.tex','w')
    label = 'SB, MB, and predictions for '+lumi+' fb$^{-1}$ for $n_{jet}$ 6,8 '
    samps = [('data','SR_SB'),('data','CR_SB'),('data','Rcs_SB'),
             ('data','CR_MB'),('EWK','Kappa'),('data','SR_MB_predict'),('data','SR_MB')]

    printSamps = ['data 45j, SR','data 45j, CR','data 4j5, Rcs$^{EWK}$',
                  'data 68j, CR','$\\kappa$ MC','data 68j, SRpred','Obs 68j, SR']
    caption = 'Input values for limit calculation. The 3 regions with data counts are given, as well as the QCD estimate for the control regions in the side and mainband and $\kappa$ derived from simulation. The last two columns represent pseudo data based based on the epxected data prediction or MC simulation.'
    printLatexHeader(len(samps), f, caption, 1)
    yds6.printLatexTable(samps, printSamps, label,f, doSys)
    label = 'SB, MB, and predictions for '+lumi+' fb$^{-1}$ for njet $\\geq 9$'
    printSamps = ['data 45j, SR','data 45j, CR','data 4j5, Rcs$^{EWK}$',
                  'data 9j, CR','$\\kappa$ MC','data 9j, SRpred','Obs 9j SR']
    yds9.printLatexTable(samps, printSamps, label, f, doSys)
    printLatexFooter(f, 1)
    f.close()

    caption = ''
    f =  open('PAS_prediction.tex','w')

    printLatexHeader(len(samps), f, caption, 0)

    samps = [ ('T1tttt_Scan_mGo1900_mLSP100','SR_MB'),('T1tttt_Scan_mGo1400_mLSP1100','SR_MB'),('data_QCDsubtr','SR_MB_predict'), ('data','SR_MB')]
    label = ''
    printSamps = ['1.9/0.1','1.4/1.1', 'Predicted background', 'Observed']
    yds6.printLatexTable(samps, printSamps, label,f, doSys)
    yds9.printLatexTable(samps, printSamps, label, f, doSys)
    printLatexFooter(f, 0)
    f.close()

    # Signal yields
    caption = 'Dummy signal points'
    f =  open('4to68_4to9j_signal.tex','w')
    samps = [('T1tttt_Scan_mGo1900_mLSP100','SR_MB'), ('T1tttt_Scan_mGo1900_mLSP600','SR_MB'), ('T1tttt_Scan_mGo1800_mLSP1100','SR_MB'), ('T1tttt_Scan_mGo1450_mLSP1100','SR_MB'),
            ('data_QCDsubtr','SR_MB_predict'), ('data','SR_MB')]
    printSamps = ['T1tttt (1.9, 0.1)', 'T1tttt (1.9, 0.6)', 'T1tttt (1.8, 1.1)', 'T1tttt (1.45, 1.1)', 'data 68j, pred (val $\pm$ stat $\pm$ syst)', 'data 68j, SR']
    label = 'SR_MB predictions for '+lumi+' fb$^{-1}$ for $n_{jet}$ 6,8 '

    printLatexHeader(len(samps), f, caption, 1)
    yds6.printLatexTable(samps, printSamps, label,f, doSys)

    label = 'SR_MB predictions for '+lumi+' fb$^{-1}$ for njet $\\geq 9$'
    yds9.printLatexTable(samps, printSamps, label, f, doSys)
    printLatexFooter(f, 1)
    f.close()

