#op ----------- me
# a -  rock   - x
# b -  paper  - y
# c - scissor - z

score = 0

f = open("wha.txt", 'r')

lines = f.readlines()

for line in lines:
    items = line.split(' ')
    
    p = items[1].strip()
    e = items[0].strip()

    if(p == 'X'):
        score += 1
    if(p == 'Y'):
        score += 2
    if(p == 'Z'):
        score += 3


    if((p == 'X' and e == 'C') or
       (p == 'Y' and e == 'A') or
       (p == 'Z' and e == 'B')):
        score += 6
        
    elif((p == 'X' and e == 'A') or
         (p == 'Y' and e == 'B') or
         (p == 'Z' and e == 'C')):
        score += 3


print(score)
    
       
        



