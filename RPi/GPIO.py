"""Hack so that we can write python code in peace without the linter complaining, delete folder when on pi"""

BOARD = 1
OUT = "OUT"
IN = "IN"
PUD_UP = "PUD_UP"
PUD_DOWN = "PUD_DOWN"
def setmode(gpio_option):
  """ fake function to appease the linter """
  print (gpio_option)

def setup(_a, _b, pull_up_down = 0):
  """ fake function to appease the linter """
  print ('channel: ' + str(_a) + ' type: ' + str(_b))

def output(_a, _b):
  """ fake function to appease the linter """
  print (_a + _b)

def cleanup():
  """ fake function to appease the linter """
  print 'a'

def setwarnings(_flag):
  """ fake function to appease the linter """
  print 'False'
