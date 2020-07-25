import gzip
import json
import re
import urllib.request

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

    for line in doc:
        if END:
            break
        if not ENTER:
            if rstart.match(line):
                ENTER = True
                continue
        elif ENTER:
            for it in r.finditer(line):
                d[it.group(1)] = it.group(2)
            if rend.match(line):
                END = True
                continue
        else:
            pass

flag_image_title = d["国旗画像"].replace(" ", "+")
URL_BASE = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:{}&prop=imageinfo&iiprop=url&format=json"
URL = URL_BASE.format(flag_image_title)
response = urllib.request.urlopen(URL)
data = json.loads(response.read().decode("utf-8"))
pages = data["query"]["pages"]
for k in pages.keys():
    if "imageinfo" in pages[k].keys():
        print(pages[k]["imageinfo"][0]["url"])
