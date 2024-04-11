# 랜덤 숫자 뽑기
import random # 이코드에서 random 모듈 사용

num = random.randint(1,45)  # 숫자만 입력, 1~45의 숫자 중 하나를 선택
print(num)


age = int(input('나이를 입력하시오'))
if age < 18 :
    print('아쉽군요. 협조 감사드립니다')
else :
    print('즐겜, 협조감사드립니')