""" provides functionality for managing IC2 and Digital Sensors for the drone """
from RPi import GPIO
class GPIOManager():
    """ functionality class """
    def __init__(self):
        
    def addConnections(channelArray):
        """ channelArray is of type [[[channels], type], [[channels], type]], type is either IN or OUT """

        for channel in channelArray:
            if channel[1] == "OUT":
                for channelNumber in channel[0]:
                    GPIO.setup(channelNumber, GPIO.OUT)
            else if channel[1] == "IN":
                for channelNumber in channel[0]:
                    GPIO.setup(channelNumber, GPIO.OUT)
            else:
                print()
