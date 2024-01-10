### Problem
# DNA string with exons & introns
# Delete introns and translate rest of string in protein string

## Given:
    # DNA string and intron strings in FASTA
## Return:
    # Proteinstring, from exons

file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/SPLC_input.txt", "r")
DataRaw = file.read()


## Steps:
    # i. Identify DNA strings and introns
    # ii. Find introns in DNA string
    # iii. Remove introns from DNA string
    # iv. Translate DNA string rest into protein (RNA, PROT)


### ii. + iii. -> Thought: find intron AND remove it, move on to next

DataString = DataRaw.split("\n")    #split in lines
DataString = DataRaw.replace(">", "").split("\n")


sequences = []
subseq = ""
for item in DataString[1:]:
    if item[0] != ">":  #lines without > get recognized as DNA strings
        subseq += item
    else:
        sequences.append(subseq)   #>-lines signal the end of a DNA string & append to list
        subseq = ""
        continue
sequences.append(subseq)   #append last DNA string


## Function for finding start and end of intron within DNAstring
def find_intron(gene, intron):
    
    for i in range(len(gene)):
        if gene[i : i + len(intron)] == intron:
            return [i, i + len(intron)]    


## Finding and removing each intron after each other
for seq in introns:
    ind = find_intron(DNAstring, seq)
    if isinstance(ind, list):
        DNAstring = DNAstring[:ind[0]] + DNAstring[ind[1]:]

final_DNAstring = DNAstring


### iv. DNA -> RNA    => "RNA.py"
RNAstring = ""

for nb in final_DNAstring:   #go through DNA string
    if nb == "T":   #check if it's a T base
        RNAstring += "U"   #if yes: put U base intro RNA string
    else:   #everything else will be put into RNA string as it is
        RNAstring += nb


## RNA -> Protein    => "PROT.py"
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


movement = 0
for i in range(len(RNAstring)):
    start = 0 + movement
    segment = RNAstring[start : 3 + movement]
 #now we look if the scanned segment is in the dict
    if len(segment) != 3:   #if segment less than 3 nb, stop scan
        break
    elif codontable[segment] == "Stop": #if the value is Stop, the scanning will end
        break
    else:
        print(codontable[segment], end = "")  #if the segment is in the dict, print it, separator is space
        movement += 2   #if printed, the scanner has to move 3 steps, since 3 bases make 1 letter, so 2...
    movement += 1           #...plus 1; if not printed the scanner will only be moved 1 base






