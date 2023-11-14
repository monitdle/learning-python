# Notes to Exercises  

## First time using **while**  
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

## Pattern: Pyramid
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
  
  
## Sum of all numbers with text
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
  
  
## Multiplication table for a number (num) till 10
```
num = 2
for x in range(1, 11):
    y = num * x
    print(y)
```
- Zweierreihe


## 
