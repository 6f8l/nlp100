import gzip
import ast

FNAME = 'jawiki-country.json.gz'
data = []
with gzip.open(FNAME, "rt", "utf_8") as fi:
    for line in fi:
        dic = ast.literal_eval(line)
        if "イギリス" in dic['text']:
            data.append(dic)

print(data)
