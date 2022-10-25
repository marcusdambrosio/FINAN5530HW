#Fill in the exercises below per instructions
#If you see  "Process finished with exit code 0"
# in console please run the right file -- _Test

#1 point:
#create the function named  "exampleOne",that will have one input parameter.
#Function should return double length of the array
def exampleOne(inArray: list) -> list:
    return (2 * len(inArray))

#1 point:
#create the function named exampleTwo, that will have one input parameter.
#return second to last element from array
def exampleTwo(inArray: list):
    return inArray[-2]

#1 point:
#create the function named  exampleThree, that will have three input parameters.
#return an array consisting of those 3 elements using no more than 2 lines
def exampleThree(ele1, ele2, ele3) -> list:
    return [ele1, ele2, ele3]
#1 points:
#create the function named  exampleFour, that will have one input array parameter .
#return an array created from first, fourth and sixth element of the input array using no more 2 lines
def exampleFour(inArray: list):
    return [inArray[0], inArray[3], inArray[5]]
#2 points:
#create the function named exampleFive,  that will have one input array parameter and one singular
#return an input array with second parameter added to it
def exampleFive(inArray: list, addEle) -> list:
    inArray.append(addEle)
    return inArray

#2 points
#create the function named exampleSix,that will have three input parameters array, number, string
#remove an element from input array under the index indicated by second input parameter
#replace second element in the input array with string from third parameter
def exampleSix(inArray: list, ind: int, replacement: str) -> list:
    del inArray[ind]
    inArray[1] = replacement
    return inArray

#2 points
#create the function named exampleSeven, that will have one input array parameter and one singular
#remove first two elements from an array and add the second parameter to the end of an array
#please use no more than 3 lines

def exampleSeven(inArray: list, addition) -> list:
    inArray = inArray[2:]
    inArray.append(addition)
    return inArray