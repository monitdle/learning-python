file = open("C:\\Users\\monik\\OneDrive\\Desktop\\Programming\\learning-python\\Advent_of_code\\Day4_input.txt", "r")
pile_of_cards = (file.read()).splitlines()


## Separating ID from content but still associating them through a dict -> for fun?
## was not necessary, I think I did it out of habit - could've just remove the ID and return a list
card_content = {}
previous_content = ""
for card in pile_of_cards:
    splitting_ID = card.split(":")
    for i, content in enumerate(splitting_ID):
        content = content.strip()
        if i % 2 == 0:
            card_ID = content
            card_content[card_ID] = ""
        else:
            card_content[card_ID] = content
#print(card_content)


## Idea: Dictionary: Key with winning (shorter length) and values with owned (longer length) numbers
win_own = {}
for values in card_content.values():
    w_o = values.split("|")
    for i, section in enumerate(w_o):
        if i % 2 == 0:
            win = section[:-1]      #to remove last space, annoyed me
            win_own[win] = ""
        else:
            owned = section[1:]     #again, just for looks
            win_own[win] = owned
#print(win_own)


## After submitting: Have to make owned numbers to a list or else one digit numbers will always be matched
for win, owned in win_own.items():
    owned_list = []
    for number in owned.split(" "):
        if number.isdigit():
            owned_list.append(number)
    win_own[win] = owned_list
#print(win_own)


## Wanted Output: For the first time it's true -> 1 point; then -> doubled
    #Meaning: 1; 1*2; 1*2*2; 1*2*2*2.....
    #OR: 2^0, 2^1, 2^3, 2^4.....
    #in Python: 2 ** 0, 2 ** 1, .....

cardID = 0  #created that just for the printing ***** below, to look pretty
sum_of_points = 0

for win, owned in win_own.items():
    #print("\nNumbers I need:", win, "\nNumbers I have:", owned)
    matches = -1
    cardID += 1
    
    for number in win.split(" "):
        if number in owned and number.isdigit():
            #print(number)
            matches += 1
    print(matches +  1, f"match*es in Card {cardID}")   #*****
    
    if matches >= 0:
        points = 2 ** matches
        print(" =>  2 **", matches, "  =", points, "points")
        sum_of_points += points

print(sum_of_points)        
