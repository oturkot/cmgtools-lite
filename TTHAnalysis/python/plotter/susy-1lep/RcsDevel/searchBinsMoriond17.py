blinded = False

# LT bins
binsLT = {}
binsLT['LTi'] = ('250 < LT','$\geq$ 250')

binsLT['LT1'] = ('250 < LT && LT < 350','[250, 350]')
binsLT['LT12'] = ('250 < LT && LT < 450','[250, 450]')
binsLT['LT13'] = ('250 < LT && LT < 600','[250, 600]')

binsLT['LT2'] = ('350 < LT && LT < 450','[350, 450]')
binsLT['LT3'] = ('450 < LT && LT < 600','[450, 600]')
binsLT['LT4'] = ('600 < LT && LT < 750','[600, 750]')
binsLT['LT1i'] = ('250 < LT','$\geq$ 250')
binsLT['LT2i'] = ('350 < LT','$\geq$ 350')
binsLT['LT3i'] = ('450 < LT','$\geq$ 450')
binsLT['LT4i'] = ('600 < LT','$\geq$ 600')
binsLT['LT5i'] = ('750 < LT','$\geq$ 750')


binsLT['DLLT1'] = ('250 < DL_ST[2] && DL_ST[2] < 350','[250, 350]')
binsLT['DLLT2'] = ('350 < DL_ST[2] && DL_ST[2] < 450','[350, 450]')
binsLT['DLLT3'] = ('450 < DL_ST[2] && DL_ST[2] < 600','[450, 600]')
binsLT['DLLT3i'] = ('450 < DL_ST[2]','$\geq$ 450')
binsLT['DLLT4i'] = ('600 < DL_ST[2]','$\geq$ 600')

DLLTDict = {}
DLLTDict['LT1']  = 'DLLT1'
DLLTDict['LT2']  = 'DLLT2'
DLLTDict['LT3']  = 'DLLT3'
DLLTDict['LT3i'] = 'DLLT3i'
DLLTDict['LT4i'] = 'DLLT4i'


# HT bins
binsHT = {}

binsHT['HT0'] = ('500 < HT && HT < 750','[500, 750]')
binsHT['HT02'] = ('500 < HT && HT < 1250','[500, 1250]')
binsHT['HT03'] = ('500 < HT && HT < 1500','[500, 1500]')
binsHT['HT1'] = ('750 < HT && HT < 1000','[750, 1000]')
binsHT['HT2'] = ('1000 < HT && HT < 1250','[1000, 1250]')
binsHT['HT23'] = ('1000 < HT && HT < 1500','[1000, 1500]')
binsHT['HT3'] = ('1250 < HT && HT < 1500','[1250, 1500]')
binsHT['HT0i'] = ('500 < HT','$\geq$ 500')
binsHT['HT1i'] = ('750 < HT','$\geq$ 750')
binsHT['HT2i'] = ('1000 < HT','$\geq$ 1000')
binsHT['HT3i'] = ('1250 < HT','$\geq$ 1250')
binsHT['HT4i'] = ('1500 < HT','$\geq$ 1500')
binsHT['HT01'] = ('500 < HT && HT < 1000','[500, 1000]')

##binsHT for dilepton study (HT recalculated ([2] option for now))
binsHT['DLHT0i'] = ('500 < DL_HT[2]','$\geq$ 500')
binsHT['DLHT0'] = ('500 < DL_HT[2] && DL_HT[2] < 750','[500, 750]')
binsHT['DLHT1'] = ('750 < DL_HT[2] && DL_HT[2] < 1250','[750, 1250]')
binsHT['DLHT1i'] = ('750 < DL_HT[2]','$\geq$ 750')
binsHT['DLHT2i'] = ('1250 < DL_HT[2]','$\geq$ 1250')
binsHT['DLHT01'] = ('500 < DL_HT[2] && DL_HT[2] < 1250','[500, 1250]')

DLHTDict = {}
DLHTDict['HT0i'] = 'DLHT0i'
DLHTDict['HT0']  = 'DLHT0'
DLHTDict['HT1']  = 'DLHT1'
DLHTDict['HT1i'] = 'DLHT1i'
DLHTDict['HT2i'] = 'DLHT2i'
DLHTDict['HT01'] = 'DLHT01'




# NB bins
binsNB = {}
binsNB['NB0'] = ('nBJet == 0','$=$ 0')
binsNB['NB1'] = ('nBJet == 1','$=$ 1')
binsNB['NB2'] = ('nBJet == 2','$=$ 2')
binsNB['NB12'] = ('nBJet == 2','[1,2]')
binsNB['NB0i'] = ('nBJet >= 0','$\geq$ 0')
binsNB['NB1i'] = ('nBJet >= 1','$\geq$ 1')
binsNB['NB2i'] = ('nBJet >= 2','$\geq$ 2')
binsNB['NB3i'] = ('nBJet >= 3','$\geq$ 3')

