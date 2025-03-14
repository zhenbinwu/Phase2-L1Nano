# Phase2-L1Nano
NanoAOD ntupler for Phase-2 L1 Muon Objects

## Setup

The Phase2 L1Nano is merged into CMSSW. This code extend the Phase2 L1Nano to
include more muon information for study.

```bash
cmsrel CMSSW_15_1_0_pre1
cd CMSSW_15_1_0_pre1/src/
cmsenv
git cms-init

### ADDING NANO
git clone git@github.com:zhenbinwu/Phase2-L1Nano.git PhysicsTools/L1Nano
scram b -j 8
```

## Usage (To be updated)

### Via cmsDriver

One can append the L1Nano output to the `cmsDriver` command via this customisation: 
```bash
--eventcontent NANOAOD -s USER:PhysicsTools/L1Nano/l1tPh2Nano_cff.l1tPh2NanoTask --customise PhysicsTools/L1Nano/l1tPh2MuNano_cff.addFullPh2L1Nano
```

`cmsDriver` command (NO Track Trigger, based on [the 1400pre3 recipe from the Offline SW twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TPhase2Instructions#Recipe_for_phase2_l1t_1400pre3_v9):
```bash
cmsDriver.py step1 --conditions 131X_mcRun4_realistic_v9 -n 1000 --era Phase2C17I13M9 --eventcontent NANOAOD -s RAW2DIGI,L1,L1P2GT,USER:PhysicsTools/L1Nano/l1tPh2Nano_cff.l1tPh2NanoTask --customise PhysicsTools/L1Nano/l1tPh2Nano_cff.addFullPh2L1Nano --datatier GEN-SIM-DIGI-RAW-MINIAOD --fileout file:test.root --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2.addHcalTriggerPrimitives --geometry Extended2026D95 --nThreads 8 --filein /store/mc/Phase2Spring23DIGIRECOMiniAOD/TT_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/PU200_L1TFix_Trk1GeV_131X_mcRun4_realistic_v9-v1/50000/005bc30b-cf79-4b3b-9ec1-a80e13072afd.root --mc --inputCommands="keep *, drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt_*_*" --outputCommands="drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt_*_*" 
```


## Output

The output file is a nanoAOD file with the output branches in the `Events` tree.

An overview of the corresponding content is shown here: https://alobanov.web.cern.ch/L1T/Phase2/L1Nano/l1menu_nano_V38_1400pre3V9_doc_report.html

Size report: https://alobanov.web.cern.ch/L1T/Phase2/L1Nano/l1menu_nano_V38_1400pre3V9_size_report.html

Example:

```python
['run',
 'luminosityBlock',
 'event',
 'bunchCrossing',
 'nL1caloJet',
 'L1caloJet_et',
 'L1caloJet_eta',
 'L1caloJet_phi',
 'L1caloJet_pt',
 'L1caloJet_z0',
 'nL1caloTau',
 'L1caloTau_eta',
 'L1caloTau_phi',
 'L1caloTau_pt',
 'nGenJet',
 'GenJet_eta',
 'GenJet_mass',
 ...
```

This can be easily handled with [`uproot/awkward`](https://gitlab.cern.ch/cms-podas23/dpg/trigger-exercise/-/blob/solutions/1_Intro_NanoAwk_Analysis_Solution.ipynb) like this:

```python
f = uproot.open("l1nano.root")
events = f["Events"].arrays() 
```
