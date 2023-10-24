ItemCards = open("ItemCards.txt", "r")
PersonCards = open("PersonCards.txt", "r")

def remove_non_ascii(s):
    return "".join(c for c in s if ord(c)<128)

ItemCards = ItemCards.read().lower()
PersonCards = PersonCards.read().lower()

PPList = []
EList = []
SOList = []

PersonPPList = []
PersonEList = []
PersonSOList = []
ItemCards = remove_non_ascii(ItemCards)
ItemCards = ItemCards.split(' ')

PersonCards = remove_non_ascii(PersonCards)
PersonCards = PersonCards.split(' ')

PersonsLength = len(PersonCards)

PartyItems = open('PartyItems.txt','w')
ElixirItems = open('ElixirItems.txt','w')
SnakeOilItems = open('SnakeOilItems.txt','w')
PartyPeople = open('PartyPeople.txt','w')
ElixirPeople = open('ElixirPeople.txt','w')
SnakeOilPeople = open('SnakeOilPeople.txt','w')


count = 0

for x in range(0,PersonsLength-1):
    Item = PersonCards[x]
    ItemNext = PersonCards[x+1]
    if 'Potion' in Item:
        PersonPPList.append(Item[7:].replace('\n', '') + '-')
    if 'Elixir' in Item:
        PersonEList.append(Item[7:].replace('\n', '') + '-')
    if 'Oil' in Item:
        count += 1
        PersonSOList.append(Item[4:].replace('\n', '') + '-')
        

ItemLength = len(ItemCards)
for x in range(0,ItemLength-1):
    Item = ItemCards[x]
    ItemNext = ItemCards[x+1]
    if 'Potion' in Item:
        PPList.append(Item[7:] + '-')
    if 'Elixir' in Item:
        EList.append(Item[7:]+ '-')
    if 'Oil' in Item:
        SOList.append(Item[4:]+ '-')
    
    
PartyItems.writelines(PPList)
PartyPeople.writelines(PersonPPList)

ElixirItems.writelines(EList)
ElixirPeople.writelines(PersonEList)

SnakeOilItems.writelines(SOList)
SnakeOilPeople.writelines(PersonSOList)
print(count)