# NJ Bins
binsNJ = {}
binsNJ['NJ34'] = ('3 <= nJets30Clean && nJets30Clean <= 4','[3, 4]')
binsNJ['NJ4i'] = ('4 <= nJets30Clean','$\geq$ 4')
binsNJ['NJ45'] = ('4 <= nJets30Clean && nJets30Clean <= 5','[4, 5]')
binsNJ['NJ45f9'] = ('4 <= nJets30Clean && nJets30Clean <= 5','[4, 5]')
binsNJ['NJ45f6'] = ('4 <= nJets30Clean && nJets30Clean <= 5','[4, 5]')
binsNJ['NJ68'] = ('6 <= nJets30Clean && nJets30Clean <= 8','[6, 8]')
binsNJ['NJ6i'] = ('6 <= nJets30Clean ','$\geq$ 6')
binsNJ['NJ9i'] = ('9 <= nJets30Clean','$\geq$ 9')
binsNJ['NJ5'] = ('nJets30Clean == 5','[5]')
binsNJ['NJ4f5'] = ('nJets30Clean == 4','[4]')


def getSRcut(nj_bin, lt_bin, sr_bin, blinded):

    dPhiCut = "dPhi "
    cutLbl = "$\delta \phi "

    if "SR" in sr_bin:
        dPhiCut += " > "
        cutLbl += " > $ "
    elif "CR" in sr_bin:
        dPhiCut += " < "
        cutLbl += " < $ "

    ## DPhi Cuts for LT bins
    cuts = { "LT1": 1.0, "LT1i": 1.0, "LT2": 0.75,"LT2i": 0.75, "LT3": 0.75, "LT3i": 0.75, "LT4": 0.5, "LT4i": 0.5 , "LT5i":0.5}

    for bin in cuts:
        if bin in lt_bin:
            cut = cuts[bin]; break
    else:
        print "No cut found for", nj_bin, lt_bin
        cut = 0

    if blinded and ('68' in nj_bin or '9i' in nj_bin) and "SR" in sr_bin:
        cut = 99.0

    dPhiCut += str(cut)
    cutLbl += str(cut)

    #print nj_bin, lt_bin, sr_bin, dPhiCut, cutLbl

    return (dPhiCut,cutLbl)


### REAL SEARCH BINS (also for RCS)
cutDict = {}
cutDictf9 = {}

cutDictSR = {}
cutDictCR = {}

cutDictSRf9 = {}
cutDictCRf9 = {}


for nj_bin in ['NJ45f6','NJ68']:#binsNJ.iteritems():
    nj_cut = binsNJ[nj_bin][0]

    nbbins = []
    if nj_bin in ['NJ45f6']:
        nbbins += ['NB1','NB1i','NB2i']

    if nj_bin in ['NJ68']:
        nbbins += ['NB1','NB2','NB3i']

    for nb_bin in nbbins:
        nb_cut = binsNB[nb_bin][0]
        
        ltbins =[]

        if nb_bin in ['NB1','NB2','NB2i','NB1i']:
            ltbins += ['LT12','LT3','LT4','LT5i']
        if nb_bin in ['NB3i','NB2i','NB1i']:
            ltbins += ['LT12','LT3','LT4i']
        
        for lt_bin in ltbins:
            lt_cut = binsLT[lt_bin][0]
            htbins = []
            if nj_bin in ['NJ45f6']:
                if nb_bin == 'NB1i' and lt_bin not in ['LT5i']:
                    htbins+= ['HT4i']
                else:
                    if lt_bin in ['LT12','LT3','LT4']:
                        htbins += ['HT01','HT23']
                    if lt_bin in ['LT5i','LT4i']:
                        htbins += ['HT0i']
#                    if lt_bin in ['LT4i']:
#                        htbins += ['HT03'] 
 
            else:
                if lt_bin in ['LT12','LT3','LT4']:
                    htbins += ['HT01','HT23','HT4i']
                if lt_bin in ['LT5i','LT4i']:
                    htbins += ['HT0i']
