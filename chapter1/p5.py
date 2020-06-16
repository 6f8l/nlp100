def n_gram(tar_str, num):
    return [tar_str[i:i+num] for i in range(len(tar_str) - num + 1)]

print(n_gram("I am an NLPer", 2))
