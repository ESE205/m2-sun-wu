import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

 
pin1 = 11
n = input('Enter the blink times:')
if n == '':
   n = 5
else:
   n = int(n)

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   

while n > 0: # Run ITER_COUNT times
   n = n - 1 # Decrement counter
   GPIO.output(pin1, GPIO.HIGH) # Turn on
   sleep(1)                     # Sleep for 1 second
   GPIO.output(pin1, GPIO.LOW)  # Turn off
   sleep(1)                     # Sleep for 1 second
GPIO.cleanup()
