#Fill in the exercises below per instructions
#If you see  "Process finished with exit code 0"
# in console please run the right file -- _Test


#1 point
#create function named exampleOne, that will have 2 input parameters.
#return True if they are not equal to each other
def exampleOne(input1, input2) -> bool:
    if input1 != input2:
        return True


#1 point
#create function named  exampleTwo, that will have 3 input parameters.
#return True if all of them are equal to each other
def exampleTwo(in1, in2, in3) -> bool:
    if in1 == in2 == in3:
        return True

#1 point
#create function named exampleThree, that will have 3 input parameters.
#return True if either first is different from second or second same is the third
def exampleThree(in1, in2, in3) -> bool:
    if in1 != in2 or in2 == in3:
        return True


#2 points
#create function named exampleFour, that will have 2 input parameters.
#if second param is a part of the first one -- reutrn the last letter of first param
#if second param is not a part of the first one -- return first letter of first param
#hint every string -- is an array of letter and can be used as such
def exampleFour(in1, in2) -> str:
    if in2 in in1:
        return in1[-1]
    else:
        return in1[0]

#2 points
#create function named exampleFive, that will have 3 input parameters: one array and two singular.
#return "One", if second element is in an array
#return "Two", if third element is in an array
#return "None", if none of the elements are in the array
def exampleFive(arr: list, in2, in3) -> str:
    if in2 in arr:
        return 'One'
    elif in3 in arr:
        return 'Two'
    else:
        return 'None'

#3 points
#create function named exampleSix, that will have 3 input parameters: one array and two singular.
#return "Success" if second element is NOT in the array and number of elements in the array equals to the third element
#return "Not In Success" if second element is NOT in the array  and number of elements in the array does not equals to the third element
#return "Length Success"  if second element is in the array and number of elements in the array equals to the third element
#return "Failure" if second element is in the array and number of elements in the array does not equals to the third element
def exampleSix(arr: list, in2, in3) -> str:
    if in2 not in arr:
        if len(arr) == in3:
            return 'Success'
        else:
            return 'Not In Success'
    else:
        if len(arr) == in3:
            return 'Length Success'
        else:
            return 'Failure'

