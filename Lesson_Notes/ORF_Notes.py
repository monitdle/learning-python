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
        
    
    

############################################################################################################
############################################### 01.12.2023 #################################################
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

