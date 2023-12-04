file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day2_input.txt", "r")
games = (file.read()).splitlines()

sum_of_games = 0

for line, game in enumerate(games):
    game_parts = game.split(":")[1].strip()
    cube_games = {}
    
    tries = ""
    tries = game_parts.replace(",", "").split(";")      #Games in lists, every round in a string
    #print(tries)
    
    for k, grab in enumerate(tries):
        grab = grab.split(" ")      #split every game into only words, alternating between number and colour
        
        mycubes = {"red" : 12, "green" : 13, "blue" : 14}   #cubes we have in the bag
        for i, word in enumerate(grab):
            #print(word)                    #looping through words
            if len(word) > 2:               #to exclude numbers, only incl. colours
                #print(word, grab[i - 1], "***")
                grabbed_cubes = int(grab[i - 1])    #the colours number is one index before -> grab[i - 1]

                if word == "red":
                    mycubes[word] -= grabbed_cubes      #number of grabbed cubes substracted, per colour
                elif word == "blue":
                    mycubes[word] -= grabbed_cubes
                elif word == "green":
                    mycubes[word] -= grabbed_cubes
        cube_games[f"Game {line + 1}, Round {k + 1}"] = mycubes      #making dict for each Game and its round
        #print(cube_games)
        
    number_of_false = 0     #basically if even one round is negative, the number is > 0
    for game_grab, grab_dict in cube_games.items():  
        #print(grab_dict)
        if any(value < 0 for value in grab_dict.values()): 
            #print(line, "False")
            number_of_false += 1
        else:
            #print(line, "True")
            number_of_false += 0
               
    if number_of_false == 0:    #sum up all games IDs that don't have false rounds
        add = line + 1      #IDs are the number of the line + 1, since lists start with 0
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
    
    