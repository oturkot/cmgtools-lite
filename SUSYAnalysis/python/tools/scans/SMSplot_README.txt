#Use the command below to create a file containing the histograms needed to extract the ISR
#normalization variables, adjust mca file if necessary and create softlinks to ntuples
#and friendtrees in a filder called "samples"
../../../../TTHAnalysis/python/plotter/mcPlots.py SMSplot_mca.txt SMSplot_cuts.txt SMSplot_plots.txt -P samples -F sf/t samples/evVarFriend_{cname}.root -l 1 -j 6 --s2v -G -f --tree treeProducerSusySingleLepton
