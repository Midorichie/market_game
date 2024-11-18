import requests
from typing import Dict, Any
from web3 import Web3
from stacks import StacksClient

class DecentralizedOracle:
    def __init__(self, data_sources: List[str]):
        self.data_sources = data_sources
        self.stake_threshold = 0.7  # Consensus threshold
        self.reputation_scores = {}

    def validate_outcome(self, event_id: str) -> Dict[str, Any]:
        """
        Multi-source outcome validation with reputation-weighted consensus
        """
        outcomes = {}
        for source in self.data_sources:
            try:
                response = self._fetch_outcome(source, event_id)
                outcomes[source] = response
                self._update_reputation(source, response['reliability'])
            except Exception as e:
                print(f"Source {source} failed: {e}")

        # Implement weighted consensus mechanism
        consensus_outcome = self._calculate_consensus(outcomes)
        return consensus_outcome

    def _calculate_consensus(self, outcomes: Dict) -> Dict:
        """
        Calculate consensus with reputation-weighted voting
        """
        weighted_outcomes = {}
        for source, outcome in outcomes.items():
            reputation = self.reputation_scores.get(source, 1.0)
            weighted_outcomes[outcome] = weighted_outcomes.get(outcome, 0) + reputation

        return max(weighted_outcomes, key=weighted_outcomes.get)