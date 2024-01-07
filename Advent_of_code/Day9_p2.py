## For train of thought: https://github.com/monitdle/learning-python/blob/main/Lesson_Notes/Day9_Notes.py

#file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day9_input.txt", "r")
file = open("/Users/lemon/Desktop/Programming/learning-python/Advent_of_code/Day9_input.txt", "r")
sequences_file = file.read()
sequences_file = sequences_file.splitlines()


####################### Calculating differences ##############################

def diff(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    diffNN = num2 - num1

    return diffNN


##############################################################################
############################ For all sequences ###############################


######### Make a dict with all sequences as keys #########
seq_hist = {}

for sequence in sequences_file:
    seq_hist[f"{sequence}"] = {}


############### Calculating differences for all sequences ####################

for sequence in seq_hist.keys():
    seq = sequence.split(" ")
    
    for k in range(1, len(seq)):
        history = f"history{k}"
        hist = f"hist{k}"
        hist = []
        seq_hist[sequence][f"{history}"] = []

        for i, number in enumerate(seq[1:]):    #so the name starts at "history1" not "0"
            #print(seq[i], number)
            hist.append(diff(seq[i], number))
        
        if seq != ([0] * len(seq)):
            seq_hist[sequence][f"{history}"] = hist
        
        else:
            del seq_hist[sequence][f"{history}"]    #that way no empty dict is created
            break
        
        seq = hist      #using name "seq" as the last history until a new seq starts
    

############ Extrapolating to find the number BEFORE the sequence #############
sum_back_ep = 0

for sequence, history in seq_hist.items():
    new_ep_diff = 0      #new extrapolated difference
    last_ep_diff = 0     #last extrapolated difference
    for value in reversed(history.values()):
        new_ep_diff = value[0] - last_ep_diff    #new extrapolated difference = first value of history - last extrapolated difference
        last_ep_diff = new_ep_diff
        
    fns = int(sequence.split(" ")[0])       #first number of sequence
        
    back_ep = fns - new_ep_diff      #extrapolation = first number of sequence - newest extrapolated difference of history
    sum_back_ep += back_ep

print(sum_back_ep)



