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



string_lines = rawdata.split("\n")



DNA_string = ""
    
for line in string_lines:
    if ">" in line:
        continue
    else:
        DNA_string += line
#print(DNA_string)




DNArev_string = ""

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



frame1 = DNA_string.replace("T", "U")
frame2 = frame1[1:]
frame3 = frame1[2:]
frame4 = DNArev_string.replace("T", "U")
frame5 = frame4[1:]
frame6 = frame4[2:]



RNA_triplets1 = []
triplet = ""
for i, nb in enumerate(frame1):
    if i % 3 == 0:
        RNA_triplets1.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets1.remove("")
#print(RNA_triplets1)

        

RNA_triplets2 = []
triplet = ""

for i, nb in enumerate(frame2):
    if i % 3 == 0:
        RNA_triplets2.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets2.remove("")
#print(RNA_triplets2)


RNA_triplets3 = []
triplet = ""

for i, nb in enumerate(frame3):
    if i % 3 == 0:
        RNA_triplets3.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets3.remove("")
#print(RNA_triplets3)




RNA_triplets1_rev = []
triplet = ""
for i, nb in enumerate(frame4):
    if i % 3 == 0:
        RNA_triplets1_rev.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets1_rev.remove("")
#print(RNA_triplets1_rev)


RNA_triplets2_rev = []
triplet = ""
for i, nb in enumerate(frame5):
    if i % 3 == 0:
        RNA_triplets2_rev.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets2_rev.remove("")
#print(RNA_triplets2_rev)


RNA_triplets3_rev = []
triplet = ""
for i, nb in enumerate(frame6):
    if i % 3 == 0:
        RNA_triplets3_rev.append(triplet)
        triplet = nb
    else:
        triplet += nb
RNA_triplets3_rev.remove("")
#print(RNA_triplets3_rev)




RNA_all_triplets = [RNA_triplets1] + [RNA_triplets2] + [RNA_triplets3] + [RNA_triplets1_rev] + [RNA_triplets2_rev] + [RNA_triplets3_rev]



### Finding AUGs
for string in RNA_all_triplets:
    for i, start in enumerate(string):
        if start == "AUG":
            print(i)


## Step 4: Translation function

def translation(target):
    start_translation = False
    proteinstring = ""

    for i, triplet in enumerate(target):
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



##### Idea: look at indices of Start- & Stoppcodons: pick smallest Stopp which is still larger than Start

