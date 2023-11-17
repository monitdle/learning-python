# Rosalind INI 5

#create a new file
#containing all the even-numbered lines from the original file#
#assume 1-based numbering of lines

old_file = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat"""

for line in (old_file.splitlines())[1::2]:
    print(line)

