import json
from typing import Dict, Any, Optional
import requests

class EventManager:
    def __init__(self, data_sources: list):
        """
        Initialize event manager with external data sources
        
        :param data_sources: List of APIs/sources for event data
        """
        self.data_sources = data_sources
        self.events: Dict[int, Dict[str, Any]] = {}
    
    def fetch_event_outcomes(self, event_id: int) -> Optional[int]:
        """
        Resolve event outcomes by querying multiple data sources
        
        :param event_id: Unique identifier for the event
        :return: Resolved outcome or None
        """
        outcomes = []
        for source in self.data_sources:
            try:
                response = requests.get(f"{source}/events/{event_id}")
                data = response.json()
                outcomes.append(data.get('outcome'))
            except Exception as e:
                print(f"Error fetching from {source}: {e}")
        
        # Basic consensus mechanism
        if len(set(outcomes)) == 1:
            return outcomes[0]
        return None

class OutcomeResolver:
    @staticmethod
    def calculate_payouts(event_data: Dict, predictions: list) -> list:
        """
        Calculate payouts for correct predictions
        
        :param event_data: Event details including resolved outcome
        :param predictions: List of user predictions
        :return: List of payouts
        """
        correct_predictions = [
            pred for pred in predictions 
            if pred['prediction'] == event_data['outcome']
        ]
        
        total_correct_stake = sum(pred['bet_amount'] for pred in correct_predictions)
        total_event_pool = event_data['total_pool']
        
        payouts = []
        for pred in correct_predictions:
            payout = (pred['bet_amount'] / total_correct_stake) * total_event_pool
            payouts.append({
                'user': pred['user'],
                'amount': payout
            })
        
        return payouts