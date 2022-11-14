from multiprocessing import Queue

Stop_Thread = False

class sEMGSensor():

    def getData(sensorList, queueList):
        while True:
            for i in range(len(sensorList)):
                queue = queueList[i]
                sensor = sensorList[i]
                queue.put(sensor.voltage)
                
                if Stop_Thread:
                    break