from abstract_factory import AbstractFactory

class AdvancedFactory(AbstractFactory):
    #Overwrites the abstract method, to create advanced mode
    def create_mode():
        #change the return
        return 

    #Overwrites the abstract method, to create many sensors
    def create_sensors():
        #change the return
        return 
    
    def create_queues(self):
        return 