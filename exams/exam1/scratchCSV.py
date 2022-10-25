# file = open("firstCSV.csv","w")
# header =    "Class,Term,Grade\n"
# firstRow  = "F6520,F20, 4.0\n"
# otherRow =  ["ACCTG6510,F20, 4.0\n",
#              "FINAN6360,F20, 3.6\n",
#              "WINES1010,F20, 3.0\n"]
# file.write(header)
# file.write(firstRow)
# file.writelines(otherRow)
# file.close()

file = open("firstCSV.csv","r")
rows = file.readlines()
dict = {"Major":[]}
for row in rows[1:]:
    row = row.strip()
    columns = row.split(",")#DO NOT DO THIS IN YOUR HOMEWORK, BUT DO THIS IN YOUR EXAM
    colA = columns[0]
    colB = columns[1]
    colC = float(columns[2])
    if "F" in colA:
        nElements = dict["Major"]
        #nElements.append(colC) = nElements
        dict["Major"] = nElements + [colC]

nElementsComplete = dict["Major"]
average = sum(nElementsComplete) / len(nElementsComplete)
print(dict)
file.close()