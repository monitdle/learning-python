# Mendalian inheritance

k = 2   #AA
m = 2   #Aa
n = 2   #aa

#broke tree down into branches and swapped the probabilities for variables

def dominant(k, m, n):
    pop = k + m + n     #population size
    k_branch = (k / pop) * (((k-1) / (pop-1)) + (m / (pop - 1)) + (n / (pop - 1)))
    m_branch = (m / pop) * (((3*(m-1)) / (4*(pop-1))) + (k / (pop - 1)) + (n / (2*(pop - 1))))
    n_branch = (n / pop) * ((k / (pop - 1)) + (m / (2*(pop - 1))))

    PA = round(k_branch + m_branch + n_branch, 5)   #rounding an integer
    return PA

dominant(2,2,2)