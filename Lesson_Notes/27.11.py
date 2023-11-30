# How to solve GC - an alternative way

#fasta = open("~/Desktop/Programming/Rosalind/GC_training.txt")

## Working with dict
s = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
string_lines = s.split("\n")   #removing > and splitting string into lines


#Creating list of IDs & list of DNA sequences:
ID_list = []
seq_list = []
seq = ""

for line in string_lines:
    if ">" in line:
        ID_list.append(line[1:])
        seq_list.append(seq)
        seq = ""
    else:
        seq += line
seq_list.append(seq)
seq_list.remove("")

print(ID_list)
print(seq_list)

dict(zip(ID_list, seq_list))




#Creating list of IDs & list of DNA sequences: #### JAAAAAAA ########
ID_seq = {}

for line in string_lines:
    if ">" in line:
        ID_seq[line[1:]] = ""
        key = line[1:]
    else:
        ID_seq[key] += line

print(ID_seq)
