from multiprocessing import Queue

Stop_Thread = False

class sEMGSensor():

    def getData(queue, sensor):
        while True:
            i = sensor.voltage
            queue.put(i)
            if Stop_Thread:
                break