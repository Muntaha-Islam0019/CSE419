from re import split

name = input()

# splitting by "" causes an element "" in the array so im removing it
letters = set(split("", name))
letters.remove("")

if len(letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
