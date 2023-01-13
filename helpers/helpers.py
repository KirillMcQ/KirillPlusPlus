'''
This file is made for functions used in ../main.py.
'''
import ast
# Error generator
def error(msg):
    print(msg)
    exit()

# This function is to convert a string to its correct data type
def tryeval(val):
  try:
    val = ast.literal_eval(val)
  except ValueError:
    pass
  return val