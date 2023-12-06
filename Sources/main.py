import korSeparator
import engDict
import re
import time
start = time.time()  # 시작 시간 저장


def generateAnagrams(word,engdict):
    def generate(currrent, remaining):
        if not remaining:
            uniqueAnagrams.add(currrent)
            return
        cmp = len(currrent)
        if cmp>1:
            PASS = 1
            for i in engdict:
                if i[:cmp]==currrent:
                    PASS = 0
                    break
            if PASS:
                return
        for i in range(len(remaining)):
            generate(currrent + remaining[i], remaining[:i] + remaining[i+1:])
    lengthWord = len(word)
    uniqueAnagrams = set()
    generate('', word)
    return  sorted(set(uniqueAnagrams))

while 1:
    lang = input("영어와 한국어 중 생성할 아나그램을 선택하세요.(0=영어,1=한국어): ")
    if lang == "0":
        print("선택한 언어(영어)")
        break
    elif lang == "1":
        print("선택한 언어(한국어)")
        break
    else:
        print("0과 1만 입력해주세요.")
while 1:
    word = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "", input("아나그램에 사용할 단어를 입력해주세요: ").lower())
    if len(word)<3:
        print("세 글자 이상 입력해주세요(특수문자 제외)")
    else:
        break
wordLen = len(word)
if lang == "1":
    wordSpells = korSeparator.korSeparator(word)
if lang == "0":
    finalResult = []
    engDictFinal = set()
    for i in engDict.engDict:
        dictWord = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "",i.lower())
        if len(dictWord)==wordLen:
            engDictFinal.add(dictWord)
    anagram = generateAnagrams(word,engDictFinal)
    finalResult = sorted(list(set(anagram) & engDictFinal))
    if finalResult == []:
        print("영어 사전에 해당하는 단어가 없습니다.")
    else:
        for i in finalResult:
            print(i)
else: 
    a = 1


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간