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
