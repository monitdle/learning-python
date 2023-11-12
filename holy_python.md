# Homework 06.11.2023
## Exercise 1
– a
```
print("Hello World!")
```
– b
```
my_text = "Hello World!"
``` 
– c
```
print("%", "gREAT", "C-14", "13", "numbers", "7", ":)")
```

  
## Exercise 2
– a
```
glass_of_water = 3
```
– b
```
print(glass_of_water)
```

  
## Exercise 3
– a
```
men_stepped_on_the_moon = 12
```
– b
```
my_reason_for_coding = "fun"
```
– c
```
global_mean_sea_level_2018 = 21.36
```
– d
```
staying_alive = True
```

  
## Exercise 4
– a
```
answer_1 = type(men_stepped_on_the_moon)
```
– b
```
answer_2 = type(my_reason_for_coding)
```
– c
```
answer_3 = type(global_mean_sea_level_delta_2018)
```
– d
```
answer_4 = type(staying_alive)
```
– e
```
answer_5 = type(int(my_grade))
```
– f
```
answer_5 = type(int(my_temp))
```
– h
```
gwp_str = str(gross_world_product)
```

  
## Exercise 6
– a
```
answer_1 = lst[0]
```
– b
```
print(lst[1])
```
– c
```
answer_1 = lst[-1]
```
– d
```
gift_list.append('pajamas')
```
– e
```
gift_list + ["socks", "tshirt", "pajamas"]
```
– f
```
gift_list.insert(3, 'slippers')
```
– g
```
answer_1 = lst.index(8679)
```
– h
```
lst.append(["Navigator", "Suburban"])
```
– i
```
lst.remove(lst[-1])
```
– j
```
lst.reverse()
```
– k
```
answer_1 = lst.count(6)
```
– l
```
answer_1 = sum(lst)
```
– m
```
answer_1 = min(lst)
```
– n
```
answer_1 = max(lst)
```
  
  
## Exercise 8
– a
```
lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]

for x in lst:
    print(x)
```
– b
```
str="Antarctica"

for x in lst:
    print("Hello!,", x)

# their solution
for i in lst:
    print("Hello!, " + i)
```
- using comma automatically inserts a space between words
- plus needs you to add it yourself

– c
```
str="Civilization"

for x in str:
    print(x)
```

– d
```
# guess: 12
for i in str:
    c = c + 1

    print(c)
```
– e
```
lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]

for x in lst1:
    lst2.append("Dr. " + x)
print(lst2)

# Output: ['Dr. Phil', 'Dr. Oz', 'Dr. Seuss', 'Dr. Dre']
```
– f
```
lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]

for x in lst1:
    lst2.append(x**2)
print(lst2)

# Output: [9, 49, 36, 64, 81, 121, 225, 625]
```
– g
```
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]

for x in lst1:
    if x > 0:
        lst2.append(x)
print(lst2)

# Output: [111, 32, 9, 85]
```
– h
```
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]

for x in dict:
    if dict[x] > 1000:
        y = dict[x] - 1000
        lst.append(y)
print(lst)

# their solution:
for i in dict:
    if dict[i] > 1000:
        lst.append(dict[i]-1000)
```
- I don't know why I made it more complicated
- probably to comprehend the structure of dictionaries better
- Note: Have to think about why _for_ doesn't need 'dict[x]' but _if_ does
  
– i
```
lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]

for x in lst1:
    lst2.append(type(x))

print(lst2)

# Output: [<type 'float'>, <type 'int'>, <type 'str'>, <type 'bool'>, <type 'list'>, <type 'dict'>]
```
  
  
## Exercise 9
– a
```
str = "It's always darkest before dawn."
```
– b
```
ans_1 = str[0] + str[1] + str[-1]
```
– c
```
str.replace('.','!')
```
– d
```
str.lower()
```
– e
```
str.upper()
```
– f
```
str.capitalize()
```
– g
```
ans_1 = str.startswith('A')
```
– h
```
ans_1 = str.endswith('.')
```
– i
```
ans_1 = str.index('v')
```
– j
```
ans_1 = str.find('m')
```
– k
```
str.find('X')
str.index('X')
```
– l
```
ans_1 = str.count('a')
ans_2 = str.count('o')
```
– m
```
ans_1 = type(v_1)
ans_2 = type(v_2)
```
– n
```
ans_1 = len(str)
```

  
## Exercise 11
– a
```
lst.sort()
```
– b
```
lst.sort()
```
– c
```
lst.sort(reverse = True)
```
– d
```
gift_list.sort(reverse = True)
```
– e
```
NFL.sort(reverse = True)
answer_1 = NFL[-1]
```
– f
```
muni.sort(reverse = True)
```
– g
```
key_list = list(dict.keys())
key_list.sort()
```


## Exercise 12
– a
```
popped_item = lst.pop()
```
– b
```
item = lst.pop(lst.index('broccoli'))
```
– c
```
italy_gdp = GDP_2018.pop('Italy')
```


## Exercise 17
– a
```
ans_1 = wrd[0:4]
```
– b
```
ans_1 = wrd[3:7]
```
– c
```
ans_1 = wrd[3:6]
```
– d
```
ans_1 = wrd[0: :2]
```
– e
```
ans_1 = wrd[1:-1:2]
```
– f
```
ans–1 = lst[::-1]
```
– g
```
ans–1 = lst[-2:]
```
– h
```
ans_1 = lst[1:3]
```


