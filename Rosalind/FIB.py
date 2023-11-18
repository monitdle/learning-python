# Wabbits

## Number of rabbits is:
    # [1] kids (= number of last Gen, in pairs)
    # [2] new offspring pairs (= adults of 2 Gens before * k)
    # [3] adult pairs who are the parents of the new offpsrings

#   F1 = 1
#   F2 = 1
#   F3 = F2 + (F1*k)
#   F4 = F3 + (F2*k)
#   F5 = F4 + (F3*k)

# n = 5 ... number of generations, Fn
# k = 3 ... number of offspring pairs per pair

def wabbits(n, k):
    F1 = 1    #first generation with one pair, two young to have offspring
    F2 = 1    #second generation
    Fn = 0    #calculating generation
    if n > 2:
        for number_of_Generations in range(n - 2):    #-2 = minus the first two generations
            Fn = (F1 * k) + F2    # ([3] * k) + [1] = [3] + [2] + [1]
            F1 = F2     #redefine last generation to generation before
            F2 = Fn    #redefine calculated generation to last generation
            
    #second and first generations are fixated
    elif n < 3:
        F2 = 1
    else:
        pass
        
    return F2
        
print(wabbits(5, 3))
        
