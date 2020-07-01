def execute(input_num):
    fname = 'popular-names.txt'
    with open(fname) as data_file:
        arr = data_file.readlines()

    for line in arr[-input_num:]:
        print(line.rstrip())

if __name__ == "__main__":
    print('Type the number of lines you want to display: ')
    user_input = int(input())
    execute(user_input)
