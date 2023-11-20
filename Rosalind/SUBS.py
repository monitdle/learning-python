# Rosalind: Finding a Motif in DNA

#given: a DNA sequence, a shorter DNA string
#find where the shorter string is in longer one, can be multiple times
#Output: state position of shorter string by naming position of the first base
#position defined as all bases left to wanted base, INCL. that base

##########################################
# Example: 

long_string = "GATATATGCATATACTT"
short_string = "ATAT"

#Idea:
#[0, n], [0 +1, n + 1],…   for n = len(short_string)

next_position = 0
for i in range(len(long_string)):
    first_position = 0 + next_position
    substring = long_string[first_position : len(short_string) + next_position]
    if substring == short_string:
        print(first_position + 1, end = " ")
    next_position += 1
            
