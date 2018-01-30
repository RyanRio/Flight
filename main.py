from Management.Sensors import GPIOManager

def initialize():
    """ upon start of the drone, run this program """
    manager = GPIOManager()
    manager.addConnections()
    

initialize()
