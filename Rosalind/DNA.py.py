# Rosalind: Counting DNA Bases
DNA_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
counting_nb = {"A" : 0, "T" : 0, "C" : 0, "G" : 0}  #creating dict with bases


for nb in DNA_string:
    counting_nb[nb] += 1    #add 1 to value of key (=base) for every counted base in DNA string

#printing out only the values:
print(counting_nb["A"], counting_nb["C"], counting_nb["G"], counting_nb["T"])