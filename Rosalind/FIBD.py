# Dead Wabbits

## for thought process: https://github.com/monitdle/learning-python/blob/main/Lesson_Notes/FIBD_Notes.py
# Note: First I tried it with a list, but it got too extensive to process for n & m of 100 & 20
# Here I am using a dict bc since m is max. 20, the dict will have max. 21 keys and values


file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/FIBD_input.txt", "r")
DataRaw = file.read()
n_m = DataRaw.split(" ")
n = int(n_m[0])
m = int(n_m[1])


## Population size of a wabbit generation is comprised of:
    # number of adult pairs (aged by 1 month)
    # number of new offspring pairs (= number of adult pairs in last Gen)
    # number of new adult pairs (= number of offspring pairs in last Gen)
    # MINUS adult pairs with age (m + 1) months
    
    # F1: 1 offspring pair


def dead_wabbits(generations, age_of_death):
    
    
    ## Dictionary loop:
    # We are now making a logbook for the population of F2 for our first calculation F3
    # Comprised of number of new offspring, of new adults and of agegroups of wabbits older than 2 months
    population = {"new_offspring" : 0, "new_adults" : 1}
    
    for a in range(3, age_of_death + 2):     # Ind of age 1 (= new off) and age 2 (= new adults) are already in dict
    
        if a == (m + 1): 
            population["too_old"] = 0   # creating category for dead wabbits
    
        else:
            population[f"age_{a}"] = 0      # create age categories for adults from 3 to age_of_death
    
    
    ## Population loop:
    for gen in range(generations - 2):  # we don't need to calculate F1 & F2 since dict starts with F2
        
        prevkey = None
        prevvalue = 0

        ## Aging the wabbits by 1 month each gen:
        for key, value in population.items():
            
            # this is every iteration after the second = age categories, sliding values of last gen by 1 key:
            if prevkey is not None and key != "new_adults":     
                population[key] = prevvalue     # assigns number of last age group to this age group
                prevvalue = value   # saves value of last age group
            
            # this is the second iteration = new_adults, which is number of new offsprings in last gen:
            elif key == "new_adults":   # calculates number of new adults
                prevvalue = value       # saves value of new_adults of last gen
                population[key] = population[prevkey]   # offsprings in last gen are now new adults
            
            # this is the first iteration = new_offspring, stays the same, just save it as previous key
            prevkey = key   # since dicts are not ordered


        ## Calculate number of offsprings == number of all adults in last gen:
            # wabbits who can't have children: new offsprings & new adults
        for gen in range(1):
            population["new_offspring"] = sum(value for key, value in population.items() if key not in ["new_offspring", "new_adults"])


    ## Calculating population size by summing up all values except too_old:
    population_size = sum(value for key, value in population.items() if key != "too_old")
    
    
    return population_size



print(dead_wabbits(n, m))





