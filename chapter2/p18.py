# import pandas as pd

# df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
# print(df.sort_values(2, ascending=False))

FNAME = 'popular-names.txt'
lines = open(FNAME).readlines()
lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for line in lines:
    print(line, end='')
