'''
This file is for use on ../main.py and is for parsing certain code like variable calls and function calls.
'''

from helpers.helpers import *

# Global vars
operators = ['+', '-', '*', '/']
comparison = ['>', '<', '>=', '<=', '==', '!=']
lineNo = 1
isIf = False
ifCode = []
elifCode = []
parts = ""
funcName = ""
args = ""
userFunctionCode = []


# Built-in functions
builtInFuncs = ['show', 'if']

# User-made variables
userVars = {}

# User-made function names
userFuncs = []


############################### VAR ASSIGN CHECK ##################################
def check(code):
    if "STORE" in code and "IN" in code:
        if code.count('STORE') > 1 or code.count('IN') > 1:
            error("Error on line " + str(lineNo) + ": Multiple assignment operators.")

        code = code.split('IN')
        code[0] = code[0].replace('STORE', '')
        # Switch the two elements
        temp = code[0]
        code[0] = code[1]
        code[1] = temp

        if len(code[1]) == 0:
            error("Error on line " + str(lineNo) + ": Empty value assigned to variable.")
        elif len(code[0]) == 0:
            error("Error on line " + str(lineNo) + ": No variable name given.")
        
        if isinstance(tryeval(code[1]), str):
            code[1] = tryeval(code[1]).replace("\n","")
        else:
            code[1] = tryeval(code[1])
        # If the value the var is being assigned to does not contain a quote and is not a number we check if it is another var, else give error
        if "'" not in str(code[1]) and '"' not in str(code[1]) and isinstance(tryeval(code[1]), str) == True and '+' not in code[1] and '-' not in code[1] and '*' not in code[1] and '/' not in code[1]:
            if code[1] not in userVars:
                error("Error on line " + str(lineNo) + ": Variable " + code[1] + " does not exist.")
            else:
                userVars[code[0]] = userVars[code[1]]
        # Check if the value that var is being assigned to is an operation
        elif isinstance(code[1], str) and '+' in str(code[1]) or '-' in str(code[1]) or '*' in str(code[1]) or '/' in str(code[1]) and '"' not in str(code[1]) and "'" not in str(code[1]):
            # Replace var calls in an operation with the var value
            if [val for key,val in userVars.items() if key in str(code[1])]:
                for key in userVars:
                    if key in str(code[1]):
                        code[1] = code[1].replace(key, str(userVars[key]))
            userVars[code[0]] = eval(code[1])
        else:
            userVars[code[0]] = code[1]
    ############################# VAR ASSIGN CHECK END #####################################

    ############################# FUNCTION CALL CHECK #######################



    elif '(' in code and ')' in code and '-' not in code and '+' not in code and '*' not in code and '/' not in code and len(code) > 2 and '>=' not in code and '<=' not in code and '==' not in code and '!=' not in code and '>' not in code and '<' not in code:
        if code.count('(') > 1 or code.count(')') > 1:
            error("Error on line " + str(lineNo) + ": Multiple function calls.")
          # TODO: Open a new python file, and then write to it the function decleration with the name and the args. THen, if someone clals it just import the funcs from that file
          
        parts = code.split('(')
        funcName = parts[0]
        args = parts[1][:-1]

        if funcName in builtInFuncs:
            if args != "":
                if funcName == 'show':
                    if isinstance(tryeval(args), str):
                        if args.count('"')==2 or args.count("'")==2:
                            print(args.replace("'", "").replace('"', ""))
                        else:
                            # See if the arg is a variable
                            if args in userVars:
                                print(userVars[args])
                            else:
                                error("Undefined term " + "'" + str(args) + "'" + " on line " + str(lineNo))
                    else:
                        print(args)

            else:
                if funcName == 'show':
                    error("Built-in function 'show' called without arguments.")
        else:
            if funcName not in userFuncs:
              error("Error on line " + str(lineNo) + ": Function " + funcName + " does not exist.")
            else:
              print("Func in user made funcs list!")