# comments are for my own understanding as ami onek childish

from sys import stdin
from re import split

text = stdin.read()

# lowering, as it's case insentive
text = text.strip().lower()

# using regex: starts with a-z; so commas, semicolons are removed
words = set(split(r'[^a-z]', text))

for word in sorted(words):

    # if word exists
    if(word):
        print(word)
