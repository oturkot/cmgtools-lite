#!/usr/bin/env python
########### author : Ashraf Kasem Mohamed ##########
########### institute : DESY #######################
########### Email : ashraf.mohamed@desy.de #########
########### Date : April 2018#######################
import sys,os, re, pprint
import re
from os import listdir
from os.path import isfile, join
import argparse
import commands
import subprocess
import shutil
from ROOT import TFile
if  os.path.exists('submit_all_to_batch_HTC.sh'):
   os.remove('submit_all_to_batch_HTC.sh')
cmssw_release = os.environ['CMSSW_BASE']
user = os.environ['USER']

def find_all_matching(substring, path):
	result = []
	for root, dirs, files in os.walk(path):
		for thisfile in files:
			if substring in thisfile:
				result.append(os.path.join(root, thisfile ))
	return result

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Runs a NAF batch system for nanoAOD', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--indir', help='List of datasets to process', metavar='indir')
	parser.add_argument('--outdir', help='output directory',default=None, metavar='outdir')
	#parser.add_argument('--pattern', help='output directory',default=None, metavar='outdir')
	parser.add_argument('--batchMode', '-b', help="Batch mode.", action='store_true')

	args = parser.parse_args()
	batch = args.batchMode
	indire = args.indir
	outdire = args.outdir

	if  os.path.exists(outdire):
		des = raw_input(" this dir is already exist : "+str(outdire)+" do you want to remove it [y/n]: ")
		if ( "y" in des or "Y" in des or "Yes" in des) :
			shutil.rmtree(str(outdire))
			os.makedirs(str(outdire))
		elif ( "N" in des or  "n" in des or  "No" in des ): print str(outdire) , "will be ovewritten by the job output -- take care"
		else :
			raise ValueError( "do not understand your potion")
	else : os.makedirs(str(outdire))
	pattern = os.listdir(indire)
	for pat in pattern :
		#if not ('SingleElectron' in pat or 'MET_' in pat  or 'SingleMuon' in pat): continue
		#if not 'SMS_T1tttt' in pat : continue
		print pat
		patout = outdire+'/'+pat
		os.makedirs(str(patout))
		tarfiles = find_all_matching('heppyOutput_',indire+'/'+pat)
		cmd_list = ['source /cvmfs/cms.cern.ch/cmsset_default.sh','cd '+os.path.abspath(patout) , 'cd '+cmssw_release+'/src','eval `scramv1 ru -sh`','cd -','echo running','export X509_USER_PROXY=/nfs/dust/cms/user/'+user+'/k5-ca-proxy.pem']
		#cmd_list.append('export GFAL_CONFIG_DIR=/cvmfs/grid.cern.ch/emi-ui-3.17.1-1.el6umd4v5/etc/gfal2.d')
		#cmd_list.append('export GFAL_PLUGIN_DIR=/cvmfs/grid.cern.ch/emi-ui-3.17.1-1.el6umd4v5/usr/lib64/gfal2-plugins/')
		for tar in tarfiles:
			chunkname = patout+'/'+pat+'_Chunk'+tar.split('heppyOutput_')[-1].replace('.tgz','')
			os.makedirs(str(chunkname))
			if not batch :
				cmd = 'tar -zxvf '+tar+' -C '+chunkname+' ; mv '+ chunkname+'/Output/* '+chunkname+'; rm -rf '+ chunkname+'/Output/ ; rm -rf '+chunkname+'/heppyOutput_*'
				os.system(cmd)
			else :
				#os.system('cp '+tar+' '+chunkname)
				newChunk = chunkname.split("/")[-1]
				#cmd = 'tar -zxvf '+newChunk+'/heppyOutput_* -C '+newChunk+' ; mv '+ newChunk+'/Output/* '+newChunk+'; rm -rf '+ newChunk+'/Output/ ; rm -rf '+newChunk+'/heppyOutput_*'
				cmd = cmd = 'tar -zxvf '+tar+' -C '+newChunk+' ; mv '+ newChunk+'/Output/* '+newChunk+'; rm -rf '+ newChunk+'/Output/ ; rm -rf '+newChunk+'/heppyOutput_*'
				cmd_list.append(cmd)
		if batch :
			cmd_list.append('heppy_hadd.py .')
			cmd_list.append('rm -rf '+pat+'*_Chunk*')
			#cmd_list.append('gfal-copy '+pat+' srm://dcache-se-cms.desy.de:8443/srm/managerv2?SFN=/pnfs/desy.de/cms/tier2/store/user/amohamed/heppy_final_trees/'+pat)
			#cmd_list.append('rm -rf '+pat)
			cmd_list.append('echo `DONE DONE DONE`')
			scriptFileName = patout+'/batchScript.sh'
			scriptFile = open(scriptFileName,'w')
			scriptFile.writelines("%s\n" % item for item in cmd_list )
			os.system('chmod +x '+patout+'/batchScript.sh')
			scriptFile.close()
			condorFileName = patout+'/condor.sub'
			condorFile = open(condorFileName,'w')
			condorFile.write("Universe = vanilla")
			condorFile.write("\n")
			condorFile.write("Executable ="+os.path.abspath(patout)+'/batchScript.sh')
			condorFile.write("\n")
			condorFile.write("Log  = condor_job_$(Process).log")
			condorFile.write("\n")
			condorFile.write("Output = condor_job_$(Process).out")
			condorFile.write("\n")
			condorFile.write("Error  = condor_job_$(Process).error")
			condorFile.write("\n")
			condorFile.write("getenv      = True")
			condorFile.write("\n")
			condorFile.write("+RequestRuntime = 60*60*9")
			condorFile.write("\n")
			condorFile.write("Queue 1")
			condorFile.write("\n")
			condorFile.close()
			#os.system('condor_submit '+condorFileName)
			file = open('submit_all_to_batch_HTC.sh','a')
			file.write("\n")
			file.write("condor_submit "+condorFileName)
			file.close()
		else :
			pwd = os.getcwd()
			os.chdir(patout)
			os.system('heppy_hadd.py .')
			os.chdir(pwd)
	if batch:
		os.system('chmod a+x submit_all_to_batch_HTC.sh')
		print 'submit_all_to_batch_HTC.sh Created for you - you can run it now with ./'

