import gzip
import json
import re
import numpy as np

FNAME = 'jawiki-country.json.gz'
def extract_uk():
    with gzip.open(FNAME, 'rt') as data_file:
        for row in data_file:
            data_json = json.loads(row)
            if data_json['title'] == 'イギリス':
                return data_json['text']
    raise ValueError('Not found England articles.')

if __name__ == "__main__":
    r = re.compile(r"^=+(.+)=$")
    doc = extract_uk().split("\n")
    for line in doc:
        match = r.match(line)
        if match:
            s = match.group(0)
            level2 = np.sum([c == "=" for c in s])
            print(level2 // 2 - 1, s)
