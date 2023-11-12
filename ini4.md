_Given: Two positive integers a and b (a<b<10000).  
Return: The sum of all odd integers from a through b, inclusively._
a = 4976
b = 9760

result = 0


# First option
```
for n in range(0, b - a + 1):
    if n % 2 == 0:
        continue
    result = result + (a + n)
    
print(result)
```

# Second option
```
for n in range(a, b + 1):
    if n % 2 == 1:
        result = result + n
    
print(result)
```

# Third option
```
for n in range(a, b + 1):
    if n % 2 == 0:
        continue
    result = result + n
    
print(result)
```
