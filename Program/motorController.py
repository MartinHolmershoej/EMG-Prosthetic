from Motor import Motor



#-----------Grip Numbers-----------#

# open = 0 - default open hand/paper

# fist/rock = 1
# scissor = 2
# pinch = 3
# F you = 4
# point = 5
# ok = 6

# xxxxx = 7
# xxxxx = 8


class MotorController():
    
    def __init__(self) -> None:
        # create 4 motor objects - no motors atm, so LED is created instead
        self.motor_1 = Motor(12) #thumb
        self.motor_2 = Motor(16) #index finger
        self.motor_3 = Motor(20) #middle finger
        self.motor_4 = Motor(21) #ring and little finger
    
    def MoveHand(self, result):
        
        if result == 0:
            self.motor_1.RunIn()
            self.motor_2.RunIn()
            self.motor_3.RunIn()
            self.motor_4.RunIn()
                
        elif result == 1:
            self.motor_1.RunOut()
            self.motor_2.RunOut()
            self.motor_3.RunOut()
            self.motor_4.RunOut()  
                  
        elif result == 2:
            self.motor_1.RunOut()
            self.motor_2.RunIn()
            self.motor_3.RunIn()
            self.motor_4.RunOut()
                
        elif result == 3: #difficult to make with leds
            self.motor_1.RunIn()
            self.motor_2.RunIn()
            self.motor_3.RunOut()
            self.motor_4.RunOut()  
                              
        elif result == 4:
            self.motor_1.RunOut()
            self.motor_2.RunOut()
            self.motor_3.RunIn()
            self.motor_4.RunOut()   
                             
        elif result == 5:
            self.motor_1.RunOut()
            self.motor_2.RunIn()
            self.motor_3.RunOut()
            self.motor_4.RunOut()  
                              
        elif result == 6: #difficult to make with leds
            self.motor_1.RunOut()
            self.motor_2.RunOut()
            self.motor_3.RunIn()
            self.motor_4.RunIn()                
        