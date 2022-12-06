from simple_factory import SimpleFactory
from advanced_factory import AdvancedFactory
from s_EMG_Sensor import sEMGSensor
from threading import Thread
from multiprocessing import Process
from time import sleep
import gpiozero    

class MainController():

    def __init__(self, SimpleMode) -> None:
        self.Mode = SimpleMode
        self.active = False
        self.gripGroup = 1
        self.Algorithm_controller = None
        self.sensor = sEMGSensor()
        
        self.device1 = gpiozero.OutputDevice(17)
        self.device2 = gpiozero.OutputDevice(27)
        self.device3 = gpiozero.OutputDevice(22)
        self.device4 = gpiozero.OutputDevice(10)

        
        self.channelList = []
        self.queueList =[]
        
        self.producerThread = Process()
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

                self.powerSensorsOff(self.channelList,)

                #Create objects here etc
                factory = SimpleFactory()
                self.Algorithm_controller = factory.create_mode()
                self.channelList = factory.create_channels()
                self.queueList = factory.create_queues()
                self.powerSensorsOn(self.channelList,)
                sleep(7) # added the sleep to make sure that the sensors has setteled in
                
                self.producerThread = Process(target=self.sensor.getData, args=(self.channelList, self.queueList))
                self.producerThread.start()
                
                self.Algorithm_controller.Baseline(self.queueList)

                self.consumerThread = Process(target=self.Algorithm_controller.Analyse, args=[self.queueList, self.gripGroup]) 
                            
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
                self.Algorithm_controller = factory.create_mode()
                self.channelList = factory.create_channels()
                self.queueList = factory.create_queues()
                self.powerSensorsOn(self.channelList, self.pinList)
                
                self.producerThread = Process(target=self.sensor.getData, args=(self.channelList, self.queueList))
                self.producerThread.start()
                            
                self.consumerThread = Process(target=self.Algorithm_controller.Analyse, args=[self.queueList])
                
                
            #call the analyse etc.
            self.consumerThread.run()
            

    def powerSensorsOn(self, sensorList):
        
        if(len(sensorList)) == 2:
            self.device1.on()
            self.device2.on()
            
        elif(len(sensorList)) == 4:
            self.device1.on()
            self.device2.on()
            self.device3.on()
            self.device4.on()
            
    def powerSensorsOff(self, sensorList):
        
        if(len(sensorList)) == 2:
            self.device1.off()
            self.device2.off()
            
        elif(len(sensorList)) == 4:
            self.device1.off()
            self.device2.off()
            self.device3.off()
            self.device4.off()
        
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
