import os

data_Spring23= {
  'DYToLL'       : '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v3/GEN-SIM-DIGI-RAW-MINIAOD',
  'DYToLL2' : '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD', 
  'DsToTauTo3Mu' : '/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'MinBias'      : '/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9_ext1-v2/GEN-SIM-DIGI-RAW-MINIAOD',
  'MinBias2' :       '/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  # 'H24mu_900'         : '/HTo2LongLivedTo4mu_MH-125_MFF-12_CTau-900mm_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v2/GEN-SIM-DIGI-RAW-MINIAOD',
  # "H24mu_100"    : '/HTo2LongLivedTo4mu_MH-125_MFF-50_CTau-10000mm_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  # 'Mu_0to200'    : '/SingleMuon_Pt-0To200_Eta-1p4To3p1-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  # 'Mu_to500'     : '/SingleMuon_Pt-200To500_Eta-1p4To3p1-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  # 'TTTo2L2Nu'    : '/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  # 'GNN'          : '/DSTau3Mu_pCut1_14TeV_Pythia8/jschulte-PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2_GEN-SIM-DIGI-RAW_part3-v1-0b09b1d51eb1b176460746cc4e457a22/USER'
}

data_Fall22= {
  'H24Mu_12_10k'  : '/HTo2LongLivedTo4mu_MH-125_MFF-12_CTau-10000mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'H24Mu_50_10k'  : '/HTo2LongLivedTo4mu_MH-125_MFF-50_CTau-10000mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'H24Mu_25_10k'  : '/HTo2LongLivedTo4mu_MH-125_MFF-25_CTau-10000mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'H24Mu_12_900'  : '/HTo2LongLivedTo4mu_MH-125_MFF-12_CTau-900mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'H24Mu_25_1500' : '/HTo2LongLivedTo4mu_MH-125_MFF-25_CTau-1500mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'H24Mu_25_10k'  : '/HTo2LongLivedTo4mu_MH-125_MFF-25_CTau-10000mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  'H24Mu_50_3k'   : '/HTo2LongLivedTo4mu_MH-125_MFF-50_CTau-3000mm_TuneCP5_14TeV-pythia8/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  "DispMu_10"     : '/DisplacedMuons_Pt-10To30_Dxy-0To3000-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  "DispMu_2"      : '/DisplacedMuons_Pt-2To10_Dxy-0To3000-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
  "DispMu_30"     : '/DisplacedMuons_Pt-30To100_Dxy-0To3000-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
}

# for tag,dataset in  data_Fall22.iteritems():
for tag,dataset in  data_Spring23.items():
    FILE="""
from CRABClient.UserUtilities import config
config = config()
config.General.requestName = 'skim_{tag}'
config.General.workArea = 'crab_projects_Tau_v0'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'rerunL1_cfg.py'
config.Data.inputDataset = '{dataset}'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 4
config.Data.outLFNDirBase = '/store/group/lpctrig/benwu/GMT_Nano/Tau23Mu/v1_noTPS/'
config.Data.publication = False
config.Data.ignoreLocality = True
config.Data.outputDatasetTag = 'PHASEII_{tag}'
config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.whitelist = ['T2_US_*']
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000
""".format(tag=tag,dataset=dataset)
    f=open("crab_{tag}.py".format(tag=tag),"w")
    print(FILE)
    f.write(FILE)
    f.close()
    os.system("crab submit -c crab_{PT}.py".format(PT=tag))
