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
### Pyramid
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

  
### Reverse Pyramid
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

### Sum of all numbers with text 
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

  
### Multiplication table for a number (num) till 10
```
num = 2
for x in range(1, 11):
    y = num * x
    print(y)
```
- Zweierreihe

### Printing list in reverse
```
list1 = [10, 20, 30, 40, 50]

for x in range(len(list1) - 1, 0 - 1, -1):
    print(list1[x])
```




## if-Loops
### Multiple if-Loops
_Conditions:_  
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





