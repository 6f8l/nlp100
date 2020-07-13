d = {}

doc = []

with open("neko.txt.mecab") as f:
    lines = f.readlines()
    sentenses = []
    for line in lines:
        line = line[:-1]
        if line == "EOS":
            if len(sentenses) > 0:
                doc = sentenses
            sentenses = []
            continue

        surface, rest = line.split("\t")
        rest = rest.split(",")

        assert len(rest) >= 6
        pos, pos1, base = rest[0], rest[1], rest[6]

        key = (surface, base, pos, pos1)
        d[key] = surface
        sentenses.append(key)

for i, ele in enumerate(doc):
    if i in (0, 1):
        pass
    else:
        if doc[i][2] == "名詞" and doc[i - 1][2] == "助詞" and doc[i - 1][0] == "の" and doc[i-2][2] == "名詞":
            print(doc[i][0] + doc[i - 1][0] + doc[i - 2][0])
