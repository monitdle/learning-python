# Finding Most Likely Common Ancestor

## Example
DataRaw = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGAAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""

### Step 1: Splitting & creating list
DataString = DataRaw.split("\n")


### Step 2: Creating list with lists (DNA strings) - ATTENTION: one string can take multiple lines
DNAstrings = []
subseq = ""
for item in DataString[1:]:
    if item[0] != ">":
        subseq += item
    else:
        DNAstrings.append(subseq)
        subseq = ""
        continue
DNAstrings.append(subseq)
#print(DNAstrings)
        
        

### Step 3: Creating list with Profile
Profile = []
for i in range(len(DNAstrings[0])):
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for aminoacid in DNAstrings:
        if aminoacid[i] == "A":
            countA += 1
        elif aminoacid[i] == "C":
            countC += 1
        elif aminoacid[i] == "G":
            countG += 1
        elif aminoacid[i] == "T":
            countT += 1
    Profile.append([countA, countC, countG, countT])
#print(Profile)


### Step 4: Consensus list
for number in Profile:
    if max(number) == number[0]:
        print("A", end="")
        continue
    elif max(number) == number[1]:
        print("C", end="")
        continue
    elif max(number) == number[2]:
        print("G", end="")
        continue
    elif max(number) == number[3]:
        print("T", end="")
        continue
        
#### Separate Step 4 and 5
print()


### Step 5: Print Profile with names of aminoacids with Consensus
Names = [["A:", "C:", "G:", "T:"]]
ProfileNames = Names + Profile
for i in range(len(ProfileNames[0])):
    for value in ProfileNames:
        print(value[i], end=" ")
    print()


