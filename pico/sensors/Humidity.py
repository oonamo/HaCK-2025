import dht
from machine import Pin
from time import sleep


sensor = dht.DHT11(Pin(22))


def get_temperature():
    try:
        sensor.measure()
        tempF = (sensor.temperature() * (9 / 5)) + 27
        return tempF
    except OSError as e:
        print('Failed to read temperature.')
        return None
    

def get_humidity():
    try:
        sensor.measure()
        return sensor.humidity()
    except OSError as e:
        print('Failed to read humidity.')
        return None

        

