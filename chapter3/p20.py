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

if __name__ == "__main__":
    print(extract_UK())
