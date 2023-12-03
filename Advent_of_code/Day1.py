## DAY 1:
    #Given: strings with letters and numbers
    #Goal: extract first and last digit -> forming them to a number -> sum them up

#rawdata = """1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet"""


fasta = open("/Users/MoniLe/Desktop/Programming/learning-python/Advent_of_code/Day1_input.txt")
rawdata = str(fasta)

##Ideas:
    
#using [0] [-1]
#recognize number: if 0....9 -> number

list_of_numbers = []

for string in rawdata.split():
    numbers = ""
    for i, num in enumerate(string):
        if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            numbers += num
    if len(numbers) > 0:
        list_of_numbers.append(numbers[0] + numbers[-1])

n = 0
for number in list_of_numbers:
    n += int(number)
print(n)