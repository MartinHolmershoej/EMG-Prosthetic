import gpiozero, datetime, multiprocessing
import mainController
from threading import Thread

SimpleMode = True

lastModeRequest = datetime.datetime.now()
lastGripRequest = datetime.datetime.now()


Power_Led = gpiozero.LED(4)
Mode_Led1 = gpiozero.LED() #Remeber to set pin number
Mode_Led2 = gpiozero.LED() #Remeber to set pin number
Grip_Led1 = gpiozero.LED() #Remeber to set pin number
Grip_Led2 = gpiozero.LED() #Remeber to set pin number
Grip_Led3 = gpiozero.LED() #Remeber to set pin number

Mode_Button = gpiozero.Button(18)
Grip_Button = gpiozero.Button() #Remeber to set pin number


controllerThread = Thread(target=mainController.onBootUp)
controllerThread.start()

while True:

    if Mode_Button.is_pressed:
        if lastModeRequest < datetime.datetime.now():
            timeOfRequest = datetime.datetime.now()
            lastModeRequest = timeOfRequest + datetime.timedelta(seconds=0.2)
            if not SimpleMode:
                SimpleMode = True
                mainController.Mode = True

            else:
                SimpleMode = False
                mainController.Mode = False


    if Grip_Button.is_pressed:
        if SimpleMode:
            if lastGripRequest < datetime.datetime.now():
                timeOfRequest = datetime.datetime.now()
                lastGripRequest = timeOfRequest + datetime.timedelta(seconds=0.2)

                mainController.ChangeGrip()



        
            
                


