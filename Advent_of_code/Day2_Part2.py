file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day2_input.txt", "r")
games = (file.read()).splitlines()

sum_of_power = 0

for line, game in enumerate(games):
    game_parts = game.split(":")[1].strip()

    tries = ""
    tries = game_parts.replace(",", "").split(";")
    
    game_dict = {"red": 0, "green" : 0, "blue" : 0}
    
    #print("************************")  #separates games

    for k, grab in enumerate(tries):
        #print("___________")           #separates rounds
        grab = grab.split(" ")
        #print(grab)
        
        for i, word in enumerate(grab):
            
            if len(word) > 2:
                number = int(grab[i - 1])   #number of cubes of a colour is before said colour
                
                if word == "red" and number > game_dict[word]:  #only added to dictionary if new number > old number
                    game_dict[word] = number
                elif word == "green" and number > game_dict[word]:
                    game_dict[word] = number
                elif word == "blue" and number > game_dict[word]:
                    game_dict[word] = number
    
    #print("\n", "=>", game_dict, "\n\n")     #dictionary for min. number of cubes needed per game
    
    power = game_dict["red"] * game_dict["green"] * game_dict["blue"]   #calculating power
    sum_of_power += power      #added to sum of powers

print(sum_of_power)
        


## Note: I could have just worked with that in the loop above, but that would increase the number of nested loops

