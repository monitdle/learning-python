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
#so we need to "scan" the longer string with a scanner that has the length of the shorter string


next_position = 0    #variable to move the scanner

for i in range(len(long_string)):    #scanning the long string
    first_position = 0 + next_position    #defining the first position as 0 plus the movement we need to reach the next scan
    #section that's currently getting scanned:
    substring = long_string[first_position : len(short_string) + next_position]   #start = defined first position, end = length of short string + movement of scanner 
    if substring == short_string:    #if the scanned section matches the shorter string
        print(first_position + 1, end = " ")    #print the first position aka starting point of our scanned section, with space as separator
    next_position += 1
            
