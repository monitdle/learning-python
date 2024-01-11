file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/inProcess/MPRT_input.txt", "r")
DataRaw = file.read()
Datanames = DataRaw.splitlines()    #split in lines

# Removing e.g. _TRBM_HUMAN from P07204_TRBM_HUMAN
Databases = Datanames
for j, db in enumerate(Databases):
    for i, letter in enumerate(db):
        if letter == "_":
            Databases[j] = db[:i]
            break


### Opening all urls and extracting just the sequences by...
import requests

sequences = []
for db in Databases:
    fasta_url = f"https://rest.uniprot.org/uniprotkb/{db}.fasta"

    response = requests.get(fasta_url)
    content = response.text

    # ...removing the first line...
    contlines = content.splitlines()
    del contlines[0]

    # ...and joining the rest for the sequence
    seq = "".join(contlines)
    sequences.append(seq)


### Function for searching N-glycosylation  N{P}[ST]{P}
# {} any except
# [] or

def finding_NG(sequence):
    positions = []
    
    for i in range(len(sequence) - 3):
        
        if sequence[i] == "N" and sequence[i+1] != "P" and (sequence[i+2] == "S" or sequence[i+2] == "T") and sequence[i+3] != "P":
            pos = i + 1
            positions.append(pos)
    
    return positions
        
#print(finding_NG(sequences[2]))


######### TWO IDEAS #########
### 1. Creating dictionary for more structured and visually appealing printing
NGdict = {}
Datanames = DataRaw.splitlines()    #bc Datanames got overwritten somehow

for name in Datanames:
    NGdict[name] = []
    

## Combining the keys with their list of values
for seq, key in zip(sequences, NGdict):
    NGdict[key] = finding_NG(seq)
    
## Printing wanted Output
for key, value in NGdict.items():
    if value != []:
        print(key)
        for pos in value:
            print(pos, end = " ")
        print("")



### 2. Just print all in one loop
Datanames = DataRaw.splitlines()    #bc Datanames got overwritten somehow

for names, seq in zip(Datanames, sequences):
    pos_list = finding_NG(seq)
    
    if pos_list != []:
        print(names)
        for pos in pos_list:
            print(pos, end = " ")
        print("")            



