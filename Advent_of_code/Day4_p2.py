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


## Making lists
owning = []
winning = []

for key, value in win_own.items():
    winning.append(key)
    owning.append(value)

    
## Counting matches and making a list
number_of_matches = []

for i, win in enumerate(winning):
    cardID = i + 1
    list_of_matches = []
    match_list = []
    
    for number in win.split(" "):
        
        if number in owning[i]:
            list_of_matches.append(number)
        
    count = len(list_of_matches)
    #print(count, f"matches on Card {i + 1}")
    number_of_matches.append(count)

#print(number_of_matches)


## Making list with number of cards
cards = [1] * len(winning)


## Counting number of a card i
#steps = card i + number_of_matches[i]
#adding (cards[i] * 1) number of copies

for i, matches in enumerate(number_of_matches):
    for next_card in range(1, matches + 1):
        cards[i + next_card] += (1 * cards[i])

print(sum(cards))




       
