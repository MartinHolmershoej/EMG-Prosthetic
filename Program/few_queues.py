from multiprocessing import Queue

def createQueues():
    queue1 = Queue(maxsize=0)
    queue2 = Queue(maxsize=0)
    queueList = [queue1, queue2]
    
    return queueList