
class sEMGSensor():

    def getData(self, channelList, queueList):
        while True:
            for i in range(len(channelList)):
                channel = channelList[i-1]
                queue = queueList[i-1]
                queue.put(channel.voltage)
                
                
