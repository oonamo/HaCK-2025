from machine import Pin
import ultrasonic
import time
speedofsound=0.0343  # speed of sound thru air at sea level in cm per microsecond 
masterbutton=Pin(25,Pin.IN) # creates pin for master button thatll control all senosrs 
trigger=Pin(27,Pin.OUT)
echo=Pin(26,Pin.IN)

def triggeractivation(): # activates pulse sending via trig pin 
    trigger.off()
    time.sleep_us(1)
    trigger.on()
    time.sleep_us(10)
    trigger.off()

def recievinganddur():
    start=0
    end=0
    triggeractivation()
    while echo.value()==0:
     start=time.ticks_us()
    while echo.value()==1:
     end=time.ticks_us()

    return end-start # delta t will be in microseconds 
    
     
def distance(): #in cm (microseconds drop out)
   time2object=recievinganddur()/2
   distance=speedofsound*time2object
   print(distance)
   return distance
   
    
while True:
   if masterbutton.value()==1:
     distance()
     time.sleep(1)











    
        

    

    
    



