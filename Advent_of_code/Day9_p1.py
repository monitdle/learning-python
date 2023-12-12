## For train of thought: https://github.com/monitdle/learning-python/blob/main/Lesson_Notes/Day9_Notes.py

#file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day9_input.txt", "r")
file = open("/Users/MoniLe/Desktop/Programming/learning-python/Advent_of_code/Day9_input.txt", "r")
sequences_file = file.read()
sequences_file = sequences_file.splitlines()


####################### Calculating differences ##############################

def diff(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if num2 > num1:
        diffNN = num2 - num1
    
    elif num2 == num1:
        diffNN = 0
    
    return diffNN



##############################################################################
############################ For all sequences ###############################


######### Make a dict with all sequences as keys #########
seq_hist = {}

for i, sequence in enumerate(sequences_file):
    seq_hist[f"{sequence}"] = {}


############### Calculating differences for all sequences ####################

for sequence in seq_hist.keys():
    



