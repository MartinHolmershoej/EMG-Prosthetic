from s_EMG_Sensor import sEMGSensor
import busio
import board
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)


def createList():
    sensor1 = sEMGSensor(AnalogIn(ads, ADS.P0))
    sensor2 = sEMGSensor(AnalogIn(ads, ADS.P1))
    sensor3 = sEMGSensor(AnalogIn(ads, ADS.P2))
    sensor4 = sEMGSensor(AnalogIn(ads, ADS.P3))

    sensorList = [sensor1, sensor2, sensor3, sensor4]
    
    return sensorList