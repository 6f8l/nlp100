def n_gram(tar_str, n):
    return [tar_str[i:i+n] for i in range(len(tar_str) - n + 1)]

print(n_gram("I am an NLPer", 2))
