import gzip
import json
import re
import numpy as np

FNAME = 'jawiki-country.json.gz'
def extract_UK():
    with gzip.open(FNAME, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']
    raise ValueError('Not found England articles.')

r = re.compile("^=+(.+)=$")
doc = extract_UK().split("\n")
for line in doc:
    match = r.match(line)
    if match:
        s = match.group(0)
        level2 = np.sum([c == "=" for c in s])
        print(level2 // 2 - 1, s)
