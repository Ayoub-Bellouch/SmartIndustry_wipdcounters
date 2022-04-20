# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:09:55 2021

@author: MA117284
"""


import datetime

from pylogix import PLC




#Connecting to db -------------------------------------------

#---------------------------------------------------------------------------

commCut= PLC()
commCut.IPAddress= "10.212.52.2"
commCut.ProcessorSlot = 0

commWM = PLC()
commWM.IPAddress= "10.212.50.98"
commWM.ProcessorSlot = 0

commInn= PLC()
commInn.IPAddress = "10.212.54.3"
commInn.ProcessorSlot = 0
    
commOut = PLC()
commOut.IPAddress =  "10.212.54.2"
commOut.ProcessorSlot = 0
    
   
commPWM= PLC()
commPWM.IPAddress = "10.212.54.3"
commPWM.ProcessorSlot = 0

commP2= PLC()
commP2.IPAddress = "10.212.49.180"
commP2.ProcessorSlot = 0


commALS= PLC()
commALS.IPAddress = "10.212.49.130"
commALS.ProcessorSlot = 1



