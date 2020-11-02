(define (problem Safety)
(:domain Kitchen)
(:objects
   r1 - room
   h1 - heater
   w1 - window
   e1 - exhaust_fan
   a1 - alarm
   x1 - hvac_system
   m1 - message)
(:init
    (on h1)
    (inside h1 r1)
    (close w1)
    (at-window w1 r1)
    (off1 e1)
    (at-exhaust e1 r1)
    (off a1)
    (at-alarm a1 r1)
    (deactivate x1)
    (in x1 r1)
    ;temp
    (= (temp_threshold) 26)
    (= (temp r1) 29.0)
    ;load
    (= (weight_threshold) 19)
    (= (weight r1) 28.0)
    ;hum
    (= (hum_threshold) 65)
    (= (hum r1) 67.0 )
    ;flame
    (= (flame_threshold) 1)
    (= (flame r1) 0.0)
    ;mq2 sensor
    (= (lpg_threshold) 700)
    (= (lpg r1) 300.0)
    ;co2 sensor
    (= (co2_threshold) 500)
    (= (co2 r1) 300.0)

)
(:goal
    (and
    (temp-under-control)
    (explosion-prevention)
    (load-msg)
    (hvac-control)))
)