import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
import time
import sys
from datetime import datetime


pin1 = 11  
pin2 = 12



GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(pin2, GPIO.IN)

n = input('Enter the Running time(s):')
if n == '':
   n = 15
else:
   n = int(n)
   
b = input('Enter the recording time interval(s):')
if b == '':
   b = 1
else:
   b = float(b)

n = n/b

c = input('Enter the blinking time interval(s):')
if c == '':
   c = 1
else:
   c = float(c)

DEBUG = False
if '-debug' in sys.argv:
   DEBUG = True

LED_IS_ON = False
ite = 1
with open('data.txt','w') as data:
   while n > 0:
      if GPIO.input(pin2):
         GPIO.output(pin1, GPIO.HIGH)
         LED_IS_ON = True
         GPIO.output(pin1, GPIO.HIGH) # Turn on
         sleep(c)                     # Sleep for 1 second
         GPIO.output(pin1, GPIO.LOW)  # Turn off
         sleep(c)                     # Sleep for 1 second
         date_t = datetime.fromtimestamp(time.time())
         data.write(f'{date_t} {LED_IS_ON}\n')
         if DEBUG:
            print(f'{date_t} iteration time: {ite} LED is on: {LED_IS_ON}')
         diff = b - 2*c
         if diff < 0:
            diff = 0
         time.sleep(diff)
         
      else:
         GPIO.output(pin1, GPIO.LOW)
         date_t = datetime.fromtimestamp(time.time())
         LED_IS_ON = False
         data.write(f'{date_t} {LED_IS_ON}\n')
         if DEBUG:
            print(f'{date_t} iteration time: {ite} LED is on: {LED_IS_ON}')
         time.sleep(b)
         
      n = n - 1
      ite = ite+1
GPIO.cleanup()
