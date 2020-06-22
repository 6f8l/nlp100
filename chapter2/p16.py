def execute(input_num):
    fname = 'popular-names.txt'
    with open(fname) as data_file:
        arr = data_file.readlines()

    for line in arr[-input_num:]:
        print(line.rstrip())

if __name__ == "__main__":
    user_input = int(input('num: '))
    execute(user_input)