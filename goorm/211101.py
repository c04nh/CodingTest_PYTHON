# 1단계
# 시험성적 평균과 등급 구하기

user_input = input()
arr = user_input.split(" ")
kor = int(arr[0])
math = int(arr[1])
eng = int(arr[2])
avg = (kor + math + eng) / 3
avg = round(avg, 2)
grade = ''
if avg >= 90:
	grade = 'A'
elif avg >= 80:
	grade = 'B'
elif avg >= 70:
	grade = 'C'
elif avg >= 60:
	grade = 'D'
else:
	grade = 'F'
avg = format(avg, ".2f")
print(f'{avg} {grade}')
