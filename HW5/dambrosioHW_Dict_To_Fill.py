#1 point
#create a function exampleOne with four input parameters.
#return a new dictionary where 1st and 3rd parameter will be keys,
#and 2nd and 4th will be values, so your key-value pair will be 1st-2nd, 3-4th
def exampleOne(in1, in2, in3, in4) -> dict:
    return {in1:in2,
            in3:in4}

#2 points
#create a function exampleTwo with one parameter which will be an array of arrays, where inner arrays have 2 elements
#iterate over each element in the array and extract first element as a key, second as a value
#construct a dictionary out of them
#e.g input( [ ["key1","value1"], ["key2","value2"] ] -> output dictionary of matching pairs "key1"-"value2", "key2"-"value2"
def exampleTwo(in1: list) -> dict:
    myDict = {}
    for arr in in1:
        myDict[arr[0]] = arr[1]
    return myDict

#2 points
#create a function exampleThree with two input paratmers, first one is a random dictionary, second is a random key
#return the square of retrieved element, if input key(second param) is present in input dictionary(first param)
#if not present, return 0
def exampleThree(in1: dict, in2: int) -> int:
    return in1[in2]**2 if in2 in in1.keys() else 0


#5 points
#create function exampleFour with two input parameters, first one is an array of letters, second is words
#return the new dictionary where letters are matched with words based on the first letter, i.e. abbreviation
#you can assume that all of the letters and words will be a unique match, i.e. if 5 letters, then there are 5 words
#e.g. inputs ["D","M","V"], ["Motor","Division","Vehicles"] -> out dictionary of "D"-"Division","M"-"Motor","Vehicles"
def exampleFour(in1: list, in2: list) -> dict:
    myDict = {}
    for letter in in1:
        currLetter = []
        for word in in2:
            if word[0] == letter:
                currLetter.append(word)

        myDict[letter] = currLetter[0] if len(currLetter) == 1 else currLetter
    print(myDict)
    return myDict

