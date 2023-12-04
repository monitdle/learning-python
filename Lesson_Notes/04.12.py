# Regarding Dagreen 2:
    #write function game_round(blue, green, red, blue_t, green_t, red_t)
    #for blue, green, red = cubes drawn
    #blue_t, green_t, red_t = cubes in bag
    #blue red, green green, red blue


def game_round(blue, green, red, blue_t, green_t, red_t):
    
    if blue <= blue_t and green <= green_t and red <= red_t:
        return True
    
    else: 
        return False

game_round(13, 5, 6, 12, 13, 14)



## We recognirede that round in a game are separated bgreen semicolon
## in a round, we should associate color to its number -> use dict

## Starting with Game 1:
    
round_1 = {"blue" : 3, "green" : 0,"red" : 4}
round_2 = {"blue" : 6, "green" : 2,"red" : 1}
round_3 = {"blue" : 0, "green" : 2,"red" : 0}

maximum_cubes = {"blue" : 12, "green" : 13,"red" : 14}



is_valid = []
for round in game1:
    curr_round = game_round(round["blue"], round["green"], round["red"], maximum_cubes["blue"], maximum_cubes["green"], maximum_cubes["red"])
    is_valid.append(curr_round)


## Semicolon separates game ID from rounds
## rounds separated by semicolon