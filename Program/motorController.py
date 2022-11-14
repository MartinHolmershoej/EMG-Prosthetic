import gpiozero



#-----------Grip Numbers-----------#

# open = 1 - default

# fist/rock = 2
# pinch = 3
# thumb up = 4
# F you = 5
# point = 6
# ok = 7

# xxxxx = 8
# xxxxx = 9


# create 4 motor objects - no motors atm, so LED is created instead
motor_1 = gpiozero.LED() #thumb
motor_2 = gpiozero.LED() #index finger
motor_3 = gpiozero.LED() #middle finger
motor_4 = gpiozero.LED() #ring and little finger

class MotorController():
    
    def MoveHand(result, gripGroup):
        
        match result:
            case 1:
                motor_1.off()
                motor_2.off()
                motor_3.off()
                motor_4.off()
                
            case 2:
                motor_1.on()
                motor_2.on()
                motor_3.on()
                motor_4.on()  
                  
            case 3: # difficut with leds
                motor_1.off()
                motor_2.off()
                motor_3.off()
                motor_4.off()
                
            case 4:
                motor_1.off()
                motor_2.on()
                motor_3.on()
                motor_4.on()  
                              
            case 5:
                motor_1.on()
                motor_2.on()
                motor_3.off()
                motor_4.on()   
                             
            case 6:
                motor_1.on()
                motor_2.off()
                motor_3.on()
                motor_4.on()  
                              
            case 7: # difficut with leds
                motor_1.off()
                motor_2.off()
                motor_3.off()
                motor_4.off()                
        