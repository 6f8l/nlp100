def n_gram(tar_str, n):
    return [tar_str[i: i + n] for i in range(len(tar_str) - n + 1)]

def printSeInclude(alp, ele):
    if "se" in ele:
        print("\"se\"は{}に含まれています".format(alp))
    else:
        print("\"se\"は{}に含まれていません".format(alp))

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

print("和集合: {}".format(str(X | Y)))
print("積集合: {}".format(str(X & Y)))
print("差集合: {}".format(str(X - Y)))

printSeInclude('X', X)
printSeInclude('Y', Y)
