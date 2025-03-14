#include "PhysicsTools/NanoAOD/interface/SimpleFlatTableProducer.h"


#include "DataFormats/L1TMuonPhase2/interface/Tau23Mu.h"
typedef SimpleFlatTableProducer<l1t::Tau23Mu> SimpleTriggerL1Tau23MuFlatTableProducer;

#include "DataFormats/L1TMuonPhase2/interface/EMTFHit.h"
typedef SimpleFlatTableProducer<l1t::phase2::EMTFHit> SimpleEMTFHitCandidateFlatTableProducer;

#include "DataFormats/L1TMuonPhase2/interface/EMTFTrack.h"
typedef SimpleFlatTableProducer<l1t::phase2::EMTFTrack> SimpleEMTFTrackCandidateFlatTableProducer;

#include "DataFormats/L1TMuon/interface/RegionalMuonCand.h"
typedef BXVectorSimpleFlatTableProducer<l1t::RegionalMuonCand> SimpleOMTFTrackCandidateFlatTableProducer;

#include "DataFormats/L1TMuonPhase2/interface/MuonStub.h"
typedef SimpleFlatTableProducer<l1t::MuonStub> SimpleMuonStubFlatTableProducer;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SimpleTriggerL1Tau23MuFlatTableProducer);
DEFINE_FWK_MODULE(SimpleEMTFHitCandidateFlatTableProducer);
DEFINE_FWK_MODULE(SimpleEMTFTrackCandidateFlatTableProducer);
DEFINE_FWK_MODULE(SimpleOMTFTrackCandidateFlatTableProducer);
DEFINE_FWK_MODULE(SimpleMuonStubFlatTableProducer);
