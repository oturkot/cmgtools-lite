#!/usr/bin/env python

import os.path
from os import listdir

def resubmitJobs(options):
    
    stdir, stjoblistname = options.stinfile.rsplit('/', 1)
#    print 'Work dir: ', stdir
    joblistid = stjoblistname.rsplit('.')[0].split('_')[1]
#    print 'Job list id: ', joblistid
    
    with open(options.stinfile) as fin:
        content = fin.readlines()
    content = [x.strip() for x in content]
    
    iNresub = 0
    logdir = 'logs/' + stdir
    logdirf = logdir +'/fails'
    if not os.path.exists(logdirf): os.system("mkdir -p "+logdirf)
    
    for stline in content:
        stmp, stopt, stval = stline.rpartition('-c')
        if stopt == '':
            stmp, stopt, stval = stline.rpartition('--chunk')
            if stopt == '':
                print "Chunk option not found !"
                exit(0)
        
        ichunk = int(stval.split()[0])
        stchunk = str(ichunk + 1)

        files = list(f for f in listdir(logdir) if f.endswith('.' + stchunk))
        if len(files) == 1:
            filefull = logdir + '/' + files[0]
            if os.path.isfile(filefull) and os.access(filefull, os.R_OK):
                with open(filefull, 'r') as filein:
                    if "Finished" not in filein.read():
                        iNresub += 1
                        os.system("mv "+filefull+" "+logdirf+"/")
                        subCmd = 'qsub -t %s -o %s nafbatch_runner.sh %s' %(stchunk,logdir,options.stinfile)
                        os.system(subCmd)
        elif len(files) > 1:
            print "More than one log file exists for chunk ", stchunk, " :"
            for f in files:
                print f
        else:
            print "Log file does not exist for chunk ", stchunk, " ."
    
    if iNresub > 0:
        print iNresub, " jobs have been resubmitted."
    else:
        print "All jobs are finished, nothing to resubmit."
        
#    newjobList.close()
    return 1

if __name__ == "__main__":


    from optparse import OptionParser
    parser = OptionParser()

    parser.usage = '%prog [options]'
    parser.description="""
    Resubmit bin yields jobs.
    """
    # I/O options
    parser.add_option("--if", "--inputfile", dest="stinfile", type="string", default="none", help="input file name")
    
    # Read options and args
    (options,args) = parser.parse_args()

    if len(args) > 0:
        print 'Arguments: ', args
    
    if options.stinfile != "none":
    
        print 'Processing joblist: ', options.stinfile
        resubmitJobs(options)
        exit(0)
        
    else:
        
        print "Please provide the input file!"
