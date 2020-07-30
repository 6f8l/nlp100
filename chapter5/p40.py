class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

doc = []

skip_empty_line = False

with open("ai.ja.txt.cabocha") as f:
    lines = f.readlines()
    sentence = []
    for line in lines:
        line = line[:-1]
        if line.startswith("*"):
            continue
        if line == "EOS":
            if not skip_empty_line or len(sentence) > 0:
                doc.append(sentence)
            sentence = []
            continue
        surface, rest = line.split("\t")
        rest = rest.split(",")

        assert len(rest) >= 6
        pos, pos1, base = rest[0], rest[1], rest[2]

        m = Morph(surface, base, pos, pos1)
        sentence.append(m)

print(" ".join(map(lambda x: x.surface, doc[2])))
