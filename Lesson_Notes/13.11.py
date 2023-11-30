# Unit 13.11.2023
shopping = ['bread','potatoes','eggs','flour','rubber duck','pizza','milk']
amounts =  ['1','10','12','1','2','5','1']
prices = [3, 0.5, 1.2, 5.3, 13.7, 16, 1.47]



## assign amounts to shopping items
for i in range(len(shopping)):
    s = 'I need to buy ' + amounts[i] + ' ' + shopping[i]
    print(s)

### my attempt avoiding len()
for i in fruits:
    s = "I need " + amount[fruits.index(x)] + " of " + x
    print(s)



## calculate the shopping bill
res = 0
for i in range(len(shopping)):
    s = 'I need to buy ' + amounts[i] + ' ' + shopping[i]
    print(s)
    res = res + (prices[i] * int(amounts[i]))
 
print("the total price is " + str(res))

### my attempt
bill = 0
for x in range(len(shopping)):
    bill += prices[x] * int(amounts[x])
print(bill)



