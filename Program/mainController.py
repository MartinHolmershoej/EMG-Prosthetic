from simple_factory import SimpleFactory
from advanced_factory import AdvancedFactory
from threading import Thread
import gpiozero

Mode = True
active = False
gripGroup = 0
pinList = [1,2,3] #Change to correct pin numbers


#--------------REMBER TO JOIN THE THREAD--------------#
def runProsthetic():
    while True:

        #Here we change the mode to simple
        if Mode and not active:
            active = True
            powerSensorsOff(sensorList, pinList)

            #Create objects here etc
            factory = SimpleFactory
            Algorithm = factory.create_mode()
            sensorList = factory.create_sensors()
            powerSensorsOn(sensorList, pinList)

            consumerThread = Thread(target=Algorithm.Analyse(), args=()) #maybe take a list if queues instead
            
        #Here we change the mode to advanced
        elif not Mode and active:
            active = False
            powerSensorsOff(sensorList, pinList)

            #Create objects here etc
            factory = AdvancedFactory
            Algorithm = factory.create_mode()
            sensorList = factory.create_sensors()
            powerSensorsOn(sensorList, pinList)
            
            consumerThread = Thread(target=Algorithm.Analyse(), args=())  #maybe take a list if queues instead

        #call the analyse etc.
        result = consumerThread.run()
        
        #call motor thread with result as parameter

def powerSensorsOn(sensorList, pinList):
    
    for i in range(len(sensorList)):
        
        device = gpiozero.OutputDevice(pinList[i])
        device.on()
        
def powerSensorsOff(sensorList, pinList):
    
    for i in range(len(sensorList)):
        
        device = gpiozero.OutputDevice(pinList[i])
        device.Off()
    
def ChangeGrip():
    gripGroup =+1

    match gripGroup: #No need for a break in python, its build in
        case 1:
            #set grip group to the first set
            print("grip 1")

        case 2:
            #set grip group to the second set
            print("grip 2")
                        
        case 3:
            #set grip group to the third set
            print("grip 3")
            gripGroup = 0

        case _:
            print("grip 1")
