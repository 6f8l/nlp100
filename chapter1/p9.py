import random

def SortAtRandom(word):
    if len(word) <= 4:
        return word

    mid_str = "".join(random.sample(word[1: len(word) - 1], len(word) - 2))
    return word[0] + mid_str + word[-1]

INPUT_STR = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = ""
for word in INPUT_STR.split():
    ans += SortAtRandom(word) + " "
print(ans)
