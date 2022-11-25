import busio
import board
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class ManySensors():
    
    def createChannelList(self):
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        # Create the ADC object using the I2C bus
        ads = ADS.ADS1015(i2c)
        
        channel1 = AnalogIn(ads, ADS.P0)
        channel2 = AnalogIn(ads, ADS.P1)
        channel3 = AnalogIn(ads, ADS.P2)
        channel4 = AnalogIn(ads, ADS.P3)
                
        channelList = [channel1, channel2, channel3, channel4]
        
        return channelList