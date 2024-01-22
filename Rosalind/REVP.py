#### Reverse Palindrome ###

fasta = """>Rosalind_3089
GCGCTCGAGGCGGGGGATCTTGCCTCGGCTACAGGGCAGTACGCAACATCGGTTTATTCA
TTATTGTAAATTGTGTCCTCCCTTAAGAAAGCGTATCACGGGGAACCCTAGGGCGTCAGA
GCCCATACTTTAGCGAGCGGTCTGAAAAATTCCCATATTATGTATGGCTCTCCGCCTCCT
GGAGACAACAGTATCGAAGACTGGCCGAACGTCCGGCTTAATGTAAGCTCCGACTATGAC
TGTGTCGTCTAAAAGCCTCCAGGCACACGCGCACAATTTCACTGATGAGATGGAAGCAAT
TCTTAAGCGGCGCTATCAGCGGAATGGGGACATGATTGTCGCGAGGTCACCAGAGCAGTG
GCAAGGGTATAGCCCTGTATAACAGAAAACTTGGGCTTTGAACATGTTCACCCCTCTTCC
CTGGGGTGATGTGAGTCTTGTAGAACCGAACTGCACTAGTGTGAAACTTTTCTAATAAGT
CAGTTGCATGATCTGTCTACAATTCATGTTGATGGCGACTCTCGGTCTTTGGGACTGTCA
ACTCGCAGTTCTATTTTCATGCCGTTCTTCATAACCCCACTCGCGACCCCGAACAGGTTT
AGACCCCTTATATCAAAGGTGAGGCATACGATGAAGGTCTTCGCAGTAAGCCATGTGTTG
GATCCTCCATCGGAGTAGGGACACCTGGACAAGAAGGAAGTAGGGAAGCTTCACCGGAGG
ACCGCGACTATTTAGATTTTCAACCATTGATTTGGTTCACTTAGATCGGGTAAGGAGACA
ACAAGACAACAAACAGCCTTATGAGCGC"""

fasta_lines = fasta.splitlines()
DNA = "".join(line for line in fasta_lines if ">" not in line)


# Input: 1 DNA string
# Output: Position and length of RP with length between 4 and 12, no distinct order

# Reversed Palindrome RP: If reversed string's complement == string

ctable = str.maketrans("ATGC", "TACG")  #used in ORF, creates translation table A to T etc.
list_of_RPs = {}

for i, nb in enumerate(DNA):
    for end in range(4, 13):    #length 4 to 12
        frame = DNA[i : i + end]    #loop in loop: fixates first position, runs end position from 4 to 12
        cframe = frame.translate(ctable)[::-1]  #complement of reversed frame
        if len(frame) >= 4 and frame == cframe:     #if length more than 4, since at the end length can be shorter
            list_of_RPs[i + 1] = len(frame)

for length, position in list_of_RPs.items():
    print(length, position)





