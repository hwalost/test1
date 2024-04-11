a = 100
b = 200

print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
print(a, "/", b, "=", a/b)


# 여기서 부터 수업 내용
c = a+b
d = a-b
e = a*b
f = a/b

print(f'{a} + {b} = {c}')
print(f'{a} + {b} = {c}')
print(f'{a} + {b} = {c}')
print(f'{a} + {b} = {c}')

# 정수 : integer(int) 12345   - 4byte
# 실수 : floating (float), double      5.4 etc  4, 8 byte
# python double doesnt use only float - 8byte


# 문자
# 문자 : character(char)  - 1,2 byte
# 문자열 : string(str)   - ?byte
# 문자열 + 문자열 :
# 문자열 * 자연수 : repeat
# reserved word 변수명에 예약어 불가능
# 변수명을 썼는데 색이 파란색이면 안된다

# input 함수는 키보드로 값을 입력 받는 함수
#input 함수는 입력값이 숫자인지 문자인지 구분하는 능력 x
# 구분은 사람이

#input() 함수로 입력된 값은 모두 문자열로 취급
# 문자열을 정수로 형변환(type casting)해줘야 숫자로 사용 가능

num1 = input() # num1 = int(input('숫자를 입력하시오'))
num1 = int(num1) # type casting float, int, etc
num2 = '입니다'
num3 = 200
print(num1 + num2)
print(num1 + num3)
