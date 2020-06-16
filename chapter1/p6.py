def n_gram(tar_str, num):
    return [tar_str[i: i + num] for i in range(len(tar_str) - num + 1)]

def print_se_include(alp, ele):
    if "se" in ele:
        print("\"se\"は{}に含まれています".format(alp))
    else:
        print("\"se\"は{}に含まれていません".format(alp))

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print("和集合: {}".format(str(X | Y)))
print("積集合: {}".format(str(X & Y)))
print("差集合: {}".format(str(X - Y)))

print_se_include('X', X)
print_se_include('Y', Y)
