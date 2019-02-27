blinded = False

binsBDT = {}

######## for 2016 
binsBDT['BDT1']= ('0.0 <= BDT && BDT <=0.005','[0.0,0.005]')
binsBDT['BDT2']= ('0.005 < BDT && BDT <=0.010','[0.005,0.010]')
binsBDT['BDT3']= ('0.010 < BDT && BDT <=0.015','[0.010,0.015]')
binsBDT['BDT4']= ('0.015 < BDT && BDT <=0.020','[0.015,0.020]')
binsBDT['BDT5']= ('0.020 < BDT && BDT <=0.025','[0.020,0.025]')
binsBDT['BDT6']= ('0.025 < BDT && BDT <=0.030','[0.025,0.030]')
binsBDT['BDT7']= ('0.030 < BDT && BDT <=0.035','[0.030,0.035]')
binsBDT['BDT8']= ('0.035 < BDT && BDT <=0.040','[0.035,0.040]')
binsBDT['BDT9']= ('0.040 < BDT && BDT <=0.045','[0.040,0.045]')
binsBDT['BDT10']= ('0.045 < BDT && BDT <=0.050','[0.045,0.050]')
binsBDT['BDT11']= ('0.050 < BDT && BDT <=0.055','[0.050,0.055]')
binsBDT['BDT12']= ('0.055 < BDT && BDT <=0.060','[0.055,0.060]')
binsBDT['BDT13']= ('0.060 < BDT && BDT <=0.065','[0.060,0.065]')
binsBDT['BDT14']= ('0.065 < BDT && BDT <=0.070','[0.065,0.070]')
binsBDT['BDT15']= ('0.070 < BDT && BDT <=0.075','[0.070,0.075]')
binsBDT['BDT16']= ('0.075 < BDT && BDT <=0.080','[0.075,0.080]')
binsBDT['BDT17']= ('0.080 < BDT && BDT <=0.085','[0.080,0.085]')
binsBDT['BDT18']= ('0.085 < BDT && BDT <=0.090','[0.085,0.090]')
binsBDT['BDT19']= ('0.090 < BDT && BDT <=0.095','[0.090,0.095]')
binsBDT['BDT20']= ('0.095 < BDT && BDT <=0.100','[0.095,0.100]')
binsBDT['BDT21']= ('0.100 < BDT && BDT <=0.105','[0.100,0.105]')
binsBDT['BDT22']= ('0.105 < BDT && BDT <=0.110','[0.105,0.110]')
binsBDT['BDT23']= ('0.110 < BDT && BDT <=0.115','[0.110,0.115]')
binsBDT['BDT24']= ('0.115 < BDT && BDT <=0.120','[0.115,0.120]')
binsBDT['BDT25']= ('0.120 < BDT && BDT <=0.125','[0.120,0.125]')
binsBDT['BDT26']= ('0.125 < BDT && BDT <=0.130','[0.125,0.130]')
binsBDT['BDT27']= ('0.130 < BDT && BDT <=0.135','[0.130,0.135]')
binsBDT['BDT28']= ('0.135 < BDT && BDT <=0.140','[0.135,0.140]')
binsBDT['BDT29']= ('0.140 < BDT && BDT <=0.145','[0.140,0.145]')
binsBDT['BDT30']= ('0.145 < BDT && BDT <=0.150','[0.145,0.150]')
binsBDT['BDT31']= ('0.150 < BDT && BDT <=0.155','[0.150,0.155]')
binsBDT['BDT32']= ('0.155 < BDT && BDT <=0.160','[0.155,0.160]')
binsBDT['BDT33']= ('0.160 < BDT && BDT <=0.165','[0.160,0.165]')
binsBDT['BDT34']= ('0.165 < BDT && BDT <=0.170','[0.165,0.170]')
binsBDT['BDT35']= ('0.170 < BDT && BDT <=0.175','[0.170,0.175]')
binsBDT['BDT36']= ('0.175 < BDT && BDT <=0.180','[0.175,0.180]')
binsBDT['BDT37']= ('0.180 < BDT && BDT <=0.185','[0.180,0.185]')
binsBDT['BDT38']= ('0.185 < BDT && BDT <=0.190','[0.185,0.190]')
binsBDT['BDT39']= ('0.190 < BDT && BDT <=0.195','[0.190,0.195]')
binsBDT['BDT40']= ('0.195 < BDT && BDT <=0.200','[0.195,0.200]')
binsBDT['BDT41']= ('0.200 < BDT && BDT <=0.205','[0.200,0.205]')
binsBDT['BDT42']= ('0.205 < BDT && BDT <=0.210','[0.205,0.210]')
binsBDT['BDT43']= ('0.210 < BDT && BDT <=0.215','[0.210,0.215]')
binsBDT['BDT44']= ('0.215 < BDT && BDT <=0.220','[0.215,0.220]')
binsBDT['BDT45']= ('0.220 < BDT && BDT <=0.225','[0.220,0.225]')
binsBDT['BDT46']= ('0.225 < BDT && BDT <=0.230','[0.225,0.230]')
binsBDT['BDT47']= ('0.230 < BDT && BDT <=0.235','[0.230,0.235]')
binsBDT['BDT48']= ('0.235 < BDT && BDT <=0.240','[0.235,0.240]')
binsBDT['BDT49']= ('0.240 < BDT && BDT <=0.245','[0.240,0.245]')
binsBDT['BDT50']= ('0.245 < BDT && BDT <=0.250','[0.245,0.250]')
binsBDT['BDT51']= ('0.250 < BDT && BDT <=0.255','[0.250,0.255]')
binsBDT['BDT52']= ('0.255 < BDT && BDT <=0.260','[0.255,0.260]')
binsBDT['BDT53']= ('0.260 < BDT && BDT <=0.265','[0.260,0.265]')
binsBDT['BDT54']= ('0.265 < BDT && BDT <=0.270','[0.265,0.270]')
binsBDT['BDT55']= ('0.270 < BDT && BDT <=0.275','[0.270,0.275]')
binsBDT['BDT56']= ('0.275 < BDT && BDT <=0.280','[0.275,0.280]')
binsBDT['BDT57']= ('0.280 < BDT && BDT <=0.285','[0.280,0.285]')
binsBDT['BDT58']= ('0.285 < BDT && BDT <=0.290','[0.285,0.290]')
binsBDT['BDT59']= ('0.290 < BDT && BDT <=0.295','[0.290,0.295]')
binsBDT['BDT60']= ('BDT > 0.295','$\geq$  0.295')



cutDict = {}
cutDictSR = {}
cutDictCR = {}


for BDT_bin in binsBDT:
    BDT_cut = binsBDT[BDT_bin][0]

    binname = "%s_SR" %(BDT_bin)
    cutDict[binname] = [("base",BDT_bin,BDT_cut)]
    # split to SR/CR
    cutDictSR[binname] = [("base",BDT_bin,BDT_cut)]

'''
for CBDT_bin in binsCBDT:
    CBDT_cut = binsCBDT[CBDT_bin][0]

    binname = "%s_CR" %(CBDT_bin.replace("BDTC","BDT"))
    cutDict[binname] = [("base",CBDT_bin,CBDT_cut)]
    # split to SR/CR
    cutDictCR[binname] = [("base",CBDT_bin,CBDT_cut)]
'''
