from abstract_factory import AbstractFactory

class SimpleFactory(AbstractFactory):
    #Overwrites the abstract method, to create the simple mode
    def create_mode():
        #change the return
        return 1

    #Overwrites the abstract method, to create many sensors
    def create_sensors():
        #change the return
        return 2