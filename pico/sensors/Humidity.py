import dht
from machine import Pin
from time import sleep


sensor = dht.DHT11(Pin(22))

while True:
    try:
        sleep(2)
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print('Temperature: %3.1f C' %temperature)
        print('Humidity: %3.1f %%' %humidity)
    except OSError as e:
        print('Failed to read sensor.')

def get_temperature():
    try:
        sensor.measure()
        return sensor.temperature()
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

        

