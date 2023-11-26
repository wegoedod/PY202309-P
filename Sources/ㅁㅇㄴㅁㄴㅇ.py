import re

fp = open("engWords.txt","r",encoding="utf-8")
wp = open("engWords123.txt","w",encoding="utf-8")
a = []
for i in fp:
    dictWord = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "",i.lower())
    if len(dictWord)>=3:
        a.append(i)
for i in a:
    wp.write(i)
fp.close()
wp.close()