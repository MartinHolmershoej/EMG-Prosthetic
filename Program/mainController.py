from simple_factory import SimpleFactory
from advanced_factory import AdvancedFactory
from s_EMG_Sensor import sEMGSensor
from motorController import MotorController
from threading import Thread
from multiprocessing import process
import gpiozero

Mode = True
active = False
gripGroup = 1
result = 0
sensorList = []
pinList = [17,27,22,10] #For the sensors
motorThread = Thread(target=MotorController.MoveHand, args=(result))
consumerThread = process

#--------------REMBER TO JOIN THE THREAD--------------#
def runProsthetic():
    while True:

        #Here we change the mode to simple
        if Mode and not active:
            active = True
            producerThread.join()
            consumerThread.join()
            powerSensorsOff(sensorList, pinList)

            #Create objects here etc
            factory = SimpleFactory
            Algorithm = factory.create_mode()
            sensorList = factory.create_sensors()
            queueList = factory.create_queues()
            powerSensorsOn(sensorList, pinList)
            
            producerThread = Thread(target=sEMGSensor.getData, args=(sensorList, queueList))
            producerThread.start()
            
            consumerThread = Thread(target=Algorithm.Baseline, args=(queueList)) 
            consumerThread.run()
            consumerThread.join()
            consumerThread = process(target=Algorithm.Analyse, args=(queueList, gripGroup)) 
                        
        #Here we change the mode to advanced
        elif not Mode and active:
            active = False
            gripGroup = 1
            producerThread.join()
            consumerThread.join()
            powerSensorsOff(sensorList, pinList)

            #Create objects here etc
            factory = AdvancedFactory
            Algorithm = factory.create_mode()
            sensorList = factory.create_sensors()
            queueList = factory.create_queues()
            powerSensorsOn(sensorList, pinList)
            
            producerThread = Thread(target=sEMGSensor.getData, args=(sensorList, queueList))
            producerThread.start()
                        
            consumerThread = process(target=Algorithm.Analyse, args=(queueList))
            
            
        #call the analyse etc.
        result = consumerThread.run()
        
        #call motor thread with result as parameter
        motorThread.run(result)

def powerSensorsOn(sensorList, pinList):
    
    for i in range(len(sensorList)):
        
        device = gpiozero.OutputDevice(pinList[i])
        device.on()
        
def powerSensorsOff(sensorList, pinList):
    
    for i in range(len(sensorList)):
        
        device = gpiozero.OutputDevice(pinList[i])
        device.Off()
    
def ChangeGrip():

    if gripGroup == 1:
        #set grip group to the first set
        gripGroup = 2
        
    elif gripGroup == 2:
        #set grip group to the second set
        gripGroup = 3
                        
    elif gripGroup == 3:
        #set grip group to the third set
        gripGroup = 1

    else:
        gripGroup = 1
