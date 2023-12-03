file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day2_input.txt")
games = (file.read()).splitlines()

sum_of_games = 0
loop = 0
for line, game in enumerate(games):
    game_parts = game.split(":")[1].strip()
    cube_games = {}
    mycubes = {"red" : 12, "green" : 13, "blue" : 14}
    
    sentence = ""
    sentence = game_parts.replace(",", "").replace(";", "").split()
    #print(sentence)
    for i, word in enumerate(sentence):
        if len(word) > 2:
            grabbed_cubes = int(sentence[i - 1])

            if word == "red":
                mycubes[word] -= grabbed_cubes
            elif word == "blue":
                mycubes[word] -= grabbed_cubes
            elif word == "green":
                mycubes[word] -= grabbed_cubes
    #print(mycubes)
    if all(value > 0 for value in mycubes.values()): 
        print(mycubes, line)
        add = line + 1
        sum_of_games += add
            
print(sum_of_games)


# missunderstood: semicolons means put back
    
    