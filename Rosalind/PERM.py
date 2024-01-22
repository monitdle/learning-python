# Permutation:
    #every possible combination of integers 1 to n
    #Input: n < 8
    #Output: sum of possible combinations & list of those

n = 5

int_list = list(x for x in range(1, n + 1))     #exclude 0, include n


from itertools import permutations
perm = list(permutations(int_list, n))

print(len(perm))
for item in perm:
    for number in item:
        print(number, end=" ")
    print("")


### Note: I use Spyder. I had to raise the number of lines shown in the console to copy the
    # Output, but the max. is 5000 so I couldn't copy the output for n > 6

## Extra: Save Output in a file

n = 7

int_list = list(x for x in range(1, n + 1))     #exclude 0, include n


from itertools import permutations
perm = list(permutations(int_list, n))

output_file_path = "/Users/lemon/Desktop/Programming/learning-python/Rosalind/PERM_output.txt"

with open(output_file_path, 'a') as file:
    print(len(perm), file=file)

for item in perm:
    for number in item:
        with open(output_file_path, 'a') as file:
            print(number, end=" ", file=file)
    with open(output_file_path, 'a') as file:
        print("", file=file)

