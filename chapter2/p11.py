FNAME = 'popular-names.txt'
with open(FNAME) as data_file:
    for line in data_file:
        print(line.replace('\t', ' '), end='')
