# Notes to Exercises  

## First time using **while**  
_Printing till 5_
```
i = 1
while i <= 5:
    print(i)
    i += 1

# Output: 1
          2
          3
          4
          5
```  
  
  
_Counting digits of num_
```
num = 34566
count = 0

while num != 0:
    num = num // 10
    count = count + 1
print(count)
```



## Patterns with **for**
_Pyramid_
```
for i in range(1, 6):
    for x in range(1, i + 1):
        print(x, end = "_")
    print("")

# Output: 1_
          1_2_
          1_2_3_
          1_2_3_4_
          1_2_3_4_5_
```
- inner loop makes columns
- outer loop makes rows
- used under score for better visualisation  
  
  
_Reverse Pyramid_
```
rows = 5
# reverse loop
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")

# Output:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
```  
  
  
_Combined pyramid_
```
n = 5

for i in range(1, n + 1):
    for x in range(i, 0, -1):
        print("*", end = " ")
    print("")
for i in range(n -1, 0, -1):
    for x in range(i, 0, -1):
        print("*", end = " ")
    print("")

# Output:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
```  
  
  
_Sum of all numbers with text_
```
y = 0
for x in range(11):
    y = x + y
print("Enter number", x)
print("Sum is:", y)

# Output: Enter number 10
          Sum is: 55
```
- remember Rosalind INI4  
  
  
_Multiplication table for a number (num) till 10_
```
num = 2
for x in range(1, 11):
    y = num * x
    print(y)
```
- Zweierreihe  
  
  
_Printing list in reverse_
```
list1 = [10, 20, 30, 40, 50]

for x in range(len(list1) - 1, 0 - 1, -1):
    print(list1[x])
```  
  
  
### Redefining variables within a loop
_Fibonacci sequence_
```
a = 0
b = 1
num = 10
print("Fibonacci sequence:")

for x in range(num):
    print(a, end = " ")
    c = b + a
    a = b
    b = c

# Output:
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34
```
  
  
_Factorial_
```
num = 4
a = 1

for x in range(1, num + 1):
    c = a * x
    a = c
print(c)
```  
  
  
## if-Loops
_Multiple if-Loops_
Conditions:  
- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]

for x in numbers:
    if x > 500:
        break
    if x%5 != 0:    #elif
        continue
    if x > 150:    #elif
        continue
    else:
        print(x)
```
  
  
_Prime numbers_
```
start = 25
end = 50

for x in range(start, end + 1):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            print(x)
```
  
  
  
## Very different solutions
_Exercise 14: Reverse a given integer number_  
I didn't think of using **while**
```
# my idea:
num = 76542

for x in range(len(str(num)) - 1,-1,-1):
    strnum = str(num)
    index = strnum[x]
    print(int(index), end = "")

###################################################
# using while:
num = 76542
reverse_number = 0
print("Given Number ", num)

while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)
```
  
  
_Printing negative numbers_
```
for x in range(10, 0, -1):
    print("-" + str(x))

# I cheated :D

###################################################
# Actual solution:
for x in range(-10, 0, 1):
    print(x)
```
  
  
_Printing odd indices_
```
# My solution:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for x in range(len(my_list)):
    if x % 2 == 0:
        continue
    else:
        print(my_list[x], end = " ")

###################################################
# Actual and better solution:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    print(i, end=" ")
```
  
  
_Sum of the series upto n terms_
2+22+222+2222+22222
```
# My solution:
n = 5
a = 0

for x in range(1, n + 1):
    res = int("2" * x) + a
    a = res
print(res)

###################################################
# Actual solution:
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)

