FNAME = 'merged-col.txt'
FNAME_COL1 = 'col1.txt'
FNAME_COL2 = 'col2.txt'

with open(FNAME, mode='w') as data_file, \
    open(FNAME_COL1) as f1, \
    open(FNAME_COL2) as f2:
    for col1_line, col2_line in zip(f1, f2):
        data_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')
