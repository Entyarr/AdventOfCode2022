import string
lowerAlphabet = list(string.ascii_lowercase)
upperAlphabet = list(string.ascii_uppercase)
alphabet = lowerAlphabet + upperAlphabet
score = 0

f = open("wha.txt", 'r')
lines = f.readlines()

for line in lines:
    line = line.strip()
    halfLen = int(len(line)/2)
    lineLen = len(line)
    l_half = line[0:halfLen]
    r_half = line[halfLen:lineLen]

    for l in l_half:
        if l in r_half:
            score += alphabet.index(l)+1
            break

print(score)
                

    

