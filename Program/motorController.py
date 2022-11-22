from Motor import Motor



#-----------Grip Numbers-----------#

# open = 0 - default open hand/paper

# fist/rock = 1
# pinch = 2
# thumb up = 3
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
        
        match result:
            case 0:
                motor_1.RunIn()
                motor_2.RunIn()
                motor_3.RunIn()
                motor_4.RunIn()
                
            case 1:
                motor_1.RunOut()
                motor_2.RunOut()
                motor_3.RunOut()
                motor_4.RunOut()  
                  
            case 2: # difficut with leds
                motor_1.RunIn()
                motor_2.RunIn()
                motor_3.RunIn()
                motor_4.RunIn()
                
            case 3:
                motor_1.RunIn()
                motor_2.RunOut()
                motor_3.RunOut()
                motor_4.RunOut()  
                              
            case 4:
                motor_1.RunOut()
                motor_2.RunOut()
                motor_3.RunIn()
                motor_4.RunOut()   
                             
            case 5:
                motor_1.RunOut()
                motor_2.RunIn()
                motor_3.RunOut()
                motor_4.RunOut()  
                              
            case 6: # difficut with leds
                motor_1.RunIn()
                motor_2.RunIn()
                motor_3.RunIn()
                motor_4.RunIn()                
        