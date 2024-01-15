# Overlap Graphs

file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/GRPH_input.txt", "r")
DataRaw = file.read()

### Step 1: Splitting & creating list
DataString = DataRaw.split("\n")    #split in lines


### Step 2: Creating lists of DNA strings and IDs - ATTENTION: one string can take multiple lines
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


IDlist = []
for ID in DataString:
    if "Rosalind_" in ID:   #every line with "Rosalind_" gets recognized as an ID line
        IDlist.append(ID[1:])  
#print(IDlist)


### Step 3: Create dictionary with DNA strings as keys and ID as values
DNA_ID = dict(zip(DNAstrings, IDlist))


### Step 4.1: Comparing first 3 aminoacids with last three aminoacids of another string
### Step 4.2: Printing out the paired DNA strings' IDs
for i in range(len(DNAstrings)):
    for DNA in DNAstrings:
        if DNAstrings[i] != DNA and DNAstrings[i][-3 : ] == DNA[0 : 3]:
            print(DNA_ID[DNAstrings[i]], DNA_ID[DNA])




############################################################################################################
##################################### Fresh Start, 14.01.2024 ##############################################

file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/GRPH_input.txt", "r")
DataRaw = file.read()
DataString = DataRaw.split("\n")    #split in lines


# Separating IDs and DNA:
ID_DNA = {}

for line in DataString:
    
    if ">" in line:
        ID = line.replace(">", "")
        ID_DNA[ID] = ""     #creates new key everytime an ID line is present
    
    elif ">" not in line:
        ID_DNA[ID] += line
        #will take last newly created ID & appends lines after that to its value until a new ID comes up


# comparing last 3 nucleobases of one string with first 3 nb of another string
for ID, DNA in ID_DNA.items():
    for ID2, DNA2 in ID_DNA.items():
        if ID != ID2 and DNA[-3:] == DNA2[:3]:
            print(ID, ID2)
        

    
    

