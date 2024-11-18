;; Prediction Market Smart Contract

(define-map predictions 
  { event-id: uint, user: principal }
  { prediction: uint, bet-amount: uint, claimed: bool }
)

(define-map events
  { event-id: uint }
  { description: (string-utf8 256), 
    outcome: (optional uint), 
    resolved: bool, 
    total-pool: uint }
)

;; Create a new prediction event
(define-public (create-event 
  (event-id uint) 
  (description (string-utf8 256))
)
  (begin
    (map-insert events 
      { event-id: event-id }
      { description: description, 
        outcome: none, 
        resolved: false, 
        total-pool: u0 }
    )
    (ok true)
  )
)

;; Place a prediction bet
(define-public (place-prediction 
  (event-id uint) 
  (prediction uint)
)
  (let 
    ((bet-amount (stx-get-balance tx-sender))
     (current-event (unwrap! 
       (map-get? events { event-id: event-id }) 
       (err u1))
     )
  )
    (if (not (get resolved current-event))
      (begin 
        (map-insert predictions 
          { event-id: event-id, user: tx-sender }
          { prediction: prediction, 
            bet-amount: bet-amount, 
            claimed: false }
        )
        (ok true)
      )
      (err u2)
    )
  )
)