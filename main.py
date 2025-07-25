import time
from machine import ADC, Pin

ldr = ADC(Pin(26))  # GP26 = ADC0

def get_voltage():
    raw = ldr.read_u16()
    voltage = (raw / 65535) * 3.3  # Convert to volts
    return round(voltage, 3)

while True:
    print("Voltage:", get_voltage(), "V")
    time.sleep(5)