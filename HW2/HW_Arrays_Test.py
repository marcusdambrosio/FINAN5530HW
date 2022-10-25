import dambrosioHW_Arrays_ToFill as toFill

score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    testArray=[1,2,3,4,5,6,'q']
    testArray2=[1,"duo",3,4]
    if toFill.exampleOne(testArray) == 14 and toFill.exampleOne(testArray2)==8:
        print(1)
        score+=1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    testArray = [1, 2, 3, 4, 5, 'six', 'q']
    testArray2 = [1, 2, 3, 4, 5, ]
    if toFill.exampleTwo(testArray) == 'six' and  toFill.exampleTwo(testArray2) == 4 :
        print(2)
        score+=1

else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if toFill.exampleThree("one","TWO",3) == ["one","TWO",3] and toFill.exampleThree(1,2,3) == [1,2,3]:
        print(3)
        score+=1

else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a','b','c','d','e','f']
    if toFill.exampleFour(testArray) == [1,4,6] and toFill.exampleFour(testArray2) == ['a','d','f']:
        print(4)
        score+=2

else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a', 'b', 'c', 'd', 'e', 'f']
    if toFill.exampleFive(testArray,'e') == [1, 2, 3, 4, 5, 6, 'q','e'] \
            and toFill.exampleFive(testArray2,'g') ==['a', 'b', 'c', 'd', 'e', 'f','g'] :
        print(5)
        score+=1

else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a', 'b', 'c', 'd', 'e', 'f']
    if toFill.exampleSix(testArray,3,"w") == [1,'w',3,5,6,'q'] \
            and toFill.exampleSix(testArray2,4,"w") == ['a', 'w', 'c', 'd', 'f']:
        print(6)
        score+=2

else:
    print("ATTN:!!!Please create method exampleSix!!!")

if (hasattr(toFill, 'exampleSeven') and callable(getattr(toFill, 'exampleSeven'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a', 'b', 'c', 'd', 'e', 'f']
    if toFill.exampleSeven(testArray, "e") == [ 3, 4, 5, 6, 'q','e'] \
            and toFill.exampleSeven(testArray2, "g") == ['c','d','e','f','g']:
        print(7)
        score += 2

else:
    print("ATTN:!!!Please create method exampleSeven!!!")

print("YOUR SCORE IS : {}".format(score) )