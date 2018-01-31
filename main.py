from Management.Sensors import GPIOManager

def initialize():
    """ upon start of the drone, run this program """
    manager = GPIOManager()
    manager.addOutConnections([1,2])
    manager.addInConnections([[3, "UP"]])
initialize()


a = [
  [
    [1,2], "OUT"
  ], 
  [
    [3,4], "IN"
  ]
]