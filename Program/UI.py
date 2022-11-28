from time import sleep
from mainController import MainController
import gpiozero, datetime, multiprocessing
from threading import Thread

SimpleMode = True
grip = 1

lastModeRequest = datetime.datetime.now()
lastGripRequest = datetime.datetime.now()


Mode_Led1 = gpiozero.LED(23)
Mode_Led2 = gpiozero.LED(24)
Grip_Led1 = gpiozero.LED(25)
Grip_Led2 = gpiozero.LED(5) 
Grip_Led3 = gpiozero.LED(6)

Mode_Button = gpiozero.Button(4)
Grip_Button = gpiozero.Button(18) 

main = MainController(SimpleMode)

controllerThread = Thread(target=MainController.runProsthetic, args=[main])
controllerThread.start()

Mode_Led1.on()
Grip_Led1.on()

while True:

    if Mode_Button.is_pressed:
        if lastModeRequest < datetime.datetime.now():
            timeOfRequest = datetime.datetime.now()
            lastModeRequest = timeOfRequest + datetime.timedelta(seconds=0.2)
            if not SimpleMode:
                SimpleMode = True
                main.Mode = True
                Mode_Led1.on()
                Mode_Led2.off()

                Grip_Led1.on()
                Grip_Led2.off()
                Grip_Led3.off()
                

            else:
                SimpleMode = False
                main.Mode = False
                Mode_Led1.off()
                Mode_Led2.on()

                Grip_Led1.off()
                Grip_Led2.off()
                Grip_Led3.off()


    if Grip_Button.is_pressed:
        if SimpleMode:
            if lastGripRequest < datetime.datetime.now():
                timeOfRequest = datetime.datetime.now()
                lastGripRequest = timeOfRequest + datetime.timedelta(seconds=0.2)

                main.ChangeGrip()
                
                if grip == 1:
                    Grip_Led1.off()
                    Grip_Led2.on()
                    grip +=1
                elif grip == 2:
                    Grip_Led2.off()
                    Grip_Led3.on()
                    grip +=1
                elif grip == 3:
                    Grip_Led3.off()
                    Grip_Led1.on()
                    grip = 1



        
            
                


