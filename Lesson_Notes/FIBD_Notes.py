# Dead Wabbits

## Number of wabbits in a Generation is:
    # [1] new adult pairs (= number of offspring pairs in last Gen)
    # [2] new offspring pairs (= number of adult pairs in last Gen)
    # [3] adult pairs who are the parents of the new offsprings = [2]
    # [4] MINUS adult pairs with age (m + 1) months
    
    # F1: 1 offspring pair


file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/FIBD_input.txt", "r")
DataRaw = file.read()
n_m = DataRaw.split(" ")
n = int(n_m[0])
m = int(n_m[1])

## Thoughts:
    # F1 => first 2 Gens have population of 1
    # [2] and [3] are (numbers of adult pairs in last Gen) * 2
    # adult pair = wabbits this Gen with age > 1 month
    # before a pair dies, it still has offspring -> so [4] calculated at last
    # [1] = wabbits last Gen with age 1 month
    # new adults first become adults, then next Gen have children
    
    # order of calculation: [2] & [3], [1], [4]



############################################################################################################
################################### Making List: Doesn't process ###########################################
############################################################################################################

## Calculations for n = 6 and m = 3:
p = [2] # starting with F2 with 1 adult rabbit pair
    

#[2] & [3]  also [1] through aging after counting last adults
for gen in range(2):
    last_adults = sum(1 for wabbit in p if wabbit > 1)  #counting number of last gens adults
    new_os = [1] * last_adults      #every adult pair gets 1 offpring
    
    # aging before appending new offspring:
    new_p = [a + 1 for a in p]
    
    new_p.extend(new_os)    #unite aged population with new offsprings
    
    p = new_p   #this new population is now the last one for next generation
    

# [4]:
# p = [wabbit for wabbit in new_p if wabbit != (m + 1)]


def dead_wabbits(generations, months_to_live):
    
    population = [2] #starting with F2 with 1 adult rabbit pair thats 2 months old
    
    for gen in range(generations - 2): #leaving out F1 & F2
        last_adults = sum(1 for wabbit in population if wabbit > 1)  #counting number of last gens adults
        new_os = [1] * last_adults      #every adult pair gets 1 offpring
        
        # aging before appending new offspring:
        new_p = [a + 1 for a in population]
        
        # appending new offspring using .extend() to not create list in list:
        new_p.extend(new_os)
        
        # overwrite old pop with new for next loop
        too_old = months_to_live + 1
        population = [wabbit for wabbit in new_p if wabbit != too_old]
    
    return len(population)
        

#print(dead_wabbits(n, m))

############################################################################################################
############################################################################################################



############################################################################################################
################################### Making Dictionary: Works! ##############################################
############################################################################################################

## Number of wabbits in a Generation is:
    # [1] new adult pairs (= number of offspring pairs in last Gen)
    # [2] new offspring pairs (= number of adult pairs in last Gen)
    # [3] adult pairs aged by 1 month, are the parents of the new offsprings, their sum = [2]
    # [4] MINUS adult pairs with age (m + 1) months
    
    # F1: 1 offspring pair
    # order of calculation: [2] & [3], [1], [4]


file = open("/Users/lemon/Desktop/Programming/learning-python/Rosalind/FIBD_input.txt", "r")
DataRaw = file.read()
n_m = DataRaw.split(" ")
n = int(n_m[0])
m = int(n_m[1])


## Dictionaries? Instead of keeping every individual just keep count of every category on its own?
# Problem: How to keep track of age?
# I would need to create age categories e.g. how many wabbits are 2 months old etc.
# But still, maybe that is easier to process
# first I need to write a loop that creates a dict for me since the number of keys is depended on m


## Dictionary loop
    #what we are now making is the population of F2 for our first calculation F3:

population = {"new_offspring" : 0, "new_adults" : 1}

# in our dict we already covered Ind of age 1 (= new off) and age 2 (= new adults):
for a in range(3, m + 2):
    
    if a == (m + 1): 
        population["too_old"] = 0
    
    else:
        population[f"age_{a}"] = 0

# since m <= 20, the dict will have max. 21 keys



### Calculations in order [3] & [1], [2], [4], [5]:
# why: [3] & [1] first to age all adults sliding values along the keys and to put new_offsprings of last gen to new_adults
    # then [2] to calculate new_offsprings of this gen
    # then [4] at last to enable them to still have offspring
        # in using dict, [4] doesn't have to be deleted, just left out in the population calculations
    # [5] calculating population size by sum of values except too_old


## [3] & [1]: in this case the number of adults doesn't have to be calculated
# => [3] is the aging process of wabbits that are NOT new offsprings (since they were just born)
# [1] included in calculation of [3]
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


## [2]: number of offsprings == number of all adults in last gen
for gen in range(1):
    population["new_offspring"] = sum(value for key, value in population.items() if key != "new_offspring")


## [4] == too_old

## [5]: calculating population size by summing up all values except too_old
population_size = sum(value for key, value in population.items() if key != "too_old")
    
    
    
    
    
    