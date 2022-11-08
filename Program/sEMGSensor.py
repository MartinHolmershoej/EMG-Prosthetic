from multiprocessing import Queue

Stop_Thread = False

def getData(queue, sensor):
    while True:
        sensor.voltage
        queue.put()
        if Stop_Thread:
            break