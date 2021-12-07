import math
import re
import json
from Term import Term

def combination(n:int, i: int) -> int:
  num: int
  den: int

  if n < 0:
    n = - n
    sub = n + i - 1 

    num = math.pow(-1, i) * math.factorial(sub)
    den = math.factorial(i) * math.factorial(sub - i)
  else:
    num = math.factorial(n)
    den = math.factorial(i) * math.factorial(n - i)

  return num / den

def developBinomio(n: int,  stTerm: str, secTerm: str):
  firstT = Term()
  secT = Term()

  firstT.parser(stTerm)
  secT.parser(secTerm)

  numTerms = abs(n) + 1
  isNegative = True if n < 0 else False

  terms = []

  for i in range(numTerms):
    fVariable = []
    variables = []
    fValue = 1
    term = {}
    den = 1

    if isNegative:
      den = math.pow(firstT.getNum(), abs(n) + i) 
    else:
      (fValue, fVariable) = firstT.powery(n-i)

    (sValue, sVariable) = secT.powery(i)

    value = combination(n,i) * fValue * sValue
    joinedVars =  fVariable + sVariable 

    term['num'] = value
    term['den'] = den

    for var in joinedVars:
      dicVar = {
        'var': var[0],
        'pow': var[1]
      }

      if var[1] > 0:
        variables.append(dicVar)
    
    term['variables'] = variables
    terms.append(term)
  
  return json.dumps(terms)