#                if lt_bin in ['LT4i']:
#                    htbins += ['HT03','HT4i'] 
            
            for ht_bin in htbins:
                ht_cut =binsHT[ht_bin][0]

                binname = "%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin)
                cutDict[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut)]

                # split to SR/CR
                for sr_bin in ['SR']:
                    sr_cut = getSRcut(nj_bin, lt_bin, sr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin,sr_bin)
                    cutDictSR[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",sr_bin,sr_cut)]

                for cr_bin in ['CR']:
                    cr_cut = getSRcut(nj_bin, lt_bin, cr_bin, blinded)[0]
                    binname = "%s_%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin,cr_bin)
                    cutDictCR[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",cr_bin,cr_cut)]




### FIXME
for nj_bin in ['NJ45f9','NJ9i']:#binsNJ.iteritems():
    nj_cut = binsNJ[nj_bin][0]

    nbbins = []
    if nj_bin in ['NJ45f9']:
        nbbins += ['NB1','NB1i','NB2i']

    if nj_bin in ['NJ9i']:
        nbbins += ['NB1','NB2','NB3i']

    for nb_bin in nbbins:
        nb_cut = binsNB[nb_bin][0]
        
        ltbins =[]
        ltbins += ['LT12','LT3i']
        
        for lt_bin in ltbins:
            lt_cut = binsLT[lt_bin][0]
            htbins = []
            
            if nj_bin in ['NJ45f9']:
                if nb_bin == 'NB1i':
                    htbins+= ['HT4i']
                else:
                    htbins += ['HT03']

            else:
                htbins += ['HT03','HT4i']

            for ht_bin in htbins:
                ht_cut =binsHT[ht_bin][0]


                binname = "%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin)

                cutDictf9[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut)]

# split to SR/CR

                for sr_bin in ['SR']:
                    sr_cut = getSRcut(nj_bin, lt_bin, sr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin,sr_bin)
                    cutDictSRf9[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",sr_bin,sr_cut)]

                for cr_bin in ['CR']:
                    cr_cut = getSRcut(nj_bin, lt_bin, cr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin,cr_bin)
                    cutDictCRf9[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",cr_bin,cr_cut)]



#####Dictionaries for data cross check from 4 to 5
cutDictf5 = {}
cutDictSRf5 = {}
cutDictCRf5 = {}


for nj_bin in ['NJ4f5','NJ5']:#binsNJ.iteritems():

    nj_cut = binsNJ[nj_bin][0]

    nbbins = []
    if nj_bin in ['NJ4f5']:
        nbbins += ['NB1i']

    if nj_bin in ['NJ5']:
        nbbins += ['NB1i']


    for nb_bin in nbbins:
        nb_cut = binsNB[nb_bin][0]
        
        ltbins =[]
        if nb_bin == 'NB1i':
            ltbins += ['LT12','LT3','LT4','LT5i']
        
        for lt_bin in ltbins:
            lt_cut = binsLT[lt_bin][0]
            htbins = []
            if lt_bin == 'LT5i':

                htbins += ['HT0i']
            else:
                htbins += ['HT01','HT23','HT4i']
                
            for ht_bin in htbins:
                ht_cut =binsHT[ht_bin][0]
    

                binname = "%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin)

                cutDictf5[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut)]

# split to SR/CR

                for sr_bin in ['SR']:
                    sr_cut = getSRcut(nj_bin, lt_bin, sr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin,sr_bin)
                    cutDictSRf5[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",sr_bin,sr_cut)]

                for cr_bin in ['CR']:
                    cr_cut = getSRcut(nj_bin, lt_bin, cr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s" %(lt_bin,ht_bin,nb_bin,nj_bin,cr_bin)
                    cutDictCRf5[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",cr_bin,cr_cut)]



#####Dictionaries for data cross check from 4 to 5
cutDictfFew = {}
cutDictSRfFew = {}
cutDictCRfFew = {}

for nj_bin in ['NJ45f6','NJ6i','NJ45f9','NJ9i']:#binsNJ.iteritems():

    nj_cut = binsNJ[nj_bin][0]

    nbbins = []
    if nj_bin in ['NJ45f9']:
        nbbins += ['NB1i','NB2i']

    if nj_bin in ['NJ45f6']:
        nbbins += ['NB1i','NB2i']

    if nj_bin in ['NJ9i']:
        nbbins += ['NB2i','NB3i']
    if nj_bin in ['NJ6i']:
        nbbins += ['NB1i','NB3i']


    for nb_bin in nbbins:
        nb_cut = binsNB[nb_bin][0]
        ltbins =[]
        if nj_bin in ['NJ45f6','NJ6i']:
            ltbins += ['LT4i']

        if nj_bin in ['NJ9i']:
            if nb_bin in ['NB1i','NB3i']:
                ltbins += ['LT1i','LT3i']
            if nb_bin in ['NB2i']:
                ltbins += ['LT3i']


        if nj_bin in ['NJ45f9']:
            ltbins += ['LT1i','LT3i']

        for lt_bin in ltbins:
            lt_cut = binsLT[lt_bin][0]
            htbins = []
            if nj_bin in ['NJ45f6','NJ6i']:
                htbins += ['HT2i']

            if nj_bin in ['NJ45f9','NJ9i']:
                if nb_bin in ['NB1i']:
                    htbins += ['HT4i']
                else:
                    htbins += ['HT0i','HT4i']

                
            for ht_bin in htbins:
                ht_cut =binsHT[ht_bin][0]
    

                binname = "%s_%s_%s_%s_Few" %(lt_bin,ht_bin,nb_bin,nj_bin)

                cutDictfFew[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut)]

# split to SR/CR

                for sr_bin in ['SR']:
                    sr_cut = getSRcut(nj_bin, lt_bin, sr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s_Few" %(lt_bin,ht_bin,nb_bin,nj_bin,sr_bin)
                    cutDictSRfFew[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",sr_bin,sr_cut)]

                for cr_bin in ['CR']:
                    cr_cut = getSRcut(nj_bin, lt_bin, cr_bin, blinded)[0]

                    binname = "%s_%s_%s_%s_%s_Few" %(lt_bin,ht_bin,nb_bin,nj_bin,cr_bin)
                    cutDictCRfFew[binname] = [("base",lt_bin,lt_cut),("base",ht_bin,ht_cut),("base",nb_bin,nb_cut),("base",nj_bin,nj_cut),("base",cr_bin,cr_cut)]

