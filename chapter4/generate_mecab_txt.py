# mecab 大文字小文字に注意
import MeCab

print('実行中…')
I_FNAME = 'neko.txt'
f = open(I_FNAME, 'r')

data = f.read()

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
text = mecab.parse(data)
mecab.parse('')

O_FNAME = "neko.txt.mecab"
with open(O_FNAME, 'w') as f:
    f.write(text)
print('ファイル出力完了 ファイル名：' + O_FNAME)
