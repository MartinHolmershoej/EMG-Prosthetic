import IMotor
import gpiozero


class Motor(IMotor.ABC):
    
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)
        
    
    def RunOut(self):
        self.led.on()
        
    
    def RunIn(self):
        self.led.off()