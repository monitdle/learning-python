
file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day6_input.txt", "r")
time_record = (file.read()).splitlines()


## Reading in file correctly
time_record_dict = {}
record_list = []
time = ""
distance = ""

for i, line in enumerate(time_record):
    new_line = line.split("  ")
    
    if i == 0:
        for char in new_line:
            new_char = char.lstrip()
            if new_char.isdigit():
                time += new_char
                
    if i == 1:
        for char in new_line:
            new_char = char.lstrip()
            if new_char.isdigit():
                distance += new_char

time_record_dict[int(time)] = ""
record_list.append(int(distance)) 

for time, record in zip(time_record_dict.keys(), record_list):
    time_record_dict[time] = record

#print(time_record_dict)


## Define function for ways to win a race
def breaking_record(time_of_race, record_dist):
    winning_buttons = []
    
    for button in range(time_of_race):
        speed = button
        travel_time = time_of_race - button
        distance = travel_time * speed
        
        if distance > record_dist:
            #print("Pressing the button for", button, "sec beats the record of", record, "mm with", distance, "mm")
            winning_buttons.append(button)

    return winning_buttons


## Creating dictionary for every race with its list of ways to win
racenumber = 0
race_winningbuttons = {}

for time, record in time_record_dict.items():
    #print("time:", time, "  record:", record)
    racenumber += 1
    #wins = breaking_record(time, record)
    #print(breaking_record(time, record))
    race_winningbuttons[racenumber] = breaking_record(time, record)

print(len(race_winningbuttons[1]))
