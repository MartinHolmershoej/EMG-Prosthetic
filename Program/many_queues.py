from multiprocessing import Queue

def createQueues():
    queue1 = Queue(maxsize=0)
    queue2 = Queue(maxsize=0)
    queue3 = Queue(maxsize=0)
    queue4 = Queue(maxsize=0)
    queueList = [queue1, queue2, queue3, queue4]
    
    return queueList
