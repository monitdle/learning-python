file = open("/Users/MoniLe/Desktop/Programming/learning-python/Advent_of_code/Day2_input.txt")
games = (file.read()).splitlines()

sum_of_games = 0
loop = 0
for line, game in enumerate(games):
    game_parts = game.split(":")[1].strip()
    cube_games = {}
    #mycubes = {"red" : 12, "green" : 13, "blue" : 14}
    
    tries = ""
    tries = game_parts.replace(",", "").split(";")     #### look here
    #print(tries)
    
    for k, grab in enumerate(tries):
        grab = grab.split(" ")
        mycubes = {"red" : 12, "green" : 13, "blue" : 14}

        for i, word in enumerate(grab):
            #print(word)
            if len(word) > 2:
                #print(word, grab[i - 1], "***")
                grabbed_cubes = int(grab[i - 1])

                if word == "red":
                    mycubes[word] -= grabbed_cubes
                elif word == "blue":
                    mycubes[word] -= grabbed_cubes
                elif word == "green":
                    mycubes[word] -= grabbed_cubes
        cube_games[f"Game {line + 1}, Grab {k + 1}"] = mycubes
        #print(cube_games)
        
    valid = 0
    for game_grab, grab_dict in cube_games.items():  
        #print(grab_dict)
        if any(value < 0 for value in grab_dict.values()): 
            #print(line, "False")
            #adding = False
            valid += 1
        else:
            #print(line, "True")
            valid += 0
               
    if valid == 0:
        add = line + 1
        #print(add)
        sum_of_games += add
            
print(sum_of_games)
    
    
    
    
################## Part of first try #########################################  
#    
#    sentence = ""
#    sentence = game_parts.replace(",", "").replace(";", "").split()     #### look here
#    print(sentence)
#    for i, word in enumerate(sentence):
#        if len(word) > 2:
#            grabbed_cubes = int(sentence[i - 1])
#
#            if word == "red":
#                mycubes[word] -= grabbed_cubes
#            elif word == "blue":
#                mycubes[word] -= grabbed_cubes
#            elif word == "green":
#                mycubes[word] -= grabbed_cubes
#    #print(mycubes)
#    if all(value > 0 for value in mycubes.values()): 
#        print(mycubes, line)
#        add = line + 1
#        sum_of_games += add
#            
#print(sum_of_games)


# misunderstood: semicolon means put back
    
    