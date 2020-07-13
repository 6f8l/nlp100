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
    r = re.compile(r"\[\[Category:(.+)\]\]")
    doc = extract_uk().split("\n")
    for line in doc:
        match = r.match(line)
        if match:
            print(match.group(1))
