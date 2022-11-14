import gpiozero



#-----------Grip Numbers-----------#

# open = 0 - default

# fist/rock = 1
# pinch = 2
# thumb up = 3
# F you = 4
# point = 5
# ok = 6

# xxxxx = 7
# xxxxx = 8


# create 4 motor objects - no motors atm, so LED is created instead
motor_1 = gpiozero.LED() #thumb
motor_2 = gpiozero.LED() #index finger
motor_3 = gpiozero.LED() #middle finger
motor_4 = gpiozero.LED() #ring and little finger

class MotorController():
    
    def MoveHand(result):
        
        match result:
            case 0:
                motor_1.off()
                motor_2.off()
                motor_3.off()
                motor_4.off()
                
            case 1:
                motor_1.on()
                motor_2.on()
                motor_3.on()
                motor_4.on()  
                  
            case 2: # difficut with leds
                motor_1.off()
                motor_2.off()
                motor_3.off()
                motor_4.off()
                
            case 3:
                motor_1.off()
                motor_2.on()
                motor_3.on()
                motor_4.on()  
                              
            case 4:
                motor_1.on()
                motor_2.on()
                motor_3.off()
                motor_4.on()   
                             
            case 5:
                motor_1.on()
                motor_2.off()
                motor_3.on()
                motor_4.on()  
                              
            case 6: # difficut with leds
                motor_1.off()
                motor_2.off()
                motor_3.off()
                motor_4.off()                
        