# Unit 15.11.
## Dictionaries

student_number = {
    "BioTech" : 16,
    "CompBio" : 12,
    "Post-genBio" : 20,
    "Economy" : 3,
    "EnvMaths" : 0
}

_Format:_
key : value

- recall a value: student_number["BioTech"]
- change value of a key: student_number["BioTech"] = 13
- add to value: student_number["BioTech"] += 1
- append new key and value: student_number["NewKey"] = 2


### Looping with Dict
```
for x in student_number:
    print(x)
        # prints the keys
```
```
for x in student_number:
    print(student_number[x])
        # prints values
```
``````
for x in student_number:
    print(x, student_number[x])
        # prints both
``````

del abc
    # deletes variable abc


### Dictionary operators
dict.keys()     # gives you the keys
dict.item()     # gives you all (key : value)



### Exercise: Debugging
- find all numbers between lower and upper bound
- put them in list
- no duplicate entries

``````
def find_within_range(list_of_numbers, lower=0, upper=10):
   #output = {}
    output = []
    for number in list_of_numbers:
       #if 0 > number <= 10:
        if lower <= number <= upper:
           #if number in output:
               #output.append(number)
            if number not in output:
                output.append(number)
  
    return output

print(find_within_range([-2, 14, 9, 3.14]))              # should return [9, 3.14]
print(find_within_range([0, 5, 10, 15]))                 # should return [0, 5, 10]
print(find_within_range([2.104, 10000, -435, 2.104]))    # should return [2.104]
print(find_within_range([1, 2, 3, 4], lower=2, upper=6)) # should return [2, 3, 4]
``````


