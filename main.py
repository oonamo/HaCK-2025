import time
from machine import ADC, Pin


ldr = ADC(Pin(28))

# CALIBRATION
ADC_DARK = 1000       
ADC_EDGE = 30000      # DISTANCE FROM LAMP ~ 4 IN
ADC_LIGHT = 50000     # LAMP SURFACE


LUMEN_DARK = 0.0
LUMEN_EDGE = 0.94
LUMEN_LIGHT = 1.0

def adc_to_lumens(adc_value):
    if adc_value <= ADC_DARK:
        return LUMEN_DARK
    elif adc_value >= ADC_LIGHT:
        return LUMEN_LIGHT
    elif adc_value >= ADC_EDGE:
        return LUMEN_EDGE + (adc_value - ADC_EDGE) * (LUMEN_LIGHT - LUMEN_EDGE) / (ADC_LIGHT - ADC_EDGE)
    else:
        return LUMEN_DARK + (adc_value - ADC_DARK) * (LUMEN_EDGE - LUMEN_DARK) / (ADC_EDGE - ADC_DARK)

while True:
    adc = ldr.read_u16()
    lumens = adc_to_lumens(adc)
    print(f"ADC: {adc} | Lumens: {lumens:.3f}")
    time.sleep(1)


