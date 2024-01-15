# Open Reading Frames
file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/ORF_input.txt", "r")
DataRaw = file.read()
string_lines = DataRaw.split("\n")


## Difference Reading frame as in Leseraster vs. Reading frame translation Leserahmen:
#URL: https://de.wikipedia.org/wiki/Leseraster
#6 possible Reading frames: start with first 3, second 3 or third 3
    # -> same with the Reverse strand
    # => 6 Reading frames

## Using codontable from PROT:
codontable = {"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "UUA":"L", "UUG":"L", 
            "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", 
            "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "AGU":"S", "AGC":"S", 
            "GCC":"A", "GCU":"A", "GCA":"A", "GCG":"A", 
            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", 
            "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", 
            "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", 
            "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", 
            "AUU":"I", "AUC":"I", "AUA":"I", 
            "UUU":"F", "UUC":"F", 
            "GAU":"D", "GAC":"D", 
            "GAA":"E", "GAG":"E",
            "AAA":"K", "AAG":"K", 
            "AAU":"N", "AAC":"N", 
            "CAU":"H", "CAC":"H", 
            "UAU":"Y", "UAC":"Y", 
            "UGU":"C", "UGC":"C", 
            "CAA":"Q", "CAG":"Q", 
            "UGG":"W", 
            "AUG":"M", 
            "UAA":"Stop", "UAG":"Stop", "UGA":"Stop"}


### We need:
    # 1) DNA string and its complementary string => to RNA
    # 2) Reading each string in 3 different ways
    # 3) Translate them into amino acids


## 1) DNA string and complementary DNA string
DNA = string_lines[1]

ctable = str.maketrans("ATGC", "TACG")  #creates translation table A to T etc.
cDNA = DNA.translate(ctable)

RNA = DNA.replace("T", "U")
cRNA = cDNA.replace("T", "U")



## 2) Reading strands in different ways

all_triplets = {"RNA":[], "RNA1":[], "RNA2":[], "cRNA":[], "cRNA1":[], "cRNA2":[]}

def triplets(strand):
    
    
    for i, nb in enumerate(strand):
        
        if i % 3 == 0 and i != 0:
            triplet = strand[i - 3 : i]
            all_triplets[strand].append(triplet)


    for i, nb in enumerate(strand[1:]):
        
        if i % 3 == 0 and i != 0:
            triplet = strand[i - 3 : i]
            all_triplets[f"{strand}1"].append(triplet)

    
    for i, nb in enumerate(strand[2:]):
    
        if i % 3 == 0 and i != 0:
            triplet = strand[i - 3 : i]
            all_triplets[f"{strand}2"].append(triplet)
    
    
    return all_triplets

print(triplets(RNA))



## 3) Translate them into amino acids    
all_proteins = {"RNA":"", "RNA1":"", "RNA2":"", "cRNA":"", "cRNA1":"", "cRNA2":""}

for i, nb in enumerate(RNA[1:]):
    RNA = RNA[1:]
    
    if i % 3 == 0 and i != 0:
        triplet = RNA[i - 3 : i]

        if triplet == "AUG":
            all_proteins["RNA"] += "M"

    if all_proteins["RNA"] != "" and codontable[triplet] not in ["Stop", "M"]:
        all_proteins["RNA"] += codontable[triplet]
        
    elif codontable[triplet] == "Stop":
        break

protein = ""
    
for nb in range(3, len(RNA)):
    triplet = strand[nb - 3 : nb]
    aa = codontable[triplet]
    
    if aa == "Stop":
        break
        
    else:
        protein += aa
        
    
    
