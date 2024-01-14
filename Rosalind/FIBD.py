# Dead Wabbits

## for thought process: https://github.com/monitdle/learning-python/blob/main/Lesson_Notes/FIBD_Notes.py

file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/FIBD_input.txt", "r")
DataRaw = file.read()
n_m = DataRaw.split(" ")
n = int(n_m[0])
m = int(n_m[1])


## Dictionary loop
    #what we are now making is the population of F2 for our first calculation F3:


# in our dict we already covered Ind of age 1 (= new off) and age 2 (= new adults):

# since m <= 20, the dict will have max. 21 keys


def dead_wabbits(generations, age_of_death):
    
    # making dict with values of F2:
    population = {"new_offspring" : 0, "new_adults" : 1}
    for a in range(3, age_of_death + 2):
    
        if a == (m + 1): 
            population["too_old"] = 0
    
        else:
            population[f"age_{a}"] = 0  
    
    
    # aging the wabbits by 1 month:
    for Gen in range(generations - 2):  #we don't need to calculate F1 & F2
        
        prevkey = None
        prevvalue = 0

        for key, value in population.items():
            
            if prevkey is not None and prevkey != "new_offspring":
                population[key] = prevvalue     #assigns number of last age group to this age group
                prevvalue = value   #saves value of last age group
            
            elif key == "new_adults":   #calculates [1]
                prevvalue = value       # saves value of new_adults of last gen
                population[key] = population[prevkey]   #offsprings in last gen are now new adults
            
            prevkey = key   #saves which key was before since dicts are not ordered by rank


        ## calculate number of offsprings == number of all adults in last gen:
        for gen in range(1):
            population["new_offspring"] = sum(value for key, value in population.items() if key not in ["new_offspring", "new_adults"])
            # leaving out new adults since they just became adults and offsprings

    ## calculating population size by summing up all values except too_old
    population_size = sum(value for key, value in population.items() if key != "too_old")
    
    
    return population_size



print(dead_wabbits(n, m))





