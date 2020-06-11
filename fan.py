import subprocess
import time

from gpiozero import LED, CPUTemperature, OutputDevice

#                     Config

FAN = LED(18)  # GPIO pin using to control the fan.
SLEEP_INTERVAL = 5  # (seconds) How often we check the core temperature.
ON_TEMP = 65  # (degrees Celsius) Temperature to start fan.
OFF_TEMP = 45  # (degress Celsius) Temperature to stop fan.

CPU = CPUTemperature()


def get_temp() -> float:
    """
    Return the core temperature using gpiozero.
    """
    return CPU.temperature


if __name__ == '__main__':

    if OFF_TEMP >= ON_TEMP:
        raise RuntimeError('OFF_TEMP must be less than ON_TEMP')

    while True:
        temp = get_temp()
        if temp > ON_TEMP and not FAN.value:
            FAN.on()
        elif FAN.value and temp < OFF_TEMP:
            FAN.off()
        time.sleep(SLEEP_INTERVAL)
