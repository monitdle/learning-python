# Open Reading Frames

rawdata = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGAC
TTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""

## Difference Reading frame as in Leseraster vs. Reading frame translation Leserahmen:
#URL: https://de.wikipedia.org/wiki/Leseraster
#6 possible Reading frames: start with first 3, second 3 or third 3
    # -> plus same of the Reverse strand

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



## Step 1: Filter out the DNA string, inspired by GC from 27.11.:
string_lines = rawdata.split("\n")
DNA_string = ""
    
for line in string_lines:
    if ">" in line:
        continue
    else:
        DNA_string += line
#print(DNA_string)
  

## Step 2: Using code for Transkription from RNA:
RNA_string = ""     #preparing an empty string for our RNA string

for nb in DNA_string:   #go through DNA string
    if nb == "T":   #check if it's a T base
        RNA_string += "U"   #if yes: put U base intro RNA string
    else:   #everything else will be put into RNA string as it is
        RNA_string += nb

#print(RNA_string)



## Step 3.1: Creating different triplets aka Reading frames

RNA_triplets1 = []
triplet = ""
for i, nb in enumerate(RNA_string):
    if i % 3 == 0:
        RNA_triplets1.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets1.remove("")
#print(RNA_triplets1)

        

RNA_triplets2 = []
triplet = ""

for i, nb in enumerate(RNA_string[1:]):
    if i % 3 == 0:
        RNA_triplets2.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets2.remove("")
#print(RNA_triplets2)


RNA_triplets3 = []
triplet = ""

for i, nb in enumerate(RNA_string[2:]):
    if i % 3 == 0:
        RNA_triplets3.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets3.remove("")
#print(RNA_triplets3)



## Step 3.2: Creating the reverse reading frames
### Taking from REVC:
DNArev_string = ""
#print(DNA_string)

for k in DNA_string[::-1]:
    if k == "A":
        DNArev_string += "T"  #like .append() but for strings which...
    elif k == "T":
        DNArev_string += "A"
    elif k == "C":
        DNArev_string += "G"
    elif k == "G":
        DNArev_string += "C"
    else:
        DNArev_string += "N"

#print(DNArev_string)  #...got rid of the googled function


RNA_reverse = ""     #preparing an empty string for our RNA string

for nb in DNArev_string:   #go through DNA string
    if nb == "T":   #check if it's a T base
        RNA_reverse += "U"   #if yes: put U base intro RNA string
    else:   #everything else will be put into RNA string as it is
        RNA_reverse += nb
        

RNA_triplets1_rev = []
triplet = ""
for i, nb in enumerate(RNA_reverse):
    if i % 3 == 0:
        RNA_triplets1_rev.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets1_rev.remove("")
#print(RNA_triplets1_rev)


RNA_triplets2_rev = []
triplet = ""
for i, nb in enumerate(RNA_reverse[1:]):
    if i % 3 == 0:
        RNA_triplets2_rev.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets2_rev.remove("")
#print(RNA_triplets2_rev)


RNA_triplets3_rev = []
triplet = ""
for i, nb in enumerate(RNA_reverse[2:]):
    if i % 3 == 0:
        RNA_triplets3_rev.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets3_rev.remove("")
#print(RNA_triplets3_rev)


## Step 3.3: Uniting all RNA triplets

RNA_all_triplets = [RNA_triplets1] + [RNA_triplets2] + [RNA_triplets3] + [RNA_triplets1_rev] + [RNA_triplets2_rev] + [RNA_triplets3_rev]



## Step 4: Translation function

def translation(target):
    start_translation = False
    proteinstring = ""

    for triplet in target:
        if triplet == "AUG":
            start_translation = True
            
        if start_translation:
            aminoacid = codontable[triplet]
            if aminoacid == "Stop":
                break
            proteinstring += aminoacid
    return proteinstring

     
## Step 5: Printing all Translations       
for string in RNA_all_triplets:
    print(string)
    print(translation(string))









