# Pitfalls of Reversing Translation

## Module
#if  a % n = b % n     <=>     a ≡ b % n
#if  c % n = d % n     <=>     c ≡ d % n

#then   a + c ≡ b + d % n   and     a * c ≡ b * d % n


## Testing with example
a = 29
b = 73
c = 10
d = 32
n = 11

a % n == b % n
c % n == d % n
a + c % n == b + d % n
a * c % n == b * d % n


## Translating Protein to RNA
#Problem: string of 1000 aa
#Output: number of possible original RNA strings % 1,000,000
#Tip: Don't forget Stop codon

Protein = "MA"
codontable = {"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "UUA":"L", "UUG":"L", 
            "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", 
            "GCC":"A", "GCU":"A", "GCA":"A", "GCG":"A", 
            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", 
            "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", 
            "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", 
            "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", 
            "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", 
            "AUU":"I", "AUC":"I", "AUA":"I", 
            "UUU":"F", "UUC":"F", 
            "GAU":"D", "GAC":"D", 
            "GAA":"E", "GAG":"E", 
            "AGU":"S", "AGC":"S", 
            "AAA":"K", "AAG":"K", 
            "AAU":"N", "AAC":"N", 
            "CAU":"H", "CAC":"H", 
            "UAU":"Y", "UAC":"Y", 
            "UGU":"C", "UGC":"C", 
            "CAA":"Q", "CAG":"Q", 
            "UGG":"W", 
            "AUG":"M", 
            "UAA":"Stop", "UAG":"Stop", "UGA":"Stop"}

last_count = 1
for i in range(len(Protein)):
    count = 0
    for value in codontable.values():
        if value == Protein[i]:
            count += 1
    #print(count, "of a base")
    last_count *= count
    #print(last_count, "possible combinations")
count_stop = last_count*3
#print(count_stop, "possible combinations incl. Stop")
module = count_stop % 1000000
print(module)


#### Note: I did use to max. acceptable number of loops...