/// \file
/// \ingroup tutorial_tmva
/// \notebook -nodraw
/// This example shows the training of signal with three different backgrounds
/// Then in the application a tree is created with all signal and background
/// events where the true class ID and the three classifier outputs are added
/// finally with the application tree, the significance is maximized with the
/// help of the TMVA genetic algrorithm.
/// - Project   : TMVA - a Root-integrated toolkit for multivariate data analysis
/// - Package   : TMVA
/// - Exectuable: TMVAGAexample
///
/// \macro_output
/// \macro_code
/// \author Andreas Hoecker


#include <iostream> // Stream declarations
#include <vector>
#include <limits>

#include "TChain.h"
#include "TCut.h"
#include "TDirectory.h"
#include "TH1F.h"
#include "TH1.h"
#include "TMath.h"
#include "TFile.h"
#include "TStopwatch.h"
#include "TROOT.h"
#include "TSystem.h"

#include "TMVA/GeneticAlgorithm.h"
#include "TMVA/GeneticFitter.h"
#include "TMVA/IFitterTarget.h"
#include "TMVA/Factory.h"
#include "TMVA/DataLoader.h"//required to load dataset
#include "TMVA/Reader.h"

using namespace std;

using namespace TMVA;

// ----------------------------------------------------------------------------------------------
// Training
// ----------------------------------------------------------------------------------------------
//
int TMVA_1lep_CMG_v6_LWt01(TString myMethodList = "" ){
	
	
	
	   // The explicit loading of the shared libTMVA is done in TMVAlogon.C, defined in .rootrc
   // if you use your private .rootrc, or run from a different directory, please copy the
   // corresponding lines from .rootrc

   // Methods to be processed can be given as an argument; use format:
   //
   //     mylinux~> root -l TMVAClassification.C\(\"myMethod1,myMethod2,myMethod3\"\)

   //---------------------------------------------------------------
   // This loads the library
   TMVA::Tools::Instance();
   //ROOT::R::TRInterface &r = ROOT::R::TRInterface::Instance();

   // Default MVA methods to be trained + tested
   std::map<std::string,int> Use;

   // Cut optimisation
   Use["Cuts"]            = 1;
   Use["CutsD"]           = 1;
   Use["CutsPCA"]         = 0;
   Use["CutsGA"]          = 0;
   Use["CutsSA"]          = 0;
   //
   // 1-dimensional likelihood ("naive Bayes estimator")
   Use["Likelihood"]      = 1;
   Use["LikelihoodD"]     = 0; // the "D" extension indicates decorrelated input variables (see option strings)
   Use["LikelihoodPCA"]   = 1; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
   Use["LikelihoodKDE"]   = 0;
   Use["LikelihoodMIX"]   = 0;
   //
   // Mutidimensional likelihood and Nearest-Neighbour methods
   Use["PDERS"]           = 1;
   Use["PDERSD"]          = 0;
   Use["PDERSPCA"]        = 0;
   Use["PDEFoam"]         = 1;
   Use["PDEFoamBoost"]    = 0; // uses generalised MVA method boosting
   Use["KNN"]             = 1; // k-nearest neighbour method
   //
   // Linear Discriminant Analysis
   Use["LD"]              = 1; // Linear Discriminant identical to Fisher
   Use["Fisher"]          = 0;
   Use["FisherG"]         = 0;
   Use["BoostedFisher"]   = 0; // uses generalised MVA method boosting
   Use["HMatrix"]         = 0;
   //
   // Function Discriminant analysis
   Use["FDA_GA"]          = 1; // minimisation of user-defined function using Genetics Algorithm
   Use["FDA_SA"]          = 0;
   Use["FDA_MC"]          = 0;
   Use["FDA_MT"]          = 0;
   Use["FDA_GAMT"]        = 0;
   Use["FDA_MCMT"]        = 0;
   //
   // Neural Networks (all are feed-forward Multilayer Perceptrons)
   Use["MLP"]             = 0; // Recommended ANN
   Use["MLPBFGS"]         = 0; // Recommended ANN with optional training method
   Use["MLPBNN"]          = 1; // Recommended ANN with BFGS training method and bayesian regulator
   Use["CFMlpANN"]        = 0; // Depreciated ANN from ALEPH
   Use["TMlpANN"]         = 0; // ROOT's own ANN
   Use["DNN_GPU"]         = 0; // CUDA-accelerated DNN training.
   Use["DNN_CPU"]         = 0; // Multi-core accelerated DNN.
   //
   // Support Vector Machine
   Use["SVM"]             = 1;
   //
   // Boosted Decision Trees
   Use["BDT"]             = 1; // uses Adaptive Boost
   Use["BDTG"]            = 0; // uses Gradient Boost
   Use["BDTB"]            = 0; // uses Bagging
   Use["BDTD"]            = 0; // decorrelation + Adaptive Boost
   Use["BDTF"]            = 0; // allow usage of fisher discriminant for node splitting
   //
   // Friedman's RuleFit method, ie, an optimised series of cuts ("rules")
   Use["RuleFit"]         = 1;
   // ---------------------------------------------------------------

   std::cout << std::endl;
   std::cout << "==> Start TMVAClassification" << std::endl;

   // Select methods (don't look at this code - not of interest)
   if (myMethodList != "") {
      for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) it->second = 0;

      std::vector<TString> mlist = TMVA::gTools().SplitString( myMethodList, ',' );
      for (UInt_t i=0; i<mlist.size(); i++) {
         std::string regMethod(mlist[i]);

         if (Use.find(regMethod) == Use.end()) {
            std::cout << "Method \"" << regMethod << "\" not known in TMVA under this name. Choose among the following:" << std::endl;
            for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) std::cout << it->first << " ";
            std::cout << std::endl;
            return 1;
         }
         Use[regMethod] = 1;
      }
   }

		std::string factoryOptions( "!V:!Silent:Transformations=I;D;P;G,D:AnalysisType=Classification" );
		//string inputFolder = "/nfs/dust/cms/user/amohamed/susy-desy/CMGSamples/Friends_for_Limits/";
		string inputFolder = "./2016_BKG_friends_split/Training_T01/";
	
   Double_t signalWeight      = 1.0;
   Double_t backgroundWeight = 1.0;
   Double_t lumi=35.9 ;
   // Create a new root output file.
   TString outfileName( "TMVA_BDT_T1tttt_1750_1000.root" );
   TFile* outputFile = TFile::Open( outfileName, "RECREATE" );
   // ____________
   TMVA::Factory *factory = new TMVA::Factory( "TMVAClassification", outputFile, factoryOptions );
   TMVA::DataLoader *dataloader=new TMVA::DataLoader("TMVA_BDT_T1tttt_1750_1000");
   
	TString QCD_HT2000toInf_ext=inputFolder+"evVarFriend_QCD_HT2000toInf_ext.root";
	TFile *input_QCD_HT2000toInf_ext;
	input_QCD_HT2000toInf_ext=TFile::Open(QCD_HT2000toInf_ext);
	TTree *tree_QCD_HT2000toInf_ext=(TTree*)input_QCD_HT2000toInf_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_QCD_HT2000toInf_ext		,	1);
	TString QCD_HT1500to2000_ext=inputFolder+"evVarFriend_QCD_HT1500to2000_ext.root";
	TFile *input_QCD_HT1500to2000_ext;
	input_QCD_HT1500to2000_ext=TFile::Open(QCD_HT1500to2000_ext);
	TTree *tree_QCD_HT1500to2000_ext=(TTree*)input_QCD_HT1500to2000_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_QCD_HT1500to2000_ext		,	1);
	TString WJetsToLNu_HT400to600_ext=inputFolder+"evVarFriend_WJetsToLNu_HT400to600_ext.root";
	TFile *input_WJetsToLNu_HT400to600_ext;
	input_WJetsToLNu_HT400to600_ext=TFile::Open(WJetsToLNu_HT400to600_ext);
	TTree *tree_WJetsToLNu_HT400to600_ext=(TTree*)input_WJetsToLNu_HT400to600_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_WJetsToLNu_HT400to600_ext		,	1);
	TString QCD_HT300to500_ext=inputFolder+"evVarFriend_QCD_HT300to500_ext.root";
	TFile *input_QCD_HT300to500_ext;
	input_QCD_HT300to500_ext=TFile::Open(QCD_HT300to500_ext);
	TTree *tree_QCD_HT300to500_ext=(TTree*)input_QCD_HT300to500_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_QCD_HT300to500_ext		,	1);
	TString TTJets_SingleLeptonFromTbar_genMET=inputFolder+"evVarFriend_TTJets_SingleLeptonFromTbar_genMET.root";
	TFile *input_TTJets_SingleLeptonFromTbar_genMET;
	input_TTJets_SingleLeptonFromTbar_genMET=TFile::Open(TTJets_SingleLeptonFromTbar_genMET);
	TTree *tree_TTJets_SingleLeptonFromTbar_genMET=(TTree*)input_TTJets_SingleLeptonFromTbar_genMET->Get("sf/t");
	dataloader->AddBackgroundTree(tree_TTJets_SingleLeptonFromTbar_genMET		,	1);
	TString WJetsToLNu_HT1200to2500_ext=inputFolder+"evVarFriend_WJetsToLNu_HT1200to2500_ext.root";
	TFile *input_WJetsToLNu_HT1200to2500_ext;
	input_WJetsToLNu_HT1200to2500_ext=TFile::Open(WJetsToLNu_HT1200to2500_ext);
	TTree *tree_WJetsToLNu_HT1200to2500_ext=(TTree*)input_WJetsToLNu_HT1200to2500_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_WJetsToLNu_HT1200to2500_ext		,	1);
	TString TTJets_SingleLeptonFromT_ext=inputFolder+"evVarFriend_TTJets_SingleLeptonFromT_ext.root";
	TFile *input_TTJets_SingleLeptonFromT_ext;
	input_TTJets_SingleLeptonFromT_ext=TFile::Open(TTJets_SingleLeptonFromT_ext);
	TTree *tree_TTJets_SingleLeptonFromT_ext=(TTree*)input_TTJets_SingleLeptonFromT_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_TTJets_SingleLeptonFromT_ext		,	1);
	TString TTJets_DiLepton_ext=inputFolder+"evVarFriend_TTJets_DiLepton_ext.root";
	TFile *input_TTJets_DiLepton_ext;
	input_TTJets_DiLepton_ext=TFile::Open(TTJets_DiLepton_ext);
	TTree *tree_TTJets_DiLepton_ext=(TTree*)input_TTJets_DiLepton_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_TTJets_DiLepton_ext		,	1);
	TString TTJets_SingleLeptonFromT_genMET=inputFolder+"evVarFriend_TTJets_SingleLeptonFromT_genMET.root";
	TFile *input_TTJets_SingleLeptonFromT_genMET;
	input_TTJets_SingleLeptonFromT_genMET=TFile::Open(TTJets_SingleLeptonFromT_genMET);
	TTree *tree_TTJets_SingleLeptonFromT_genMET=(TTree*)input_TTJets_SingleLeptonFromT_genMET->Get("sf/t");
	dataloader->AddBackgroundTree(tree_TTJets_SingleLeptonFromT_genMET		,	1);
	TString WJetsToLNu_HT600to800_ext=inputFolder+"evVarFriend_WJetsToLNu_HT600to800_ext.root";
	TFile *input_WJetsToLNu_HT600to800_ext;
	input_WJetsToLNu_HT600to800_ext=TFile::Open(WJetsToLNu_HT600to800_ext);
	TTree *tree_WJetsToLNu_HT600to800_ext=(TTree*)input_WJetsToLNu_HT600to800_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_WJetsToLNu_HT600to800_ext		,	1);
	TString QCD_HT200to300_ext=inputFolder+"evVarFriend_QCD_HT200to300_ext.root";
	TFile *input_QCD_HT200to300_ext;
	input_QCD_HT200to300_ext=TFile::Open(QCD_HT200to300_ext);
	TTree *tree_QCD_HT200to300_ext=(TTree*)input_QCD_HT200to300_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_QCD_HT200to300_ext		,	1);
	TString DYJetsToLL_M50_HT200to400_ext=inputFolder+"evVarFriend_DYJetsToLL_M50_HT200to400_ext.root";
	TFile *input_DYJetsToLL_M50_HT200to400_ext;
	input_DYJetsToLL_M50_HT200to400_ext=TFile::Open(DYJetsToLL_M50_HT200to400_ext);
	TTree *tree_DYJetsToLL_M50_HT200to400_ext=(TTree*)input_DYJetsToLL_M50_HT200to400_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_DYJetsToLL_M50_HT200to400_ext		,	1);
	TString QCD_HT500to700_ext=inputFolder+"evVarFriend_QCD_HT500to700_ext.root";
	TFile *input_QCD_HT500to700_ext;
	input_QCD_HT500to700_ext=TFile::Open(QCD_HT500to700_ext);
	TTree *tree_QCD_HT500to700_ext=(TTree*)input_QCD_HT500to700_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_QCD_HT500to700_ext		,	1);
	TString WJetsToLNu_HT200to400_ext=inputFolder+"evVarFriend_WJetsToLNu_HT200to400_ext.root";
	TFile *input_WJetsToLNu_HT200to400_ext;
	input_WJetsToLNu_HT200to400_ext=TFile::Open(WJetsToLNu_HT200to400_ext);
	TTree *tree_WJetsToLNu_HT200to400_ext=(TTree*)input_WJetsToLNu_HT200to400_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_WJetsToLNu_HT200to400_ext		,	1);
	TString TTJets_SingleLeptonFromTbar_ext=inputFolder+"evVarFriend_TTJets_SingleLeptonFromTbar_ext.root";
	TFile *input_TTJets_SingleLeptonFromTbar_ext;
	input_TTJets_SingleLeptonFromTbar_ext=TFile::Open(TTJets_SingleLeptonFromTbar_ext);
	TTree *tree_TTJets_SingleLeptonFromTbar_ext=(TTree*)input_TTJets_SingleLeptonFromTbar_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_TTJets_SingleLeptonFromTbar_ext		,	1);
	TString TTJets_DiLepton_genMET=inputFolder+"evVarFriend_TTJets_DiLepton_genMET.root";
	TFile *input_TTJets_DiLepton_genMET;
	input_TTJets_DiLepton_genMET=TFile::Open(TTJets_DiLepton_genMET);
	TTree *tree_TTJets_DiLepton_genMET=(TTree*)input_TTJets_DiLepton_genMET->Get("sf/t");
	dataloader->AddBackgroundTree(tree_TTJets_DiLepton_genMET		,	1);
	TString DYJetsToLL_M50_HT400to600_ext=inputFolder+"evVarFriend_DYJetsToLL_M50_HT400to600_ext.root";
	TFile *input_DYJetsToLL_M50_HT400to600_ext;
	input_DYJetsToLL_M50_HT400to600_ext=TFile::Open(DYJetsToLL_M50_HT400to600_ext);
	TTree *tree_DYJetsToLL_M50_HT400to600_ext=(TTree*)input_DYJetsToLL_M50_HT400to600_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_DYJetsToLL_M50_HT400to600_ext		,	1);
	TString WJetsToLNu_HT200to400_ext2=inputFolder+"evVarFriend_WJetsToLNu_HT200to400_ext2.root";
	TFile *input_WJetsToLNu_HT200to400_ext2;
	input_WJetsToLNu_HT200to400_ext2=TFile::Open(WJetsToLNu_HT200to400_ext2);
	TTree *tree_WJetsToLNu_HT200to400_ext2=(TTree*)input_WJetsToLNu_HT200to400_ext2->Get("sf/t");
	dataloader->AddBackgroundTree(tree_WJetsToLNu_HT200to400_ext2		,	1);
	TString QCD_HT1000to1500_ext=inputFolder+"evVarFriend_QCD_HT1000to1500_ext.root";
	TFile *input_QCD_HT1000to1500_ext;
	input_QCD_HT1000to1500_ext=TFile::Open(QCD_HT1000to1500_ext);
	TTree *tree_QCD_HT1000to1500_ext=(TTree*)input_QCD_HT1000to1500_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_QCD_HT1000to1500_ext		,	1);
	TString DYJetsToLL_M50_HT100to200_ext=inputFolder+"evVarFriend_DYJetsToLL_M50_HT100to200_ext.root";
	TFile *input_DYJetsToLL_M50_HT100to200_ext;
	input_DYJetsToLL_M50_HT100to200_ext=TFile::Open(DYJetsToLL_M50_HT100to200_ext);
	TTree *tree_DYJetsToLL_M50_HT100to200_ext=(TTree*)input_DYJetsToLL_M50_HT100to200_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_DYJetsToLL_M50_HT100to200_ext		,	1);
	TString WJetsToLNu_HT800to1200_ext=inputFolder+"evVarFriend_WJetsToLNu_HT800to1200_ext.root";
	TFile *input_WJetsToLNu_HT800to1200_ext;
	input_WJetsToLNu_HT800to1200_ext=TFile::Open(WJetsToLNu_HT800to1200_ext);
	TTree *tree_WJetsToLNu_HT800to1200_ext=(TTree*)input_WJetsToLNu_HT800to1200_ext->Get("sf/t");
	dataloader->AddBackgroundTree(tree_WJetsToLNu_HT800to1200_ext		,	1);
   
   
   //dataloader->AddVariable("Lep_pdgId"       ,"Lep_pdgId"       ,"",'F');
   //dataloader->AddVariable("Lep_pt"          ,"Lep_pt"          ,"",'F');
   //dataloader->AddVariable("Lep_eta"         ,"Lep_eta"         ,"",'F');
   //dataloader->AddVariable("Lep_phi"         ,"Lep_phi"         ,"",'F');
   //dataloader->AddVariable("Lep_relIso"      ,"Lep_relIso"      ,"",'F');
   //dataloader->AddVariable("Lep_miniIso"     ,"Lep_miniIso"     ,"",'F');
   //dataloader->AddVariable("Lep2_pt"         ,"Lep2_pt"         ,"",'F');
   dataloader->AddVariable("MET"             ,"MET"             ,"",'F');
   dataloader->AddVariable("MT"              ,"MT"              ,"",'F');
   dataloader->AddVariable("dPhi"            ,"dPhi"            ,"",'F');
   dataloader->AddVariable("LT"              ,"LT"              ,"",'F');
   dataloader->AddVariable("HT"              ,"HT"              ,"",'F');
   dataloader->AddVariable("nJets30Clean"    ,"nJets30Clean"           ,"",'F');
   dataloader->AddVariable("nBJet"           ,"nBJet"           ,"",'F');
   //dataloader->AddVariable("Jet1_pt"         ,"Jet1_pt"         ,"",'F');
   //dataloader->AddVariable("Jet2_pt"         ,"Jet2_pt"         ,"",'F');
   //dataloader->AddVariable("nBJetDeep"       ,"nBJetDeep"       ,"",'F');
   //dataloader->AddVariable("FatJet1_pt"      ,"FatJet1_pt"      ,"",'F');
   //dataloader->AddVariable("FatJet2_pt"      ,"FatJet2_pt"      ,"",'F');
   //dataloader->AddVariable("FatJet1_eta"     ,"FatJet1_eta"     ,"",'F');
   //dataloader->AddVariable("FatJet2_eta"     ,"FatJet2_eta"     ,"",'F');
   //dataloader->AddVariable("FatJet1_phi"     ,"FatJet1_phi"     ,"",'F');
   //dataloader->AddVariable("FatJet2_phi"     ,"FatJet2_phi"     ,"",'F');
   //dataloader->AddVariable("FatJet1_mass"    ,"FatJet1_mass"    ,"",'F');
   //dataloader->AddVariable("FatJet2_mass"    ,"FatJet2_mass"    ,"",'F');
   //dataloader->AddVariable("nDeepTop_medium" ,"nDeepTop_medium" ,"",'F');
   //dataloader->AddVariable("nDeepTop_tight"  ,"nDeepTop_tight"  ,
	//dataloader->AddVariable("nDeepTop_loose"  ,"nDeepTop_loose"  ,
	
	TString SMS_T1tttt_TuneCUETP8M1_2="2016_Sig_Training/evVarFriend_SMS_T1tttt_TuneCUETP8M1_1750_1000.root";
	TFile *input_SMS_T1tttt_TuneCUETP8M1_2;
	input_SMS_T1tttt_TuneCUETP8M1_2=TFile::Open(SMS_T1tttt_TuneCUETP8M1_2);
	TTree *tree_SMS_T1tttt_TuneCUETP8M1_2=(TTree*)input_SMS_T1tttt_TuneCUETP8M1_2->Get("sf/t");
	//dataloader->AddSignalTree    ( tree_SMS_T1tttt_TuneCUETP8M1_1,     0.00359842);
	dataloader->AddSignalTree    ( tree_SMS_T1tttt_TuneCUETP8M1_2,     1);
	/*dataloader->AddSignalTree    ( tree_SMS_T1tttt_TuneCUETP8M1_3,     3754923);
	dataloader->AddSignalTree    ( tree_SMS_T1tttt_TuneCUETP8M1_4,     3760043);
	dataloader->AddSignalTree    ( tree_SMS_T1tttt_TuneCUETP8M1_5,     4287118);
	dataloader->AddSignalTree    ( tree_SMS_T1tttt_TuneCUETP8M1_6,     3963362);*/
	

	  //0.00359842 1750
	  //0.00212345 1850
   // Set individual event weights (the variables must exist in the original TTree)
   // -  for signal    : `dataloader->SetSignalWeightExpression    ("weight1*weight2");`
   // -  for background: `dataloader->SetBackgroundWeightExpression("weight1*weight2");`
   dataloader->SetBackgroundWeightExpression( "Xsec" );
   dataloader->SetSignalWeightExpression( "0.00359842" );
   //     factory->SetBackgroundWeightExpression("weight");
   TCut mycuts = "nLep == 1 && Lep_pt > 25 && Selected == 1 &&  nVeto == 0 && nJets30Clean >= 5 && Jet2_pt > 80 &&  HT > 500 && LT > 250 "; // for example: TCut mycuts = "abs(var1)<0.5 && abs(var2-0.5)<1";
   TCut mycutb = "nLep == 1 && Lep_pt > 25 && Selected == 1 &&  nVeto == 0 && nJets30Clean >= 5 && Jet2_pt > 80 &&  HT > 500 && LT > 250"; // for example: TCut mycutb = "abs(var1)<0.5";

   // tell the factory to use all remaining events in the trees after training for testing:
   // dataloader->PrepareTrainingAndTestTree( mycuts, mycutb,
   //                                     "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" );
   dataloader->PrepareTrainingAndTestTree( mycuts, mycutb,
                                        "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" );
   
   // Cut optimisation
   if (Use["Cuts"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "Cuts",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" );

   if (Use["CutsD"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsD",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=Decorrelate" );

   if (Use["CutsPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsPCA",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=PCA" );

   if (Use["CutsGA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsGA",
                           "H:!V:FitMethod=GA:CutRangeMin[0]=-10:CutRangeMax[0]=10:VarProp[1]=FMax:EffSel:Steps=30:Cycles=3:PopSize=400:SC_steps=10:SC_rate=5:SC_factor=0.95" );

   if (Use["CutsSA"])
      factory->BookMethod( dataloader, TMVA::Types::kCuts, "CutsSA",
                           "!H:!V:FitMethod=SA:EffSel:MaxCalls=150000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

   // Likelihood ("naive Bayes estimator")
   if (Use["Likelihood"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "Likelihood",
                           "H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50" );

   // Decorrelated likelihood
   if (Use["LikelihoodD"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodD",
                           "!H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" );

   // PCA-transformed likelihood
   if (Use["LikelihoodPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodPCA",
                           "!H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=PCA" );

   // Use a kernel density estimator to approximate the PDFs
   if (Use["LikelihoodKDE"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodKDE",
                           "!H:!V:!TransformOutput:PDFInterpol=KDE:KDEtype=Gauss:KDEiter=Adaptive:KDEFineFactor=0.3:KDEborder=None:NAvEvtPerBin=50" );

   // Use a variable-dependent mix of splines and kernel density estimator
   if (Use["LikelihoodMIX"])
      factory->BookMethod( dataloader, TMVA::Types::kLikelihood, "LikelihoodMIX",
                           "!H:!V:!TransformOutput:PDFInterpolSig[0]=KDE:PDFInterpolBkg[0]=KDE:PDFInterpolSig[1]=KDE:PDFInterpolBkg[1]=KDE:PDFInterpolSig[2]=Spline2:PDFInterpolBkg[2]=Spline2:PDFInterpolSig[3]=Spline2:PDFInterpolBkg[3]=Spline2:KDEtype=Gauss:KDEiter=Nonadaptive:KDEborder=None:NAvEvtPerBin=50" );

   // Test the multi-dimensional probability density estimator
   // here are the options strings for the MinMax and RMS methods, respectively:
   //
   //      "!H:!V:VolumeRangeMode=MinMax:DeltaFrac=0.2:KernelEstimator=Gauss:GaussSigma=0.3" );
   //      "!H:!V:VolumeRangeMode=RMS:DeltaFrac=3:KernelEstimator=Gauss:GaussSigma=0.3" );
   if (Use["PDERS"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERS",
                           "!H:!V:NormTree=T:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600" );

   if (Use["PDERSD"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERSD",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=Decorrelate" );

   if (Use["PDERSPCA"])
      factory->BookMethod( dataloader, TMVA::Types::kPDERS, "PDERSPCA",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=PCA" );

   // Multi-dimensional likelihood estimator using self-adapting phase-space binning
   if (Use["PDEFoam"])
      factory->BookMethod( dataloader, TMVA::Types::kPDEFoam, "PDEFoam",
                           "!H:!V:SigBgSeparate=F:TailCut=0.001:VolFrac=0.0666:nActiveCells=500:nSampl=2000:nBin=5:Nmin=100:Kernel=None:Compress=T" );

   if (Use["PDEFoamBoost"])
      factory->BookMethod( dataloader, TMVA::Types::kPDEFoam, "PDEFoamBoost",
                           "!H:!V:Boost_Num=30:Boost_Transform=linear:SigBgSeparate=F:MaxDepth=4:UseYesNoCell=T:DTLogic=MisClassificationError:FillFoamWithOrigWeights=F:TailCut=0:nActiveCells=500:nBin=20:Nmin=400:Kernel=None:Compress=T" );

   // K-Nearest Neighbour classifier (KNN)
   if (Use["KNN"])
      factory->BookMethod( dataloader, TMVA::Types::kKNN, "KNN",
                           "H:nkNN=20:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:UseWeight=T:!Trim" );

   // H-Matrix (chi2-squared) method
   if (Use["HMatrix"])
      factory->BookMethod( dataloader, TMVA::Types::kHMatrix, "HMatrix", "!H:!V:VarTransform=None" );

   // Linear discriminant (same as Fisher discriminant)
   if (Use["LD"])
      factory->BookMethod( dataloader, TMVA::Types::kLD, "LD", "H:!V:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

   // Fisher discriminant (same as LD)
   if (Use["Fisher"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "Fisher", "H:!V:Fisher:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

   // Fisher with Gauss-transformed input variables
   if (Use["FisherG"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "FisherG", "H:!V:VarTransform=Gauss" );

   // Composite classifier: ensemble (tree) of boosted Fisher classifiers
   if (Use["BoostedFisher"])
      factory->BookMethod( dataloader, TMVA::Types::kFisher, "BoostedFisher",
                           "H:!V:Boost_Num=20:Boost_Transform=log:Boost_Type=AdaBoost:Boost_AdaBoostBeta=0.2:!Boost_DetailedMonitoring" );

   // Function discrimination analysis (FDA) -- test of various fitters - the recommended one is Minuit (or GA or SA)
   if (Use["FDA_MC"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MC",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:SampleSize=100000:Sigma=0.1" );

   if (Use["FDA_GA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_GA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:PopSize=100:Cycles=2:Steps=5:Trim=True:SaveBestGen=1" );

   if (Use["FDA_SA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_SA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=SA:MaxCalls=15000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

   if (Use["FDA_MT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=2:UseImprove:UseMinos:SetBatch" );

   if (Use["FDA_GAMT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_GAMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:Cycles=1:PopSize=5:Steps=5:Trim" );

   if (Use["FDA_MCMT"])
      factory->BookMethod( dataloader, TMVA::Types::kFDA, "FDA_MCMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:SampleSize=20" );

   // TMVA ANN: MLP (recommended ANN) -- all ANNs in TMVA are Multilayer Perceptrons
   if (Use["MLP"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator" );

   if (Use["MLPBFGS"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLPBFGS", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );

   if (Use["MLPBNN"])
      factory->BookMethod( dataloader, TMVA::Types::kMLP, "MLPBNN", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=60:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators


   // Multi-architecture DNN implementation.
   if (Use["DNN_CPU"] or Use["DNN_GPU"]) {
      // General layout.
      TString layoutString ("Layout=TANH|128,TANH|128,TANH|128,LINEAR");

      // Training strategies.
      TString training0("LearningRate=1e-1,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=20,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.5+0.5+0.5, Multithreading=True");
      TString training1("LearningRate=1e-2,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=20,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.0+0.0+0.0, Multithreading=True");
      TString training2("LearningRate=1e-3,Momentum=0.0,Repetitions=1,"
                        "ConvergenceSteps=20,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.0+0.0+0.0, Multithreading=True");
      TString trainingStrategyString ("TrainingStrategy=");
      trainingStrategyString += training0 + "|" + training1 + "|" + training2;

      // General Options.
      TString dnnOptions ("!H:V:ErrorStrategy=CROSSENTROPY:VarTransform=N:"
                          "WeightInitialization=XAVIERUNIFORM");
      dnnOptions.Append (":"); dnnOptions.Append (layoutString);
      dnnOptions.Append (":"); dnnOptions.Append (trainingStrategyString);

      // Cuda implementation.
      if (Use["DNN_GPU"]) {
         TString gpuOptions = dnnOptions + ":Architecture=GPU";
         factory->BookMethod(dataloader, TMVA::Types::kDNN, "DNN_GPU", gpuOptions);
      }
      // Multi-core CPU implementation.
      if (Use["DNN_CPU"]) {
         TString cpuOptions = dnnOptions + ":Architecture=CPU";
         factory->BookMethod(dataloader, TMVA::Types::kDNN, "DNN_CPU", cpuOptions);
      }
   }

   // CF(Clermont-Ferrand)ANN
   if (Use["CFMlpANN"])
      factory->BookMethod( dataloader, TMVA::Types::kCFMlpANN, "CFMlpANN", "!H:!V:NCycles=200:HiddenLayers=N+1,N"  ); // n_cycles:#nodes:#nodes:...

   // Tmlp(Root)ANN
   if (Use["TMlpANN"])
      factory->BookMethod( dataloader, TMVA::Types::kTMlpANN, "TMlpANN", "!H:!V:NCycles=200:HiddenLayers=N+1,N:LearningMethod=BFGS:ValidationFraction=0.3"  ); // n_cycles:#nodes:#nodes:...

   // Support Vector Machine
   if (Use["SVM"])
      factory->BookMethod( dataloader, TMVA::Types::kSVM, "SVM", "Gamma=0.25:Tol=0.001:VarTransform=Norm" );

   // Boosted Decision Trees
   if (Use["BDTG"]) // Gradient Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTG",
                           "!H:!V:NTrees=1000:MinNodeSize=2.5%:BoostType=Grad:Shrinkage=0.10:UseBaggedBoost:BaggedSampleFraction=0.5:nCuts=20:MaxDepth=2" );

   if (Use["BDT"])  // Adaptive Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDT",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTB"]) // Bagging
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTB",
                           "!H:!V:NTrees=400:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTD"]) // Decorrelation + Adaptive Boost
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTD",
                           "!H:!V:NTrees=400:MinNodeSize=5%:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:VarTransform=Decorrelate" );

   if (Use["BDTF"])  // Allow Using Fisher discriminant in node splitting for (strong) linearly correlated variables
      factory->BookMethod( dataloader, TMVA::Types::kBDT, "BDTF",
                           "!H:!V:NTrees=50:MinNodeSize=2.5%:UseFisherCuts:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:SeparationType=GiniIndex:nCuts=20" );

   // RuleFit -- TMVA implementation of Friedman's method
   if (Use["RuleFit"])
      factory->BookMethod( dataloader, TMVA::Types::kRuleFit, "RuleFit",
                           "H:!V:RuleFitModule=RFTMVA:Model=ModRuleLinear:MinImp=0.001:RuleMinDist=0.001:NTrees=20:fEventsMin=0.01:fEventsMax=0.5:GDTau=-1.0:GDTauPrec=0.01:GDStep=0.01:GDNSteps=10000:GDErrScale=1.02" );
   if (Use["RXGB"])
      factory->BookMethod( dataloader, TMVA::Types::kRXGB, "RXGB",
                           "!V:NRounds=80:MaxDepth=2:Eta=1");
   
   
   
   
      // For an example of the category classifier usage, see: TMVAClassificationCategory
   //
   // --------------------------------------------------------------------------------------------------
   //  Now you can optimize the setting (configuration) of the MVAs using the set of training events
   // STILL EXPERIMENTAL and only implemented for BDT's !
   //
   //     factory->OptimizeAllMethods("SigEffAt001","Scan");
   //     factory->OptimizeAllMethods("ROCIntegral","FitGA");
   //
   // --------------------------------------------------------------------------------------------------

   // Now you can tell the factory to train, test, and evaluate the MVAs
   //
   // Train MVAs using the set of training events
   factory->TrainAllMethods();

   // Evaluate all MVAs using the set of test events
   factory->TestAllMethods();

   // Evaluate and compare performance of all configured MVAs
   factory->EvaluateAllMethods();

   // --------------------------------------------------------------


   outputFile->Close();

   std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
   std::cout << "==> TMVAClassification is done!" << std::endl;

   delete factory;
   delete dataloader;
   // Launch the GUI for the root macros
   if (!gROOT->IsBatch()) TMVA::TMVAGui( outfileName );

   return 0;
}


int main( int argc, char** argv )
{
   // Select methods (don't look at this code - not of interest)
   TString methodList;
   for (int i=1; i<argc; i++) {
      TString regMethod(argv[i]);
      if(regMethod=="-b" || regMethod=="--batch") continue;
      if (!methodList.IsNull()) methodList += TString(",");
      methodList += regMethod;
   }
   return TMVA_1lep_CMG_v6_LWt01(methodList);
}


