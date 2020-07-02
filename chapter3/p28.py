import gzip
import json
import re

FNAME = 'jawiki-country.json.gz'
def extract_uk():
    with gzip.open(FNAME, 'rt') as data_file:
        for row in data_file:
            data_json = json.loads(row)
            if data_json['title'] == 'イギリス':
                return data_json['text']
    raise ValueError('Not found England articles.')

if __name__ == "__main__":
    rstart = re.compile(r"^{{基礎情報(.+)")
    rend = re.compile(r"^}}")
    r = re.compile(r"^\|(.+) = (.+)")
    doc = extract_uk().split("\n")

    ENTER = False
    END = False

    d = {}
    rpattern = r'\'|\[+|\]+|{+|}+'

    for line in doc:
        if END:
            break
        if not ENTER:
            if rstart.match(line):
                ENTER = True
                continue
        elif ENTER:
            for it in r.finditer(line):
                d[it.group(1)] = re.sub(rpattern, '', it.group(2))
            if rend.match(line):
                END = True
                continue
        else:
            pass
    for k, v in d.items():
        print("{}: {}".format(k, v))
