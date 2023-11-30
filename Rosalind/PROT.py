 
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

# Example:
RNAstring = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

#it is very similar to SUBS solution
#so we still look at it as using a scanner to scan a segment and moving the scanner base by base

movement = 0
for i in range(len(RNAstring)):
    start = 0 + movement
    segment = RNAstring[start : 3 + movement]
 #now we look if the scanned segment is in the dict
    if codontable[segment] == "Stop": #if the value is Stop, the scanning will end
        break
    else:
        print(codontable[segment], end = "")  #if the segment is in the dict, print it, separator is space
        movement += 2   #if printed, the scanner has to move 3 steps, since 3 bases make 1 letter, so 2...
    movement += 1           #...plus 1; if not printed the scanner will only be moved 1 base
