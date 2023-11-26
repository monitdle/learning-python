# Calculating Expected Offspring

## Given Example
#I wanted to make it into an easy input, so later it can be copy&pasted
rawdata = list("1 0 2 1 4 1")
number_of_couples = [int(number) for number in rawdata if number != " "]

## Assigning the integers with their population
type_of_couples = list(("AA_AA", "AA_Aa", "AA_aa", "Aa_Aa", "Aa_aa", "aa_aa"))
population = dict(zip(type_of_couples, number_of_couples))

## Calculated probability per couple (look up Mendel's Laws) & assign to population
probability_per_couple = list((1, 1, 1, 0.75, 0.5, 0))
probability_population = dict(zip(type_of_couples, probability_per_couple))


## Equation for number of offspring per couple:
    # integer of of population dict * probability of that dict * 2 (because there are 2 kids)
    # that makes the number of offsprings in a population sum(offspring per couple)
number_of_offsprings = 0
for couple in type_of_couples:
    number_of_offsprings += population[couple] * probability_population[couple] * 2

print(number_of_offsprings)


########################################################################################
## Note:
    # making a dict with just type_of_couples and probability_per-couple doesn't work
    # since keys have to be unique