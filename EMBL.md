# Introduction to Python Programming: 2. Beginning Programming
## _Exercise 2.1_: .append() and not in
- Make second list and append to first one.
```
shopping = ['bread', 'potatoes', 'eggs', 'flour', 'rubber duck', 'pizza', 'milk']
shopping2 = ["cheese", "flour", "eggs", "spaghetti", "sausages", "bread"]

shopping = ['bread', 'potatoes', 'eggs', 'flour', 'rubber duck', 'pizza', 'milk']
for item in shopping2:
    shopping.append(item)
print(shopping)
```      
  
  
- Avoid double items.
```
for item in shopping2:
    if item not in shopping:
        shopping.append(item)
print(shopping)
```


## _Exercise 2.2_: elif and else
- Printing what's already on the list.
  
1. Solution using **elif**
```
for item in shopping2:
    if item not in shopping:
        shopping.append(item)
    elif item in shopping:
        print(item + " already on list"
print(shopping)
```
  
2. Solution using **else**
```
for item in shopping2:
    if item in shopping:
        print(item + " already on list")
    else:
        shopping.append(item)
print(shopping)
```
  
  
## _Exercise 2.3_: range()
- Desired output: [4, 11, 18, 25]
```
list(range(4, 26, 7))
```
  
  
## **Recalling variables in a string**
name = 'Betty'
date = '15th June 2016'
job = 'engineer'
  
- using %
```
  print('Hi, my name is %s and I am an %s. I have been an %s since %s.' % (name, job, job, date))
```
– %s: String (works for any type)  
– %d: Integer  
– %f: Floating-point number  
– %x or %X: Integer in hexadecimal (lowercase or uppercase)  
  
- using .format
```
  print('Hi, my name is {0} and I am an {1}. I have been an {1} since {2}.'.format(name, job, date))
```
– numbers in {} describe the index in .format()
  
- using f
```
  print(f'Hi, my name is {name} and I am an {job}. I have been an {job} since {date}.')
```
– I like this one (in theory)  -> we'll see
– looks the clearest  
  
  
## _Exercise 2.4_: .format()
- Fill in the gaps
- Did similar/simpler version in unit 13.11.
    
shopping = ['bread', 'potatoes', 'eggs', 'flour', 'rubber duck', 'pizza', 'milk']
amounts = ['1', '10', '12', '1', '2', '5', '1']
--- i in range(len(---)):
    s = 'I need to buy --- ---'.format(amounts[---], ---[i])
    print(---)

```
for i in range(len(shopping)):
    s = "I need to buy {0} {1}".format(amounts[i], shopping[i])
    print(s)
```


    

