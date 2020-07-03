# mecab 大文字小文字に注意
import MeCab

print('実行中…')
input_file_name = 'neko.txt'
f =  open(input_file_name,'r')

data = f.read()

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
text = mecab.parse(data)
mecab.parse('')

out_file_name = "neko.txt.mecab"
with open(out_file_name, 'w') as f:
    f.write(text)
print('ファイル出力完了 ファイル名：' + out_file_name)
