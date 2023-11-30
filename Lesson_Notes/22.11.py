# Lesson to PROT:

## Exercise: Print triplets
RNAstring = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

move = 0
for i in range(len(RNAstring)):
    triplet = RNAstring[0 + move : 3 + move]
    print(triplet)
    move += 1

print("###########")

### Alternative with % without move
for i in range(1, len(RNAstring)):
    if i % 2 != 0:
        position = i
        triplet = RNAstring[position - 3 : position]
        print(triplet)


