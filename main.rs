use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Serialize, Deserialize)]
struct Event {
    id: u64,
    description: String,
    categories: Vec<String>,
    status: EventStatus,
}

#[derive(Debug, Serialize, Deserialize)]
enum EventStatus {
    Open,
    Closed,
    Resolved,
}

#[derive(Debug)]
struct PredictionEngine {
    events: HashMap<u64, Event>,
    user_predictions: HashMap<(u64, String), Prediction>,
}

#[derive(Debug, Serialize, Deserialize)]
struct Prediction {
    user_id: String,
    event_id: u64,
    prediction_value: f64,
    stake: f64,
}

impl PredictionEngine {
    fn new() -> Self {
        PredictionEngine {
            events: HashMap::new(),
            user_predictions: HashMap::new(),
        }
    }

    fn create_event(&mut self, event: Event) {
        self.events.insert(event.id, event);
    }

    fn place_prediction(&mut self, prediction: Prediction) -> Result<(), String> {
        let event = self.events.get(&prediction.event_id)
            .ok_or_else(|| "Event not found".to_string())?;

        if event.status != EventStatus::Open {
            return Err("Event is not open for predictions".to_string());
        }

        self.user_predictions.insert(
            (prediction.event_id, prediction.user_id.clone()), 
            prediction
        );

        Ok(())
    }
}

fn main() {
    let mut engine = PredictionEngine::new();
    
    // Example usage
    let sports_event = Event {
        id: 1,
        description: "NBA Championship Finals".to_string(),
        categories: vec!["Sports".to_string()],
        status: EventStatus::Open,
    };

    engine.create_event(sports_event);
}