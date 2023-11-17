# Rosalind: GC-content

## First idea
#but it didn't work with the Dataset I got
#Already knew the seq_list is too relative, well..
s = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
string_lines = s.replace(">", "").split("\n")   #removing > and splitting string into lines


#Creating list of IDs:
ID_list = []
for ID in string_lines:
    if "Rosalind_" in ID:   #every line with "Rosalind_" gets recognized as an ID line
        ID_list.append(ID)  
        string_lines.remove(ID)    #remove ID lines for easier steps forward
#print(ID_list)


#Creating list of DNA sequences:
seq_list = []
for subseq in range(len(list(string_lines))):
    #looking at the even lines since they are the first part of the sequence:
    if subseq % 2 == 0:
        #putting those lines together with their second part
        seq_list.append(string_lines[subseq] + string_lines[subseq + 1])
    else:
        continue
#print(seq_list)


#Calculating GC content:
GC_list = []    #creating GC list
for seq in seq_list:
    counter = 0
    for base in seq:
        if base == "G" or base == "C":  #only counting G & C
            counter += 1
        else:
            continue
    GC_value = (counter / len(seq)) * 100   #calculating their percentage of the sequence
    GC_list.append(GC_value)
    

#Printing right Output:
highest_GC = max(GC_list)  #looking for highest GC in seq_list
rounded_GC = "{:.6f}".format(max(GC_list))     #Google, rounds 6 digits after decimal
#print("%s\n%s" % (ID_list[GC_list.index(highest_GC)], rounded_GC))     #w3: had to do this or else the output would not worked bc of int or had a space when using comma



#####################################################################################
#####################################################################################
############################# Second and working idea ###############################
#####################################################################################
#####################################################################################

s = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

string_lines = s.replace("\n", "").split(">")   #split by > and putting everything in one line
string_lines.remove("")


###Calculating GC content:
GC_list = []    #creating GC list

for seq in string_lines:
    counter = 0
    for base in seq:
        if base == "G" or base == "C":  #only counting G & C
            counter += 1
        else:
            continue
    GC_value = (counter / (len(seq)-13)) * 100   #calculating their percentage of the sequence, minus Rosalind_XXXX
    GC_list.append(GC_value)
    
#print(GC_list)


###Creating ID List:
string_lines2 = s.replace(">", "").split("\n")  #spliting into lines and removing >

ID_list = []
for ID in string_lines2:
    if "Rosalind_" in ID:   
        ID_list.append(ID)  
        string_lines2.remove(ID)

#print(ID_list)


###Printing right Output:
highest_GC = max(GC_list)  #looking for highest GC in seq_list
rounded_GC = "{:.6f}".format(max(GC_list))     #Google, rounds 6 digits after decimal
print("%s\n%s" % (ID_list[GC_list.index(highest_GC)], rounded_GC))     #w3: had to do this or else the output would not worked bc of int or had a space when using comma
