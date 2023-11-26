from itertools import permutations
import korSeparator
import engDict
import re
import time
start = time.time()  # 시작 시간 저장


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
    a = []
    for i in engDict.engDict:
        dictWord = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "",i.lower())
        if len(dictWord)==wordLen:
            a.append(dictWord)
    finalResult = list(set(anagram) & set(a))
    if finalResult == []:
        print("영어 사전에 해당하는 단어가 없습니다.")
    else:
        for i in finalResult:
            print(i)
else: 
    a = 1


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간