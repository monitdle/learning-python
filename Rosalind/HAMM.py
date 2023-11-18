# Hamming Distance

#Given two strings s and t of equal length
#the Hamming distance dH(s,t) = the number of different bases between them

###### Solution #######

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
counter = 0

for x in range(len(s)):    #working with indeces
    if s[x] == t[x]:
        continue
    else:
        counter += 1

print(counter)




## Something new
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
counter = 0

for (x, y) in zip(s, t):    #I really wanted a function that allows me to work with 2 samples in a for-loop (Google)
        if x == y:
            continue
        else:
            counter += 1

#print(counter)

