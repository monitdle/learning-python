file = open("/Users/lemon/Desktop/Programming/learning-python/Advent_of_code/Day10_input.txt", "r")
pipes_file = file.read()
pipes_file = pipes_file.splitlines()


### What are the steps?
# Which pipes are connectable?
# How to differenciate between e & w and s & n?
# How to know which way to go when you're at S?
# Replacing the pipes with numbers, following the connectables list/dict?
# Output: max number


### Input
# multiple lines
# every line same length
# not every pipe is relevant



############# Creating dictionaries with connectable pipes #############

possdirect = {"n" : ["|", "7", "F"], "s" : ["|", "L", "J"], "e" : ["-", "J", "7"], "w" : ["-", "F", "L"]}      #possible pipes depending on where you want to go
pipes = {"|" : ["n", "s"], "-" : ["e", "w"], "7" : ["w", "s"], "L" : ["n", "e"], "F" : ["s", "e"], "J" : ["n", "w"]}    #pipes directions



############# Looking around, starting by S #############

## Finding positon of S:
    
for l, line in enumerate(pipes_file):
    for i, letter in enumerate(line):
        if letter == "S":
            S_line = l
            S_index = i


# north ... last line, same index
# south ... next line, same index
# east ... index + 1
# west ... index - 1

north = pipes_file[S_line - 1][S_index]
south = pipes_file[S_line + 1][S_index]
east = pipes_file[S_line][S_index + 1]
west = pipes_file[S_line][S_index - 1]




###############################################################################
############################ Working with numpy ###############################
###############################################################################

import numpy as np

matrix = np.array([list(row) for row in pipes_file], dtype='str')
num_rows, num_cols = matrix.shape



############## Defining function to look for neighbor & add 1 #################

def path(row, col):
    
    if row > 0 and row - 1 in range(num_rows) and matrix[row - 1, col] in possdirect["n"]:     #north
        north = matrix[row - 1, col]
        matrix[row - 1, col] = int(matrix[row, col]) + 1
    
    if row < num_rows and row + 1 in range(num_rows) and matrix[row + 1, col] in possdirect["s"]:     #south
        south = matrix[row + 1, col]
        matrix[row + 1, col] = int(matrix[row, col]) + 1
    
    if col < num_cols and col + 1 in range(num_cols) and matrix[row, col + 1] in possdirect["e"]:     #east
        east =  matrix[row, col + 1]
        matrix[row, col + 1] = int(matrix[row, col]) + 1
    
    if col > 0 and col - 1 in range(num_cols) and matrix[row, col - 1] in possdirect["w"]:     #west
        west =  matrix[row, col - 1]
        matrix[row, col - 1] = int(matrix[row, col]) + 1
       

    return matrix



############################### Finding S #####################################
for i in range(num_rows):
    for j in range(num_cols):
        
        if matrix[i, j] == "S":
            matrix[i, j] = 0
            start_i, start_j = i, j
            
            matrix = path(start_i, start_j)
            print(matrix)

############################### Finding 1s #####################################
#for i in range(num_rows):
 #   for j in range(num_cols):
        
        

    







