
RPI Fan Control
===============

Raspberry Pi fan controller is Python script to start and stop  5V fan depends on RPI cpu temperature.


Description
=================

Before run you can customize script settings such as FAN GPIO number, SLEEP_INTERVAL,
ON_TEMP or OFF_TEMP. If you have only two wire fan PWM control causes an unpleasant sound and is probably not healthy for the engine.
I tried to customize fan speed depends on CPU temperature but to do this the best way is use fan with three or four wire to set this. If you have extra wires you can customize my script to use PWM.


Software requirements
=====================

To be able to run **RPI Fan Control** you have to minimum meet following requirements:

- gpiozero==1.5.1
- RPi.GPIO==0.7.0


Hardware requirements
=====================

.. image:: https://github.com/TheProrok29/rpi-fan/blob/master/circuit_scheme.jpg


Instalation
============

It's possible to run script directly but also you can add this file to system autostart e.g using crontab:

.. code-block:: bash

    $ git clone git@github.com:TheProrok29/rpi-fan.git
    $ cd rpi-fan
    $ sudo pip3 install -r requirements.txt
    $ sudo cp scripts/fan.py /usr/local/bin
    $ sudo chmod +x /usr/local/bin/fan.py
    $ sudo cp scripts/launcher.sh /usr/local/bin
    $ sudo chmod +x /usr/local/bin/launcher.sh
    $ sudo crontab -e

Now, enter the line:

.. code-block:: bash

    $ @reboot sh /usr/local/bin/launcher.sh

License
=============

`MIT <https://choosealicense.com/licenses/mit/>`_
