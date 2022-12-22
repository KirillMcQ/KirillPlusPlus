'''
Started December 7th, 2022.
Ended: ----
This program is used for parsing and compiling user inputed code. It is the Kirill++ language.

TODO:
    - Fix issue that there are no spaces when showing a string.
    - Add support for function declarations.
'''

import ast
from helpers.helpers import *
from helpers.checkers import *

ifCondition = False
wasIfBefore = False
elifCondition = True
isElif = False



# Open the file
file = open("main.kpp", "r")
for code in file:
    # Remove all spaces and new lines
    copyCode = code
    code = code.replace(' ', '').replace('\n', '')

    # Check if the code is a comment
    if code[:2] == '//':
      continue
    elif isIf and code!="ENDIF":
        ifCode.append(code)
    elif isElif and code!="ENDELIF":
        elifCode.append(code)
    elif isElif and code=="ENDELIF":
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
        wasIfBefore = True
        ifCondition = eval(code)
    elif 'STARTELIF' in code:
        # Check if the condition in the if statement is true or false
        code = code.replace("STARTELIF", "").replace("elif", "")
        # Check if there are any user-made variables inside the code. If so, replace them with the actual value
        for i in userVars:
            if i in code:
                code = code.replace(i, str(userVars[i]))
        elifCondition = eval(code)
        isElif = True

    else:
        check(code)
            

    lineNo+=1