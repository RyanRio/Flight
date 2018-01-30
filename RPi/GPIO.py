"""Hack so that we can write python code in peace without the linter complaining"""

BOARD = 1
OUT = 1
IN = 1


def setmode(gpio_option):
  """ fake function to appease the linter """
  print gpio_option


def setup(_a, _b):
  """ fake function to appease the linter """
  print _a + _b


def output(_a, _b):
  """ fake function to appease the linter """
  print _a + _b


def cleanup():
  """ fake function to appease the linter """
  print 'a'


def setwarnings(_flag):
  """ fake function to appease the linter """
  print 'False'
