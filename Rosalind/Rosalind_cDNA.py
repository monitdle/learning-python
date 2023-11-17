# Rosalind: Complementary DNA
## First idea (that worked)
sequence = "AAAACCCGT"  #sequence given
sequence_list = list(sequence)  #create it into a list
sequence_reverse = sequence_list[::-1]  #create the list reverse
sequence_result = []    #create empty list for result
print(sequence_list)    #prints given list

for x in sequence_reverse:
    #checking if it's an A
    if x == "A":
        #putting T in list of results
        sequence_result.append("T")
    elif x == "T":
        sequence_result.append("A")
    elif x == "C":
        sequence_result.append("G")
    elif x == "G":
        sequence_result.append("C")
    else:
        sequence_result.append("N")

print(sequence_result)



## Second idea
sequence = "AAAACCCGT"
sequence_result = []
print(sequence)

for x in sequence[::-1]:    #getting rid of list creations & using splicing
    if x == "A":
        sequence_result.append("T")
    elif x == "T":
        sequence_result.append("A")
    elif x == "C":
        sequence_result.append("G")
    elif x == "G":
        sequence_result.append("C")
    else:
        sequence_result.append("N")

print("".join(sequence_result))     #making result list into a string (had to google that one)



## Third and best idea
sequence = "AAAACCCGT"
sequence_result = ""
print(sequence)

for x in sequence[::-1]:
    if x == "A":
        sequence_result += "T"  #like .append() but for strings which...
    elif x == "T":
        sequence_result += "A"
    elif x == "C":
        sequence_result += "G"
    elif x == "G":
        sequence_result += "C"
    else:
        sequence_result += "N"

print(sequence_result)  #...got rid of the googled function