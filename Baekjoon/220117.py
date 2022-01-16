# 알파벳 찾기

word = input()
for i in range(97, 123):
    print(word.find(chr(i)))