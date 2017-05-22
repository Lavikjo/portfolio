.. title: Electronics workshop
.. slug: electronics-workshop
.. date: 2017-01-04 13:07:20 UTC+02:00
.. tags: electronics, pcb, design, rf, 3D-printing, greenhouse, measurement

--------
Overview
--------

In the Electronics workshop course we worked in 3 member groups to create functional prototype of electronic device. Our team decided to build a remote measurement device for greenhouse. The device could measure light intensity, temperature and humidity although other sensors could be added as well. The measurement device is powered with Li-ion battery and the battery is charged with a solar panel. The measurement device communicates wirelessly through 433 MHz ISM-band to receiver unit installed indoors. The receiver unit has WIFI connection for transmitting the measurement data to internet. It also has small LCD screen for showing the current sensor readings.


----


-----------
Design
-----------

I designed the circuit for measurement and receiver units. I also designed the circuit board for measurement unit. The circuit boards were ordered from professional manufacturer and assembled by hand. The transceiver and battery charging IC chips were quite small but we managed to assemble the boards successfully. The enclosure for the measurement device was designed in CAD and I used my 3D-printer to make it.

----

-------
Summary
-------

We did comprehensive documentation on the features of our project. Documentation also contained measurements of the performance and suggestions for further improvements. Before this course I had no previous knowledge on designing RF circuits but through extensive study I managed to design and build one. While developing the software for the microcontroller controlling the radio chip I learned that for first prototype I should put more debugging LEDs on the circuit board.


**Things I learned:**

* RF circuit and PCB design
* Embedded programming
* Functional prototyping
* Documenting

.. thumbnail:: /images/transmitter.jpg
.. thumbnail:: /images/transmitter2.JPG 
.. thumbnail:: /images/measuring.jpg
