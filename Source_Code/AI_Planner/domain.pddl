(define (domain Kitchen)
  (:requirements  :strips  :typing  :negative-preconditions  :disjunctive-preconditions )
  (:types
   room  heater  window  alarm  exhaust_fan  message hvac_system - object
   )

  (:predicates
          (temp-under-control)
          (load-msg)
          (explosion-prevention)
          (hvac-control)
          (deactivate ?x - hvac_system)
          (in ?x - hvac_system ?r - room)
          (on ?h - heater)
          (off ?a - alarm)
          (close ?w - window)
          (off1 ?e - exhaust_fan)
          (inside ?h - heater ?r - room)
          (at-window ?w - window ?r - room)
          (at-exhaust ?e - exhaust_fan ?r - room)
          (at-alarm ?a - alarm ?r - room)
          (send ?m - message)

   )

   (:functions
	  (temp ?r - room)
	  (weight ?r - room)
	  (hum ?r - room)
	  (lpg ?r - room)
	  (flame ?r - room)
      (co2 ?r - room)
       (temp_threshold)
       (weight_threshold)
       (hum_threshold)
       (lpg_threshold)
       (flame_threshold)
       (co2_threshold)
   )

  ;;comment

  (:action switchoff_heater
        :parameters (?h - heater ?r - room ?m - message)
        :precondition (and (on ?h) (>(temp ?r) (temp_threshold))(>(hum ?r) (hum_threshold)))
        :effect (and(not(on ?h)) (send ?m) (temp-under-control))
   )
   (:action switchon_heater
        :parameters (?h - heater ?r - room ?m - message)
        :precondition (or (not(on ?h)) (<(temp ?r) (temp_threshold))(<(hum ?r) (hum_threshold)))
        :effect (and (on ?h) (send ?m) (temp-under-control))
   )
   (:action open_window-turnon_exhaust-trigger_alarm
       :parameters ( ?a - alarm ?e - exhaust_fan ?w - window ?r - room ?m - message)
       :precondition (and (off ?a) (off1 ?e) (close ?w) (>(lpg ?r) (lpg_threshold))(<(flame ?r) (flame_threshold)))
       :effect (and (not(off ?a)) (not(off1 ?e)) (not(close ?w)) (send ?m) (explosion-prevention))
  )
  (:action close_window-turnoff_exhaust-donttrigger_alarm
       :parameters ( ?a - alarm ?e - exhaust_fan ?w - window ?r - room ?m - message)
       :precondition (or (not(off ?a)) (not(off1 ?e)) (not(close ?w)) (<(lpg ?r) (lpg_threshold))(>=(flame ?r) (flame_threshold)))
       :effect (and (off ?a) (off1 ?e) (close ?w) (send ?m) (explosion-prevention))
  )
  (:action on_hvac
        :parameters (?x - hvac_system ?r - room ?m - message)
        :precondition (or (deactivate ?x) (>(co2 ?r) (co2_threshold)))
        :effect (and(not(deactivate ?x)) (send ?m) (hvac-control))
   )
   (:action off_evac
        :parameters (?x - hvac_system ?r - room ?m - message)
        :precondition (or (not(deactivate ?x))  (<(co2 ?r) (co2_threshold)))
        :effect (and (deactivate ?x) (send ?m) (hvac-control))
   )
   (:action notification_cylinderbooking
        :parameters ( ?r - room ?m - message )
        :precondition (and  (<(weight ?r) (weight_threshold)))
        :effect (and  (send ?m) (load-msg))
   )
   (:action no_notification_cylinderbooking
        :parameters ( ?r - room ?m - message )
        :precondition (and  (>(weight ?r) (weight_threshold)))
        :effect (and  (send ?m) (load-msg))
   )
      )
