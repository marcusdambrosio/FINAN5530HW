def doSimpleCalculations():
    a = 99999#  create variable equal to 99999
    b = 11111#  create variable equal to 11111
    return(a / b)#  return first variable divided by the second one


def combineStringsSimple():
  var1 = 'University of' #  create variable Univerisity of
  var2 = ' Utah'#  create variable Utah
  var3 = ' Rules'#  create variable Rules
  return (var1 + var2 + var3)#   return University of Utah Rules


def combineNumsStrings():
  num1 = 32000#  create number variable 32000
  str1 = 'University of Utah has ' #  create variable University of Utah has
  str2 = ' students' #  create variable students
  return (str1 + str(num1) + str2)#  combine all of the variables so you would get University of Utah has 32000 students


#create a function named convertStringToNum, that will have one input parameter
#take that input parameter, convert it to float and divide by 50
#return the result

def convertStringToNum(input1: float or int or str) -> float:
    return float(input1) / 50

