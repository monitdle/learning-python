file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/SPLC_input.txt", "r")
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


### Searching for N-glycosylation  N{P}[ST]{P}
# {} any except
# [] or

def finding_Ng(sequence):
    positions = []
    
    for i, abc in enumerate(sequence):
        
        if abc == "N" and sequence[i + 1] != "P" and sequence[i + 2] == ("S" or "T") and sequence[i + 3] != "P":
            pos = i + 1
            positions.append(pos)
        
    return positions
            

for seq in sequences:
     print(finding_Ng(seq))
        

