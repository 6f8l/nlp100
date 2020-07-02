import gzip
import json
import re

FNAME = 'jawiki-country.json.gz'
def extract_UK():
    with gzip.open(FNAME, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']
    raise ValueError('Not found England articles.')

r = re.compile("\[\[Category:(.+)\]\]")
doc = extract_UK().split("\n")
for line in doc:
    match = r.match(line)
    if match:
        print(match.group(1))
