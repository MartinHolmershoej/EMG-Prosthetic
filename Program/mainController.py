from simple_factory import SimpleFactory
from advanced_factory import AdvancedFactory
from s_EMG_Sensor import sEMGSensor
from motorController import MotorController
from threading import Thread
import gpiozero

Mode = True
active = False
gripGroup = 1
result = 0
sensorList = []
pinList = [1,2,3] #Change to correct pin numbers
motorThread = Thread(target=MotorController.MoveHand, args=(result))


#--------------REMBER TO JOIN THE THREAD--------------#
def runProsthetic():
    while True:

        #Here we change the mode to simple
        if Mode and not active:
            active = True
            producerThread.join()
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
            consumerThread = Thread(target=Algorithm.Analyse, args=(queueList, gripGroup)) 
                        
        #Here we change the mode to advanced
        elif not Mode and active:
            active = False
            gripGroup = 1
            producerThread.join()
            powerSensorsOff(sensorList, pinList)

            #Create objects here etc
            factory = AdvancedFactory
            Algorithm = factory.create_mode()
            sensorList = factory.create_sensors()
            queueList = factory.create_queues()
            powerSensorsOn(sensorList, pinList)
            
            producerThread = Thread(target=sEMGSensor.getData, args=(sensorList, queueList))
            producerThread.start()
                        
            consumerThread = Thread(target=Algorithm.Analyse, args=(queueList))
            
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
            gripGroup = 1
