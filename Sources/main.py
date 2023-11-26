from itertools import permutations
import korSeparator
import engDict
import re

def generate_anagrams(word):
    # 문자열의 모든 순열을 생성
    permutationsList = [''.join(p) for p in permutations(word)]
    
    # 중복된 순열을 제거하고 정렬
    uniqueAnagrams = sorted(set(permutationsList))
    
    return uniqueAnagrams

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
    anagram = generate_anagrams(word)
    engDictFinal = [[[[] for n in range(27)] for j in range(27)] for i in range(27)]
    for i in engDict.engDict:
        dictWord = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "",i.lower())
        dictAscii0 = ord(dictWord[0])-97
        dictAscii1 = ord(dictWord[1])-97
        dictAscii2 = ord(dictWord[2])-97
        if len(dictWord) == wordLen:
            if dictAscii0<0:
                if dictAscii1<0:
                    if dictAscii2<0:
                        engDictFinal[26][26][26].append(dictWord)
                    else:
                        engDictFinal[26][26][dictAscii2].append(dictWord)
                else:
                    if dictAscii2<0:
                        engDictFinal[26][dictAscii1][26].append(dictWord)
                    else:
                        engDictFinal[26][dictAscii1][dictAscii2].append(dictWord)
            else:
                if dictAscii1<0:
                    if dictAscii2<0:
                        engDictFinal[dictAscii0][26][26].append(dictWord)
                    else:
                        engDictFinal[dictAscii0][26][dictAscii2].append(dictWord)
                else:
                    if dictAscii2<0:
                        engDictFinal[dictAscii0][dictAscii1][26].append(dictWord)
                    else:
                        engDictFinal[dictAscii0][dictAscii1][dictAscii2].append(dictWord)
    for i in anagram:
        ascii0 = ord(i[0])-97
        ascii1 = ord(i[1])-97
        ascii2 = ord(i[2])-97
        if ascii0<0:
            if ascii1<0:
                if ascii2<0:
                    if i in engDictFinal[26][26][26]:
                        finalResult.append(i)
                else:
                    if i in engDictFinal[26][26][ascii2]:
                        finalResult.append(i)
            else:
                if ascii2<0:
                    if i in engDictFinal[26][ascii1][26]:
                        finalResult.append(i)
                else:
                    if i in engDictFinal[26][ascii1][ascii2]:
                        finalResult.append(i)
        else:
            if ascii1<0:
                if ascii2<0:
                    if i in engDictFinal[ascii0][26][26]:
                        finalResult.append(i)
                else:
                    if i in engDictFinal[ascii0][26][ascii2]:
                        finalResult.append(i)
            else:
                if ascii2<0:
                    if i in engDictFinal[ascii0][ascii1][26]:
                        finalResult.append(i)
                else:
                    if i in engDictFinal[ascii0][ascii1][ascii2]:
                        finalResult.append(i)
    if finalResult == []:
        print("영어 사전에 해당하는 단어가 없습니다.")
    else:
        for i in finalResult:
            print(i)
else: 
    a = 1