# This module provides a compatibility layer between Python 2.7.x
# and Python 3.x


try:
  prompt = raw_input
except NameError:
  prompt = input

