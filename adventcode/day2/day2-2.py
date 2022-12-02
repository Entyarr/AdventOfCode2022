#op ----------- me
# a -  rock   - x - lose
# b -  paper  - y - draw
# c - scissor - z - win

score = 0

f = open("wha.txt", 'r')

lines = f.readlines()

for line in lines:
    items = line.split(' ')
    
    p = items[1].strip()
    e = items[0].strip()

    if(p == 'X'):
        if(e == 'A'):
            score += 3
        if(e == 'B'):
            score += 1
        if(e == 'C'):
            score += 2
    if(p == 'Y'):
        if(e == 'A'):
            score += 4
        if(e == 'B'):
            score += 5
        if(e == 'C'):
            score += 6
    if(p == 'Z'):
        if(e == 'A'):
            score += 8
        if(e == 'B'):
            score += 9
        if(e == 'C'):
            score += 7



print(score)
    
       
        



