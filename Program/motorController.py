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


# create 4 motor objects - no motors atm, so LED is created instead
motor_1 = Motor(12) #thumb
motor_2 = Motor(16) #index finger
motor_3 = Motor(20) #middle finger
motor_4 = Motor(21) #ring and little finger

class MotorController():
    
    def MoveHand(result):
        
        if result == 0:
            motor_1.RunIn()
            motor_2.RunIn()
            motor_3.RunIn()
            motor_4.RunIn()
                
        elif result == 1:
            motor_1.RunOut()
            motor_2.RunOut()
            motor_3.RunOut()
            motor_4.RunOut()  
                  
        elif result == 2:
            motor_1.RunOut()
            motor_2.RunIn()
            motor_3.RunIn()
            motor_4.RunOut()
                
        elif result == 3: #difficult to make with leds
            motor_1.RunIn()
            motor_2.RunIn()
            motor_3.RunOut()
            motor_4.RunOut()  
                              
        elif result == 4:
            motor_1.RunOut()
            motor_2.RunOut()
            motor_3.RunIn()
            motor_4.RunOut()   
                             
        elif result == 5:
            motor_1.RunOut()
            motor_2.RunIn()
            motor_3.RunOut()
            motor_4.RunOut()  
                              
        elif result == 6: #difficult to make with leds
            motor_1.RunOut()
            motor_2.RunOut()
            motor_3.RunIn()
            motor_4.RunIn()                
        