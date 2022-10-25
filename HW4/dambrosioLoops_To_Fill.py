#1 point
#create function exampleOne with one input parameter
#the input is an array of numbers
#square each number and return it as a new array
def exampleOne(in1: list) -> list:
    return [c**2 for c in in1]

#2 points
#create function exampleTwo with one input parameter
#the input is an array of numbers
#return last 2 elements of the array in a new array with 100 added to each element
def exampleTwo(in1: list) -> list:
    return [in1[-2]+100, in1[-1]+100]

#2 points
#create function exampleThree with one input parameter
#the input is an array of random elemnts
#return even elements i.e. 2nd, 4th, 6th, etc.
def exampleThree(in1: list) -> list:
    newArr = []
    for i, item in enumerate(in1):H
        if (i+1) % 2 == 0:
            newArr.append(item)
    print(newArr)
    return newArr

#5 points
#create function exampleFour with two input parameters
#the first input is an array of numbers, second is a single number
#if an element of the array is divisible by the second parameter without remainder
#add it to the temp array
#if element is either 7 or 12 immediately move out of the loop.
#next operation is to transform each element in temp array to the string element
#return transofrmed elements as an array
#hint: the remainder is calculated through %, i.e 7%2 = 1
def exampleFour(in1: list, in2: int) -> list:
    tempArr = []
    for item in in1:
        if item % in2 == 0:
            if item == 7 or item == 12:
                break
            else:
                tempArr.append(item)
        elif item ==  7 or item == 12:
            break
    return [str(c) for c in tempArr]

