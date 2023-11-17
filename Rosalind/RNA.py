# Rosalind: RNA string
#we want to replace all "T" in DNA string with "U" for RNA string

DNA_string = "GATGGAACTTGACTACGTAAATT"
RNA_string = ""     #preparing an empty string for our RNA string

for nb in DNA_string:   #go through DNA string
    if nb == "T":   #check if it's a T base
        RNA_string += "U"   #if yes: put U base intro RNA string
    else:   #everything else will be put into RNA string as it is
        RNA_string += nb

print(RNA_string)

