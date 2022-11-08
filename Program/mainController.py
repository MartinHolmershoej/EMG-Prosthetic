
Mode = True
active = False
gripGroup = 0


def runProsthetic():
    while True:

        #Here we change the mode to simple
        if Mode and not active:
            active = True

            #Create objects here etc
            return None

        #Here we change the mode to advanced
        elif not Mode and active:
            active = False

            #Create objects here etc
            return None

        #call the analyse etc.
    
def ChangeGrip():
    gripGroup =+1

    match gripGroup: #No need for a break in python, its build in
        case 1:
            #set grip group to the first set
            print("grip 1")

        case 2:
            #set grip group to the second set
            print("grip 2")
                        
        case 3:
            #set grip group to the third set
            print("grip 3")
            gripGroup = 0

        case _:
            print("grip 1")