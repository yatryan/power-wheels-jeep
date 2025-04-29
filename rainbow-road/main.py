# Rainbow Road Jeep

from machine import Pin
import machine, neopixel, time
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
import _thread

# OTA Update Link
firmware_url = "https://raw.githubusercontent.com/yatryan/power-wheels-jeep/master/rainbow-road/"

# Perform OTA
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

# configure pushbuttons as interrupts
switch = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

led = Pin('LED', Pin.OUT)
led.value(True)

# LED strip configuration
# number of pixels
n = 160
# strip control gpio
p = 10 # GP10
np = neopixel.NeoPixel(machine.Pin(p), n)

# FUNCTIONS FOR LIGHTING EFFECTS

# function to go through all colors 
def wheel(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

# rainbow 
def rainbow_cycle(wait):
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    time.sleep_ms(wait)


# Thread it up!
def rainbow_cycle_thread():
  while True:
    rainbow_cycle(1)

# turn off all pixels
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

_thread.start_new_thread(rainbow_cycle_thread, ())

#while True:
#  if switch.value() == 0:
#    clear()
#  elif switch.value() == 1:
#    rainbow_cycle(1)

