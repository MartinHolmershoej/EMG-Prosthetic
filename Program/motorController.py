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
        self.currentResult = 0
    
    def MoveHand(self, result):
        
        if result == 0 and not self.currentResult == 0:
            self.motor_1.RunIn()
            self.motor_2.RunIn()
            self.motor_3.RunIn()
            self.motor_4.RunIn()
            self.currentResult = 0
                
        elif result == 1 and not self.currentResult == 1:
            self.motor_1.RunOut()
            self.motor_2.RunOut()
            self.motor_3.RunOut()
            self.motor_4.RunOut()
            self.currentResult = 1  
                  
        elif result == 2 and not self.currentResult == 2:
            self.motor_1.RunOut()
            self.motor_2.RunIn()
            self.motor_3.RunIn()
            self.motor_4.RunOut()
            self.currentResult = 2
                
        elif result == 3 and not self.currentResult == 3: #difficult to make with leds
            self.motor_1.RunIn()
            self.motor_2.RunIn()
            self.motor_3.RunOut()
            self.motor_4.RunOut()
            self.currentResult = 3  
                              
        elif result == 4 and not self.currentResult == 4:
            self.motor_1.RunOut()
            self.motor_2.RunOut()
            self.motor_3.RunIn()
            self.motor_4.RunOut()
            self.currentResult = 4   
                             
        elif result == 5 and not self.currentResult == 5:
            self.motor_1.RunOut()
            self.motor_2.RunIn()
            self.motor_3.RunOut()
            self.motor_4.RunOut()
            self.currentResult = 5  
                              
        elif result == 6 and not self.currentResult == 6: #difficult to make with leds
            self.motor_1.RunOut()
            self.motor_2.RunOut()
            self.motor_3.RunIn()
            self.motor_4.RunIn()
            self.currentResult = 6                
        