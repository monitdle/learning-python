# Open Reading Frames
file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/ORF_input.txt", "r")
DataRaw = file.read()
string_lines = DataRaw.split("\n")[1:]



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


## 1) DNA string and complementary DNA string & putting all frames into dict
DNA = "".join(string_lines)

ctable = str.maketrans("ATGC", "TACG")  #creates translation table A to T etc.
cDNA = DNA.translate(ctable)[::-1]  #complementary DNA has to be read in reverse

RNA = DNA.replace("T", "U")
cRNA = cDNA.replace("T", "U")


# For different reading frames, here translation starts at index 1
RNA1 = RNA[1:]      
cRNA1 = cRNA[1:]

# Translation starts at index 2
RNA2 = RNA[2:]      
cRNA2 = cRNA[2:]

# list with all frames:
frames = [RNA, RNA1, RNA2, cRNA, cRNA1, cRNA2]   


## 2) Translate them into amino acids    
proteins = []    
    
for seq in frames:
    translation_active = False  #ensures that translation only starts after an AUG is found
    protein = ""        #resets protein for each frame
    rest = len(seq) % 3     #to ensure that all triplets are len(triplet) = 3, no error message
    
    for i in range(0, len(seq) - rest, 3):  #basically range(len(seq)) but in steps of 3
        triplet = seq[i : i + 3]
        aa = codontable[triplet]    #translation into amino acids
 #       print(triplet, aa, name)
        
        if aa == "M":       #alternative: if triplet == "AUG"
            protein += aa
            translation_active = True   #sign to start translation = activates elif-statements
        
        elif aa == "Stop" and translation_active == True:
            proteins.append(protein)    #save protein then break off inner for-loop
            break
        
        elif translation_active == True:  #main translation here
            protein += aa


    # Problem: When a protein includes another AUG, it has to be translated again starting at that AUG
        # so here I'm just slicing it, starting at all the M positions in the long protein
    if protein.count("M") > 1:
        #creating list & searching for very position with M, except first M since its the long protein we already have
        positions = [i for i, nb in enumerate(protein) if nb == "M" and i != 0]
        
        for pos in positions:
            proteins.append(protein[pos:])  #slicing using our position list


for string in set(proteins):    #set() doesn't give out doubles, distinctions
    print(string)











