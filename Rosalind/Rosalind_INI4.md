# INI 4
_Given: Two positive integers a and b (a<b<10000).  
Return: The sum of all odd integers from a through b, inclusively._
a = 4976
b = 9760

result = 0


## First option
```
for n in range(0, b - a + 1):
    if n % 2 == 0:
        continue
    result = result + (a + n)
    
print(result)
```

## Second option
```
for n in range(a, b + 1):
    if n % 2 == 1:
        result = result + n
    
print(result)
```

## Third option
```
for n in range(a, b + 1):
    if n % 2 == 0:
        continue
    result = result + n
    
print(result)
```


# INI 6
## Initial idea
```
s = "When I find myself in times of trouble Mother Mary comes to me"
list = []
dict = {}
for word in s.split(" "):
    if word not in list:
        list.append(word)
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    print(key, value)
```
- I think I thought of this bc I'm more familiar working with lists than dictionaries
- I did use the hints

## Clean up
```
s = "We tried list and we tried dicts also we tried Zen"
dict = {}
for word in s.split(" "):
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    print(key, value)
```
