#!/usr/bin/env python

import time

from max30100.oxymeter import Oxymeter
from max30100.constants import *

x = Oxymeter(1)

lastReport = time.time() * 1000

if not x.begin():
  print "Error initializing"
  exit(1)

x.setIRLedCurrent(MAX30100_LED_CURR_7_6MA) # Works best with me

print "Running loop"
while True:
  x.update()

  if time.time() * 1000 - lastReport > 1000:
    print("Heart Rate: %s bpm - SpO2: %s%%" %(x.getHeartRate(), x.getSpO2()))
    lastReport = time.time() * 1000


