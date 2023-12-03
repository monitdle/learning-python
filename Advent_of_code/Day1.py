## DAY 1:
    #Given: strings with letters and numbers
    #Goal: extract first and last digit -> forming them to a number -> sum them up

#rawdata = """1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet"""


fasta = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day1_input.txt")
#rawdata = str(fasta)

##Ideas:
    
#using [0] [-1]
#recognize number: if 0....9 -> number

list_of_numbers = []

for string in fasta:
    numbers = ""
    for i, num in enumerate(string):
        if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            numbers += num
    if len(numbers) > 0:
        print(numbers[0], numbers[-1])
        list_of_numbers.append(numbers[0] + numbers[-1])

n = 0
for number in list_of_numbers:
    n += int(number)
print(n)



##############################################################################
################################# Part Two ###################################

fasta = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day1_input.txt")

content = fasta.read()
lines = content.splitlines()


# Step 1: Make dict and then insert the number at the end of each word
word_number = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

test = []

for i, line in enumerate(lines):
    #print(line)
    for word, number in word_number.items():
        if word in line:
            index = line.find(word) + len(word)
            line = line[:index] + number + line[index:]
            #print(line, "*")
            test.append(line)
            #print(test, "test")


list_of_numbers = []         
            
for string in test:
    numbers = ""
    for i, num in enumerate(string):
        if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            numbers += num
    if len(numbers) > 0:
        #print(numbers[0], numbers[-1])
        list_of_numbers.append(numbers[0] + numbers[-1])

n = 0
for number in list_of_numbers:
    n += int(number)
print(n)
### somehow doesn't work for the big file....



###############################################################################
############################ Second Try - Sophia's Idea #######################

fasta = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day1_input.txt")

lines = fasta.read()

word_to_number = {'oneight':'18', 'threeight':'38', 'fiveight':'58',
                  'nineight':'98', 'eightwo':'82', 'eighthree':'83',
                  'sevenine':'79','twone':'21', 'one':'1', 'two':'2', 'three':'3',
                  'four':'4', 'five':'5', 'six':'6', 'seven':'7',
                  'eight':'8', 'nine':'9'}

for word, number in word_to_number.items():
    lines = lines.replace(word, number)
#print(lines)

lines = lines.split()

list_of_numbers = []

for string in lines:
    numbers = ""
    for i, num in enumerate(string):
        if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            numbers += num
    if len(numbers) > 0:
        print(numbers[0], numbers[-1])
        list_of_numbers.append(numbers[0] + numbers[-1])

n = 0
for number in list_of_numbers:
    n += int(number)
print(n)
