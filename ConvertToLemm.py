import pymorphy2

res = set()

with open("good_words.txt", 'r', encoding = 'utf-8') as f:
    text = f.read().split()

morph = pymorphy2.MorphAnalyzer()

for word in text:
    p = morph.parse(word)[0]
    res.add(p.normal_form)
resFile = open("res.txt", 'w', encoding = 'utf-8')
for word in res:
    resFile.write(word + '\n')
    print(word)
resFile.close()


