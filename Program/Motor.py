import IMotor
import gpiozero


class Motor(IMotor):
    
    def __init__(self, pin):
        self.pin = pin
        
    
    def RunOut(self):
        led = gpiozero.LED(self.pin)
        led.on()
        
    
    def RunIn():
        led = gpiozero.LED(self.pin)
        led.off()