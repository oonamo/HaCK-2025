from lib.hcsr04 import HCSR04

TRIGGER_PIN = 20
ECHO_PIN = 21

sensor = HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN)

def get_distance_cm():
    try:
        return sensor.distance_cm()
    except OSError:
        return None
