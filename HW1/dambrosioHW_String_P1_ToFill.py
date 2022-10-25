#Fill in the exercises below per instructions
#If you see  "Process finished with exit code 0"
# in console please run the right file

#1 point:
#create the function named "exampleOne" that will return "I am alive! Alive!".
#do it before you run the test file
def exampleOne():
    return ('I am alive! Alive!')
#1 point:
#create the function named exampleTwo, that will have one input parameter.
#take this parameter and add it to "And this alive too: " after that then return
def exampleTwo(livingThing: str) -> str:
    return('And this alive too: ' + livingThing)

#1 point:
#create the function named  exampleThree, that will have three input parameters.
#return the single string with element separated with ...
#like so go...utes...example
def exampleThree(str1 : str, str2: str, str3: str) -> str:
    return( str(str1) + '...' + str(str2) + '...' + str(str3))

#1 point:
#create the function named exampleFour, that will have two input parameters.
#first one is a text you need to adjust, and second is the leading and trailing
# text that needs to be removed
#Example:
#first param: %%%%HOHOHO%%%%, second %, resut HOHOHO
def exampleFour(needAdjust: str, remove: str) -> str:
    return needAdjust.strip(remove)

#3 points:
#create the function named exampleFive, that will have one input parameter.
#change it so all of the question marks are gone
#example: ????Why am i doing? this???? => Why am i doing this
def exampleFive(removeQMarks: str) -> str:
    return (removeQMarks.replace('?', ''))

#3 points:
#create the function named exampleSix, that will have one input parameter.
#Take that input parameter and replace all of the "ss" with "s", and "tt" with "t"
def exampleSix(replaceStr: str) -> str:
    return (replaceStr.replace('ss','s').replace('tt','t'))



