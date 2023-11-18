# Wabbits

####Number of rabbits is:
    #older offspring (= number of 1 Generation before)
    #plus adults (= number of 2 Gens before)
    #plus new offspring (= adults * k)
    #number of Generations = n

#   F1 = 1
#   F2 = 1
#   F3 = F2 + (F1*k)
#   F4 = F3 + (F2*k)
#   F5 = F4 + (F3*k)

#n = 5
#k = 3

def wabbits(n, k):
    F1 = 1
    F2 = 1
    Fn = 0
    if n > 2:
        for number_of_Generations in range(n - 2):
            Fn = (F1 * k) + F2
            F1 = F2
            F2 = Fn
    elif n == 2:
        F2 = k
    else:
        F2 = 1
    return F2
        
print(wabbits(5, 3))
        