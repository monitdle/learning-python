## For train of thought: https://github.com/monitdle/learning-python/blob/main/Lesson_Notes/Day9_Notes.py

file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day9_input.txt", "r")
#file = open("/Users/MoniLe/Desktop/Programming/learning-python/Advent_of_code/Day9_input.txt", "r")
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

for i, sequence in enumerate(sequences_file):
    seq_hist[f"{sequence}"] = {}


############### Calculating differences for all sequences ####################

for sequence in seq_hist.keys():
    seq = sequence.split(" ")
    
    for k in range(1, int(max(seq))):
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
    

############### Extrapolating to find next number in sequence ################
sum_ep = 0

for sequence, history in seq_hist.items():
    ep_diff = 0                             #extrapolated differences
    for value in history.values():
        for i, last_number in enumerate(value[-1:]):
            ep_diff += last_number          #sum up all last differences of each history
    
    for last_num_seq in sequence.split(" ")[-1:]:
        lns = int(last_num_seq)
        
    ep = lns + ep_diff      #extrapolation = last number of sequence + sum(last numbers of all differences)
    sum_ep += ep

print(sum_ep)

# 1685665928 ... too high
# 1680103424 ... too high
# 1647195430 ... too low

