import re
def korSeparator(string):
    # 유니코드 한글 시작 : 44032, 끝 : 55203
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28
    
    # 초성 리스트. 0 ~ 18
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    
    # 중성 리스트. 0 ~ 20
    JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    
    # 종성 리스트. 0 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    
    print(string)
    sp_list = list(string) # string make list

    result = []
    for keyword in sp_list:

        # 한글 여부 check 후 분리
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
            if keyword in CHOSUNG_LIST or keyword in JUNGSUNG_LIST or keyword in JONGSUNG_LIST:
                result.append(keyword)
            else:
                # 초성
                char_code = ord(keyword) - BASE_CODE
                print(char_code)
                char1 = char_code // CHOSUNG
                result.append(CHOSUNG_LIST[char1])

                # 중성
                char2 = (char_code - (CHOSUNG * char1)) // JUNGSUNG
                result.append(JUNGSUNG_LIST[char2])
                
                # 종성
                char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
                result.append(JONGSUNG_LIST[char3])
                
        else:
            result.append(keyword)
    print("".join(result)) # 자소 분리 결과 출력
    return result