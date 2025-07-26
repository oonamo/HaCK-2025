import time

from machine import ADC, Pin

ldr = ADC(Pin(26, Pin.IN))

RESISTOR_VAL = 1000

ADC_MAX = 65535
LUMEN_CONVERSION = 0.75  # Ohms/ Lumen


def adc_to_ohms(adc_val):
    ohms = (RESISTOR_VAL * (ADC_MAX - adc_val)) / adc_val
    print("ohms", ohms)
    return ohms

# TODO: find linear relation
def convert(adc):
    return adc * (1 / 346_000)


def ohms_to_lux(ohms):
    return ohms * (LUMEN_CONVERSION)


def adc_to_v(adc):
    return adc * (3.3 / ADC_MAX)


def read_photoresistor_value():
    return ldr.read_u16()


def read_pr_lumens():
    adc = read_photoresistor_value()
    return ohms_to_lux(adc_to_ohms(adc))
