from simple_factory import SimpleFactory
from advanced_factory import AdvancedFactory
from s_EMG_Sensor import sEMGSensor
from motorController import MotorController
from threading import Thread
from multiprocessing import Process
import gpiozero    

class MainController():

    def __init__(self, SimpleMode) -> None:
        self.Mode = SimpleMode
        self.active = False
        self.gripGroup = 1
        self.result = 0
        self.Algorithm = None
        self.sensor = sEMGSensor()
        
        self.channelList = []
        self.queueList =[]
        self.pinList = [17,27,22,10] #For the sensors
        
        self.motorThread = Thread(target=MotorController.MoveHand, args=[self.result])
        self.producerThread = Thread()
        self.consumerThread = Process()
        

    #--------------REMBER TO JOIN THE THREAD--------------#
    def runProsthetic(self):

        while True:

            #Here we change the mode to simple
            if self.Mode and not self.active:
                self.active = True
                if self.producerThread.is_alive():
                    self.producerThread.kill()
                    self.producerThread.join()

                self.powerSensorsOff(self.channelList, self.pinList)

                #Create objects here etc
                factory = SimpleFactory()
                self.Algorithm = factory.create_mode()
                self.channelList = factory.create_channels()
                self.queueList = factory.create_queues()
                self.powerSensorsOn(self.channelList, self.pinList)
                
                self.producerThread = Process(target=self.sensor.getData, args=(self.channelList, self.queueList))
                self.producerThread.start()
                
                self.consumerThread = Thread(target=self.Algorithm.Baseline, args=[self.queueList]) 
                self.consumerThread.run()

                self.consumerThread = Process(target=self.Algorithm.Analyse, args=[self.queueList, self.gripGroup]) 
                            
            #Here we change the mode to advanced
            elif not self.Mode and self.active:
                self.active = False
                self.gripGroup = 1
                if self.producerThread.is_alive():
                    self.producerThread.kill()
                    self.producerThread.join()
                    
                self.powerSensorsOff(self.channelList, self.pinList)

                #Create objects here etc
                factory = AdvancedFactory()
                self.Algorithm = factory.create_mode()
                self.channelList = factory.create_channels()
                self.queueList = factory.create_queues()
                self.powerSensorsOn(self.channelList, self.pinList)
                
                self.producerThread = Process(target=self.sensor.getData, args=(self.channelList, self.queueList))
                self.producerThread.start()
                            
                self.consumerThread = Process(target=self.Algorithm.Analyse, args=[self.queueList])
                
                
            #call the analyse etc.
            self.result = self.consumerThread.run()
            
            #call motor thread with result as parameter
            #need to find a way to share result safely between consumer and motor
            #self.motorThread.run()

    def powerSensorsOn(self, sensorList, pinList):
        
        for i in range(len(sensorList)):
            
            device = gpiozero.OutputDevice(pinList[i])
            device.on()
            
    def powerSensorsOff(self, sensorList, pinList):
        
        for i in range(len(sensorList)):
            
            device = gpiozero.OutputDevice(pinList[i])
            device.off()
        
    def ChangeGrip(self):

        if self.gripGroup == 1:
            #set grip group to the first set
            self.gripGroup = 2
            
        elif self.gripGroup == 2:
            #set grip group to the second set
            self.gripGroup = 3
                            
        elif self.gripGroup == 3:
            #set grip group to the third set
            self.gripGroup = 1

        else:
            self.gripGroup = 1
