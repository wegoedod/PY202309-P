import korSeparator
import engDict
import korDict
import re

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
word = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "", input("아나그램에 사용할 단어를 입력해주세요: ").lower())
    
wordLen = len(word)

if lang == "0":
    finalResult = []
    engWordSpells = sorted(list(word))
    for i in engDict.engDict:
        dictWord = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "",i.lower())
        if len(dictWord)==wordLen:
            if engWordSpells == sorted(list(dictWord)):
                finalResult.append(dictWord)
    if word in finalResult:
        finalResult.remove(word)
    if finalResult:
        for i in range(len(finalResult)):
            print(f"{i+1}. {finalResult[i]}")
    else:
        print("국어 사전에 해당하는 단어가 없습니다.")
else: 
    wordSpells = korSeparator.korSeparator(word)
    wordSpellsLenght = len(wordSpells)
    korDictFinal = []
    korWordSpells = []
    sortedwordSpells = sorted(wordSpells)
    finalResult = []
    for i in korDict.korDict:
        i = i.rstrip("\n")
        if len(i)==wordLen:
            korWordSpell = korSeparator.korSeparator(i)
            if len(korWordSpell)==wordSpellsLenght:
                korDictFinal.append(i)
                korWordSpells.append(korWordSpell)
    for i in range(len(korWordSpells)):
        if sortedwordSpells == sorted(korWordSpells[i]):
            finalResult.append(korDictFinal[i])
    if word in finalResult:
        finalResult.remove(word)
    if finalResult:
        for i in range(len(finalResult)):
            print(f"{i+1}. {finalResult[i]}")
    else:
        print("국어 사전에 해당하는 단어가 없습니다.")