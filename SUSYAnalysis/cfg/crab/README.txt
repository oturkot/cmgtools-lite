1) Source the CRAB3 environment and run cmsenv (in this order)
> source /cvmfs/cms.cern.ch/crab3/crab.sh
> cmsenv

2) Ensure that you have a valid proxy:
> voms-proxy-init -voms cms --valid=50:00

3) Execute heppy_crab.py with the correct options: see the integrated help
> ./heppy_crab.py --help

4) As an example you can run with
> python heppy_crab.py --cfg-file run_susySinglelepton18_DeepAK8.py --storage-site T2_DE_DESY --output-dir heppyTrees -v ProdMCJan23 -l ProdMCJan23

5) or in full 

> python heppy_crab.py --cfg-file ../run_susyMultilepton_cfg.py --storage-site T2_CH_CERN --output-dir heppyTrees -v ProdMCJan23 -l ProdMCJan23 --option removeJecUncertainties --option analysis="susy" --option mcGroup=0
