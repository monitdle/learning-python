## For train of thoughts: https://github.com/monitdle/learning-python/blob/main/Lesson_Notes/06.12._Day6.py

file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day9_input.txt", "r")
sequences_file = file.read()
sequences_file = sequences_file.splitlines()


###### Breaking down the problem ######
## Input: sequences
## Output: next number of each sequence summed up
## Way: Calculate differences between each number with the next, then same with the number in differences until reaching 0


## Steps:
    # Calculate differences
    # Calculate differences of differences until 0
    # Extrapolate to get next number in sequence
    # Sum up extrapolations


##### Calculating differences #####

def diff(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if num2 > num1:
        diffNN = num2 - num1
    
    elif num2 == num1:
        diffNN = 0
    
    return diffNN


## Testing out function on one sequence
test_sequence = sequences_file[0].split(" ")
history1 = []

for i, number in enumerate(test_sequence[1:]):
    history1.append(diff(test_sequence[i], number))

print(history1)



##### Calculating differences of differences until 0 #####
test_sequence = sequences_file[1].split(" ")
history = {}
hist1 = []

for i, number in enumerate(test_sequence[1:]):
    hist1.append(diff(test_sequence[i], number))
    
history["history1"] = hist1

add_hist = []
while 0 not in add_hist:
    
    for k in range(2, max(hist1)):
        histname = f"history{k}"
        add_hist = []

        for sequence in history.values():
            for i, number in enumerate(sequence[1:]):
                add_hist.append(diff(sequence[i], number))
        history[f"{histname}"] = add_hist
