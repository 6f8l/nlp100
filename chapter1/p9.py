import random

def sort_at_random(input_word):
    if len(input_word) <= 4:
        return input_word

    mid_str = "".join(random.sample(input_word[1: len(input_word) - 1], len(input_word) - 2))
    return input_word[0] + mid_str + input_word[-1]

if __name__ == "__main__":
    INPUT_STR = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    ANS = ""
    for word in INPUT_STR.split():
        ANS += sort_at_random(word) + " "
    print(ANS)
