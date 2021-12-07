import math
import re

class Term:
  __num: int
  __variables: list

  def __init__(self, num:int = 1):
    self.__num = num
    self.__variables = []

  def addVariable(self, var: str, num:int):
    toAppend = [var, num]
    self.__variables.append(toAppend)

  def addVariables(self, variables: list):
    self.__variables.extend(variables)

  def getNum(self):
    return self.__num


  def powery(self, power: int):
    coificient  = math.pow(self.__num, power)
    variables = []
    
    for item in self.__variables:
      variables.append([item[0], item[1] * power])  

    return (coificient, variables)

  def getVariables(self):
    return self.__variables

  def parser(self, token: str):
    num = re.findall("^-?[0-9]*", token)

    if num and num[0]:
      number = num[0]
      self.__num = int(number) if number != '-' else -1
      variable = token.replace(number, '')

      if variable != '':
        self.__variables.append([variable, 1])

    else:
      self.__num = 1
      self.__variables.append([token, 1])

