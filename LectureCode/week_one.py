

file =  open('tst.csv', 'r')
data = []
lines = file.readlines()
for line in lines:
    line = line.strip()
    accounts = line.split(';')
    for account in accounts:
        data.append(account + '\n')

file.close()

fileWrite = open('magic.csv', 'w')
fileWrite.writelines(data)
fileWrite.close()