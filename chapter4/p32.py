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

for ele in doc:
    if ele[2] == "動詞":
        print(ele[1])
