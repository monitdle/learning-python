#file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day9_input.txt", "r")
file = open("/Users/MoniLe/Desktop/Programming/learning-python/Advent_of_code/Day9_input.txt", "r")
sequences_file = file.read()
sequences_file = sequences_file.splitlines()


##################### Breaking down the problem ##############################
## Input: sequences
## Output: next number of each sequence summed up
## Way: Calculate differences between each number with the next, then same with the number in differences until reaching 0


## Steps:
    # Calculate differences
    # Calculate differences of differences until 0
    # Extrapolate to get next number in sequence
    # Sum up extrapolations



####################### Calculating differences ##############################

def diff(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if num2 > num1:
        diffNN = num2 - num1
    
    elif num2 == num1:
        diffNN = 0
    
    return diffNN


## Testing out function on one sequence
test_sequence = sequences_file[2].split(" ")
history = {}
hist1 = []

for i, number in enumerate(test_sequence[1:]):
    hist1.append(diff(test_sequence[i], number))

#print(hist1)



############### Calculating differences of differences until 0 ###############
history["history1"] = hist1

for k in range(2, max(hist1)):
    histname = f"history{k}"

    for sequence in history.values():
        add_hist = []
        for i, number in enumerate(sequence[1:]):
            add_hist.append(diff(sequence[i], number))
    
    prev_histname = history[f"history{k - 1}"]
    
    if prev_histname != ([0] * len(prev_histname)):
        history[f"{histname}"] = add_hist
    
    else:
        break



############### Extrapolating to find next number in sequence ################
ep_diff = 0     #extrapolated difference

for value in history.values():
    for last_number in value[-1:]:
        ep_diff += last_number

for last_num_seq in test_sequence[-1:]:
    lns = int(last_num_seq)
        
ep = lns + ep_diff      #extrapolation = last number of sequence + sum of last numbers of all differences



##############################################################################
############################ For all sequences ###############################

# https://github.com/monitdle/learning-python/blob/main/Advent_of_code/Day9_p1.py








