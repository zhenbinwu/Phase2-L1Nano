import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.nano_cff import nanoMetadata
from PhysicsTools.L1Nano.l1tPh2MuNanotables_cff import *

def addPh2L1MuonObjects(process):
    process.l1tPh2NanoTask.add(p2L1MuTablesTask)
    return process

