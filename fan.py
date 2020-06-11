import subprocess
import time

from gpiozero import LED, OutputDevice

# Config
FAN = LED(18)  # GPIO pin using to control the fan.
SLEEP_INTERVAL = 5  # (seconds) How often we check the core temperature.
ON_TEMP = 65  # (degrees Celsius) Temperature to start fan.
OFF_TEMP = 45  # (degress Celsius) Temperature to stop fan.

