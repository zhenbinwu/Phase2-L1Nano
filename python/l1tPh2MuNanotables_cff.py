import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.NanoAOD.l1trig_cff import *

# #### GTT Vertex
from PhysicsTools.L1Nano.l1tPh2Nanotables_cff import vtxTable,  pvtxTable

### Muons
EMTFHitTable = cms.EDProducer( "SimpleEMTFHitCandidateFlatTableProducer",
                              src = cms.InputTag('simEmtfDigisPhase2'),
                              name = cms.string("emtfhit"),
                              doc = cms.string("testing"),
                              cut = cms.string("bx()==0"),
                              singleton = cms.bool(False), # the number of entries is variable
                              variables = cms.PSet(
                                # bx = Var("bx()", "int16"), 
                                chamber = Var("emtfChamber()", "int16"),
                                segment = Var("emtfSegment()", "int16"),
                                phi = Var("emtfPhi()", "int16"),
                                bend = Var("emtfBend()", "int16"),
                                theta1 = Var("emtfTheta1()", "int16"),
                                theta2 = Var("emtfTheta2()", "int16"),
                                qual1 = Var("emtfQual1()", "int16"),
                                qual2 = Var("emtfQual2()", "int16"),
                                time = Var("emtfTime()", "int16"),
                                site = Var("emtfSite()", "int16"),
                                host = Var("emtfHost()", "int16"),
                                zones = Var("emtfZones()", "int16"),
                                timezones = Var("emtfTimezones()", "int16"),
                                globPhi = Var("globPhi()", float, precision=8),
                                globTheta = Var("globTheta()", float, precision=8),
                                globPerp = Var("globPerp()", float, precision=8),
                              )
                             )

EMTFTrackTable = cms.EDProducer( "SimpleEMTFTrackCandidateFlatTableProducer",
                                src = cms.InputTag('simEmtfDigisPhase2'),
                                name = cms.string("emtf"),
                                doc = cms.string("EMTF Track"),
                                cut = cms.string("bx()==0"),
                                singleton = cms.bool(False), # the number of entries is variable
                                variables = cms.PSet(
                                  # bx = Var("bx()", "int16"), 
                                  endcap = Var("endcap()", "int16"), 
                                  sector = Var("sector()", "int16"), 
                                  Q = Var("emtfQ()", "int16"),
                                  qual = Var("modelQual()", "int16"), 
                                  phi = Var("modelPhi()",int), 
                                  eta = Var("modelEta()", int), 
                                  pt = Var("emtfPt()", int), 
                                  d0 =  Var("emtfD0()", int), 
                                  z0 =  Var("emtfZ0()", int), 
                                  beta =  Var("emtfBeta()", int), 
                                )
                               )

OMTFTrackTable = cms.EDProducer( "SimpleOMTFTrackCandidateFlatTableProducer",
                                src = cms.InputTag('simOmtfPhase2Digis', 'OMTF'),
                                minBX = cms.int32(0),
                                maxBX = cms.int32(0),                           
                                name = cms.string("omtf"),
                                doc = cms.string("OMTF Track"),
                                cut = cms.string(""),
                                extension = cms.bool(False), 
                                variables = cms.PSet(
                                  ## hw Values
                                  Q = Var("hwSign()", "int16"),
                                  hwPt = Var("hwPt()","int16",doc="hardware pt"),
                                  hwPtUnc = Var("hwPtUnconstrained()","int16",doc="hardware pt"),
                                  hwDXY = Var("hwDXY()","int16",doc="hardware beta"),
                                  hwEta = Var("hwEta()","int16",doc="hardware eta"),
                                  hwPhi = Var("hwPhi()","int16",doc="hardware phi"),
                                  hwQual = Var("hwQual()","int16",doc="hardware qual"),
                                  muIdx = Var("muIdx()", "int16", doc="muon index (i.e., 0, 1, or 2) "),
                                  processor = Var("processor()", "int16", doc="(0..5 for OMTF/EMTF; 0..11 for BMTF)"),
                                )
                               )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GMT ~~~~~
### common variables set (pt/eta/phi)
l1MuObjVars = cms.PSet(
        # l1ObjVars,
        ### WARNING : the pt/eta/phi/vz methods give rounded results -> use the "physical" accessors
        # vz = Var("vz",float),
        chargeNoPh = Var("charge", int, doc="charge id"),

        ## physical values
        charge  = Var("phCharge", int, doc="charge id"),
        pt  = Var("phPt()",float, precision=8),
        eta = Var("phEta()",float, precision=8),
        phi = Var("phPhi()",float, precision=8),
        z0 = Var("phZ0()",float, precision=8),
        d0 = Var("phD0()",float, precision=8),
        # beta = Var("phBeta()",float), # does not exist

        ## hw Values
        hwPt = Var("hwPt()","int16",doc="hardware pt"),
        hwEta = Var("hwEta()","int16",doc="hardware eta"),
        hwPhi = Var("hwPhi()","int16",doc="hardware phi"),
        hwQual = Var("hwQual()","int16",doc="hardware qual"),
        hwBeta = Var("hwBeta()","int16",doc="hardware beta"),

)

SAPromptMuTable = cms.EDProducer( "SimpleCandidateFlatTableProducer",
    src = cms.InputTag('l1tSAMuonsGmt','promptSAMuons'),
    name = cms.string("samu"),
    doc = cms.string("GMT standalone Muons, origin: GMT"),
    cut = cms.string(""),
    singleton = cms.bool(False), # the number of entries is variable
    variables = cms.PSet(
      l1MuObjVars
        # ## more info
        # nStubs = Var("stubs().size()",int,doc="number of stubs"),
    )
)


SADisplacedMuTable = SAPromptMuTable.clone(
    src = cms.InputTag("l1tSAMuonsGmt", "displacedSAMuons"),
    name = cms.string("dismu"),
    doc = cms.string("GMT standalone displaced Muons, origin: GMT"),
)


TkMuTable = SAPromptMuTable.clone(
    src = cms.InputTag('l1tTkMuonsGmt'),
    name = cms.string("tkmu"),
    doc = cms.string("GMT Tk Muons, origin: GMT"),
    variables = cms.PSet(
      l1MuObjVars,
      hwIso = Var("hwIso()",int,doc="hardware iso"),
    )
)

## L1 Objects
p2L1MuTablesTask = cms.Task(
  ## EMTF
  EMTFHitTable,
  EMTFTrackTable,
  OMTFTrackTable,
  ## Muons
  TkMuTable,
  SAPromptMuTable, 
  SADisplacedMuTable, 
  # # GTT
  vtxTable,
  pvtxTable
)

