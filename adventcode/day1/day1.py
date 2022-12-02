f = open("wha.txt", 'r')
calCount = 0
elves = []

lines = f.readlines()
last = lines[-1]


for line in lines:
    if(line.strip() == ""):
        elves.append(calCount)
        calCount = 0
    else:
        calCount += int(line)

    if(line == last):
        elves.append(calCount)
        
print(max(elves))




       
