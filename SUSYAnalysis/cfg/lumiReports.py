import os
dirs = [x for x in next(os.walk('.'))[1]]
print dirs

for d in dirs:
    print d
    os.chdir(d)
    os.system("pwd ")
    os.system('heppy_report.py JSONAnalyzer -a "" ')
    os.system('brilcalc lumi -b "STABLE BEAMS" -u /fb --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -i JSONAnalyzer/lumiSummary.json &> lumi.txt')
    os.system('tail -n 5 lumi.txt')
    os.chdir('..')



