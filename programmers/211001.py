# 1단계
# 이상한 문자 만들기

def solution(s):
    word_list = s.split(" ")
    upper_word = []
    for a in word_list:
        word = ""
        for i, b in enumerate(a):
            if i % 2 == 0:
                word += b.upper()
            else:
                word += b.lower()
        upper_word.append(word)
    answer = " ".join(upper_word)
    return answer