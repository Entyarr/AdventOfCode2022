import string
lowerAlphabet = list(string.ascii_lowercase)
upperAlphabet = list(string.ascii_uppercase)
alphabet = lowerAlphabet + upperAlphabet

score = 0

f = open("wha.txt", 'r')
lines = f.readlines()

for i in range(0, len(lines)-1, 3):
    lines[i] = lines[i].strip()
    for one in lines[i]:
        if one in lines[i+1] and one in lines[i+2]:
            score += alphabet.index(one)+1
            break
print(score)
                

    

