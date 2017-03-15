#!/usr/bin/env python
#import re, sys, os, os.path

import glob, os, sys, math




#Scale-Env

firstPart = """
### Signal systematic: scale variation
./makeBinYields.py --mca ../systs/signal/scale/mca-Spring16_Signal_forMoriond17.txt --signal --systs True -v2 -l 35.6 -b -od lum36fb/signal/scale


T1tttt_Scan : SMS_T1tttt_TuneCUETP8M1_1_Norm10393971 : susyXsec*10393971/susyNgen*lepSF*btagSF*LHEweight_wgt[0]/LHEweight_original;
T1tttt_Scan : SMS_T1tttt_TuneCUETP8M1_2_Norm10414335 : susyXsec*10414335/susyNgen*lepSF*btagSF*LHEweight_wgt[0]/LHEweight_original;
T1tttt_Scan : SMS_T1tttt_TuneCUETP8M1_3_Norm10327389 : susyXsec*10327389/susyNgen*lepSF*btagSF*LHEweight_wgt[0]/LHEweight_original;

"""




def returnWeightSnippe(index):
    temp = """

T1tttt_ScanScale-Env{0} : SMS_T1tttt_TuneCUETP8M1_1_Norm10393971 : susyXsec*10393971/susyNgen*lepSF*btagSF*LHEweight_wgt[{0}]/LHEweight_original;
T1tttt_ScanScale-Env{0} : SMS_T1tttt_TuneCUETP8M1_2_Norm10414335 : susyXsec*10414335/susyNgen*lepSF*btagSF*LHEweight_wgt[{0}]/LHEweight_original;
T1tttt_ScanScale-Env{0} : SMS_T1tttt_TuneCUETP8M1_3_Norm10327389 : susyXsec*10327389/susyNgen*lepSF*btagSF*LHEweight_wgt[{0}]/LHEweight_original;
""".format(index)
    return temp

f = open('mca-Spring16_Signal_forMoriond17.txt', 'w')
f.write(firstPart)
for i in [1,2,3,4,6,8]:
    f.write(returnWeightSnippe(i))
f.close()


#just for reference: if the above does not work on the batch system, one can split up the mca and run separetely, e.g. a la 
#split = 0
#f = open('mca-Summer16_Moriond17_{0}.txt'.format(split), 'w')
#f.write(firstPart)
#for i in range (9,110):
#    if i%10==0:
#        f.close()
#        split += 1
#        f = open('mca-Summer16_Moriond17_{0}.txt'.format(split), 'w')
#        f.write(firstPart)
#    f.write(returnWeightSnippe(i))
#f.close()
#
#
#for i in range (0,split+1):
#    print "./makeBinYields.py --mca ../systs/PDFUnc-RMS/mca-Summer16_Moriond17_{split}.txt -P ../systs/PDFUnc-RMS/links -F sf/t ../systs/PDFUnc-RMS/links/Friends/DileptonPreapproval/evVarFriend_{cname}.root -l 2.2 --grid -v 2 --od lumi22fb_DlMakeBinYields/PDFUnc-RMS_{split} --syst -b".format(cname="{cname}",split=i)
