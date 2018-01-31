""" provides functionality for managing IC2 and Digital Sensors for the drone """
import RPi.GPIO as GPIO


class GPIOManager():
  """ functionality class """
  
  outChannels = [] 
  inChannels = []

  def addOutConnections(self, channelArray):
    """ channelArray is of type [channels], type is OUT """

    try:
      for channelNumber in channelArray:
        GPIO.setup(channelNumber, GPIO.OUT)
        self.outChannels.append(channelNumber)
    except IndexError:
      raise IndexError('Didnt properly specify channels')
    except ValueError:
      raise ValueError('Didnt properly specify channels')

  def addInConnections(self, channelArray):
    """ channelArray is of type [ [channelNumber, type], [channelNumber, type] ] where type is either UP or DOWN """
    try:
      for channel in channelArray:
        if channel[1] == "UP":
          GPIO.setup(channel[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
          self.inChannels.append(channel[0])
        elif channel[1] == "DOWN":
          GPIO.setup(channel[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
          self.inChannels.append(channel[0])
    except Exception as e:
      print(e)

      
  def getChannels(self):
    return self.inChannels
