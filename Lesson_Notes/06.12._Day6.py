## Given: List of times, list of distances
## Want: product of number of ways we can beat all records

## Breaking down the problem:
    # i. product of ways
    # ii. finding ways to finish a race
    # iii. break record
    # iv. break all the records
    # v. extract data from file
  
    
## i. Getting product of a list
a_list = [1, 2, 3]
product = 1

for number in a_list:
    old_product = product
    product *= number
    print(old_product, "*", number, "=> new product:", product)
print("endproduct", product)


## iv. all races:
    # "for" all races -> for-loop



## ii. Way finish a race
    # Looking at first race: 7ms timeofrace, 9mm record
    
    # Press -> travel time, speed/acceleration
    # 0 -> 7, 0, 0
    # 1 -> 6, 1, 6
    # 2 -> 5, 2, 10  beat
    # 3 -> 4, 3, 12  beat
    # 4 -> 3, 4, 12  beat
    # 5 -> 2, 5, 10  beat
    # 6 -> 1, 6, 6
    # 7 -> 0, 7, 0


#Finding patterns:
    
    # button, traveltime, speed, distance, timeofrace
    # button = speed
    # number of button = timeofrace
    # traveltime = timeofrace - button
    # distance = traveltime * speed



### iii. How to know if I beat the record
dist_traveled = [0, 6, 10, 12, 12, 10, 6, 0]
record = 9

for way, dist in enumerate(dist_traveled):
    if dist > record:
        #print("Pressing the button for", way, "sec beats the record of", record, "mm with", dist, "mm")
        continue


### ii + iii. Trying to implement this in code for that one race

winning_buttons = []

def breaking_record(time_of_race, record_dist):
    
    for button in range(time_of_race):
        speed = button
        travel_time = time_of_race - button
        distance = travel_time * speed
        
        if distance > record:
            #print("Pressing the button for", button, "sec beats the record of", record, "mm with", distance, "mm")
            winning_buttons.append(button)

    return winning_buttons

#breaking_record(7, 9)




### iv. Winning all races
    # ideally I would like to have a dict with time_of_race : record
    # so looping through dict using breaking_record

times_of_races = [7, 15, 30]
all_records = [9, 40, 200]


## Making dictionary

times_records = {}
for time, record in zip(times_of_races, all_records):
    times_records[time] = record

#print(times_records)


## Looping through dict, implementing breaking_record on every key and its value
    ## saving results in dict with race_number as keys and list of winning_button_times as values

racenumber = 0
race_winningbuttons = {}

for time, record in times_records.items():
    #print("time:", time, "  record:", record)
    racenumber += 1
    #wins = breaking_record(time, record)
    #print(breaking_record(time, record))
    race_winningbuttons[racenumber] = breaking_record(time, record)

print(race_winningbuttons)
    

breaking_record(7, record_dist)
    

        



