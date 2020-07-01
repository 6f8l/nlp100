FNAME = 'popular-names.txt'
FNAME_COL1 = 'col1.txt'
FNAME_COL2 = 'col2.txt'

with open(FNAME) as data_file, \
    open(FNAME_COL1, mode='w') as f1, \
    open(FNAME_COL2, mode='w') as f2:
    for line in data_file:
        f1.write(line.split()[0] + '\n')
        f2.write(line.split()[1] + '\n')
