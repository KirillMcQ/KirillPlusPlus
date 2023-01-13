'''
Started December 7th, 2022.
Ended: ----
TODO:
    - The program stores the function declaration code into the array. Somehow keep that for later so we know when the user calls the function, and store the function name inside the userfunctions array.
    - Fix issue that there are no spaces when showing a string.
'''

import ast
from helpers.helpers import *
from helpers.checkers import *

ifCondition = False
wasIfBefore = False
elifCondition = True
isElif = False
elifConditionToCheck = False
elifCodePass = False
elifCodeCont = False
wasIf = False
elseCondition = False
isElse = False
elsePass = False
elseIfCondition = False
wasElifEver = False
elseCode = []
isFuncDef = False
funcDefCode = []
userFuncsAndCode = {}
funcName = ""

# Open the file
file = open("main.kpp", "r")
for code in file:
  # Remove all spaces and new lines
  copyCode = code
  code = code.replace(' ', '').replace('\n', '')

  # Check if the code is a comment
  if code[:2] == '//':
    continue
  elif "FUNCTION" in code and "STARTFUNCDEF" in code:
    isFuncDef = True
    code = code.replace("FUNCTION", "").replace("STARTFUNCDEF", "")
    parts = code.split('(')
    funcName = parts[0]
    print(funcName)
  elif isFuncDef and code != "ENDFUNCDEF":
    funcDefCode.append(code)
  elif isFuncDef and code == "ENDFUNCDEF":
    isFuncDef = False
    userFuncsAndCode[funcName] = funcDefCode
    userFuncs.append(funcName)
    print(userFuncsAndCode)
    # Do Something after you have the array with function code
  elif isIf and code != "ENDIF":
    ifCode.append(code)
  elif isElif and code != "ENDELIF":
    elifCode.append(code)
  elif elifCodeCont and code == 'ENDELIF':
    elifCodeCont = False
    elifCodePass = False
  elif isElif and code == "ENDELIF":
    isElif = False
    for i in elifCode:
      if elifCondition:
        check(i)
    elifCondition = False
    elifCode = []
  elif isIf and code == "ENDIF":
    isIf = False
    for i in ifCode:
      if ifCondition:
        check(i)
    ifCode = []
    ifCondition = False
  elif 'STARTIF' in code:
    # Check if the condition in the if statement is true or false
    code = code.replace("STARTIF", "").replace("if", "")
    # Check if there are any user-made variables inside the code. If so, replace them with the actual value
    for i in userVars:
      if i in code:
        code = code.replace(i, str(userVars[i]))
    isIf = True
    wasIf = True
    wasIfBefore = True
    ifCondition, elifConditionToCheck = eval(code), eval(code)
  elif 'STARTELIF' in code and not elifConditionToCheck:
    # Check if the condition in the if statement is true or false
    code = code.replace("STARTELIF", "").replace("elif", "")
    # Check if there are any user-made variables inside the code. If so, replace them with the actual value
    for i in userVars:
      if i in code:
        code = code.replace(i, str(userVars[i]))
    elifCondition = eval(code)
    elseIfCondition = eval(code)
    isElif = True
    wasElifEver = True
  elif 'STARTELIF' in code and elifConditionToCheck:
    elifCodePass = True
    elifCodeCont = True
  elif 'STARTELSE' in code and (
      wasIf
      or wasElifEver) and not elifConditionToCheck and not elseIfCondition:
    isElse = True
    elsePass = False
  elif 'STARTELSE' in code:
    elsePass = True
  elif isElse and code != 'ENDELSE' and not elsePass:
    elseCode.append(code)
  elif isElse and code == 'ENDELSE':
    isElse = False
    elsePass = False
    for i in elseCode:
      check(i)
  elif 'ENDELSE' in code and elsePass:
    elsePass = False
  else:
    if not elifCodePass and not elsePass:
      check(code)
  lineNo += 1