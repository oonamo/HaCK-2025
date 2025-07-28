import dht
from machine import Pin
import time

DHT_PIN = 22

DELTA = -5

sensor = dht.DHT11(Pin(DHT_PIN))


def get_temperature():
    try:
        sensor.measure()
        tempF = (sensor.temperature() * (9 / 5)) + 32 + DELTA
        return tempF
    except OSError:
        print("Failed to read temperature.")
        return None


def get_humidity():
    try:
        sensor.measure()
        return sensor.humidity()
    except OSError:
        print("Failed to read humidity.")
        return None


# while True:
#     print("humidity: ", get_humidity())
#     print("temp: ", get_temperature())
#     time.sleep(1)
