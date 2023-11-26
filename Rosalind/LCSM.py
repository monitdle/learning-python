# Finding a Shared Motif

DataRaw = """>Rosalind_1
GATT
ACAT
>Rosalind_2
TAGACA
AGATT
>Rosalind_3
ATACAGATT"""

## Step 1: Splitting & creating lists
DataString = DataRaw.split("\n")    #split in lines
DataString_remv = DataRaw.replace(">", "").split("\n")


## Step 2: Creating lists of DNA strings - ATTENTION: one string can take multiple lines
DNAstrings = []
subseq = ""
for item in DataString[1:]:
    if item[0] != ">":  #lines without > get recognized as DNA strings
        subseq += item
    else:
        DNAstrings.append(subseq)   #>-lines signal the end of a DNA string & append to list
        subseq = ""
        continue
DNAstrings.append(subseq)   #append last DNA string
#print(DNAstrings)


## Step 3: Look for common substring
#take shortest string as template string
#fixate first base, look for longer segments of after that base, creating longer substrings
    #check if any of them are present in EVERY other strings
#move on to next base, repeat
#only if substring is in EVERY string and is longer than current common substring, can it become the current common substring

comSubstr = ""
template = min(DNAstrings, key = len)

for i in range(len(template)):
    for j in range(i + 1, len(template)):
        currSubstr = template[i : j]
        #print(f"The current substring is {currSubstr}")
        if all(currSubstr in strings for strings in DNAstrings) and len(comSubstr) < len(currSubstr):
            comSubstr = currSubstr
            #print(f"The current common substring is {comSubstr}")

#print(f"The longest common substring is {comSubstr}")
print(comSubstr)        

