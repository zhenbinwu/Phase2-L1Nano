import os

data_Spring23= {
    'DYToLL'         : '/DYToLL_M-50_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v3/GEN-SIM-DIGI-RAW-MINIAOD',
    'DsToTauTo3Mu'   : '/DsToTauTo3Mu_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD',
    'MinBias'        : '/MinBias_TuneCP5_14TeV-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9_ext1-v2/GEN-SIM-DIGI-RAW-MINIAOD',
    # 'Mu_0to200'      : '/SingleMuon_Pt-0To200_Eta-1p4To3p1-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
    # 'Mu_to500'       : '/SingleMuon_Pt-200To500_Eta-1p4To3p1-gun/Phase2Fall22DRMiniAOD-PU200_125X_mcRun4_realistic_v2-v1/GEN-SIM-DIGI-RAW-MINIAOD',
    'TTTo2L2Nu'      : '/TTTo2L2Nu_TuneCP5_14TeV-powheg-pythia8/Phase2Spring23DIGIRECOMiniAOD-PU200_Trk1GeV_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD',
    # 'GNN' : '/DSTau3Mu_pCut1_14TeV_Pythia8/jschulte-PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2_GEN-SIM-DIGI-RAW_part3-v1-0b09b1d51eb1b176460746cc4e457a22/USER'
}


for tag,dataset in  data_Spring23.iteritems():
    FILE="""
from CRABClient.UserUtilities import config
config = config()
config.General.requestName = 'skim_{tag}'
config.General.workArea = 'crab_projects_Spring_v0'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'v33_rerunL1MuwTT_cfg.py'
config.Data.inputDataset = '{dataset}'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/group/lpctrig/benwu/GMT_Nano/Spring23_GMTv2_v0'
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


