import collections

FNAME = 'popular-names.txt'
lines = open(FNAME).readlines()

names = [line.split()[0] for line in lines]
name_c = collections.Counter(names)

name_sorted = sorted(name_c.items(), key=lambda x: x[1], reverse=True)
print(name_sorted)
