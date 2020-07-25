import matplotlib.pyplot as plt

d = {}

doc = []

with open("neko.txt.mecab") as f:
    lines = f.readlines()
    sentense = []
    for line in lines:
        line = line[:-1]
        if line == "EOS":
            if len(sentense) > 0:
                doc.append(sentense)
            sentense = []
            continue

        surface, rest = line.split("\t")
        rest = rest.split(",")

        assert len(rest) >= 6
        pos, pos1, base = rest[0], rest[1], rest[6]

        key = (surface, base, pos, pos1)
        d[key] = surface
        sentense.append(key)

ans_dict = {}
for ele in doc[0]:
    if ele[0] in ans_dict:
        ans_dict[ele[0]] += 1
    else:
        ans_dict[ele[0]] = 0

ans_arr = sorted(ans_dict.items(), key=lambda x: x[1], reverse=True)
labels = []
heights = []
numbers = []
for i, ele in enumerate(ans_arr):
    if i <= 9:
        labels.append(ele[0])
        heights.append(ele[1])
        numbers.append(i)

plt.bar(numbers, heights, tick_label=labels)
plt.show()
