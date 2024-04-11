#변수 선언할때 자료형도 함깨 선언
#ex int var1 = 100; 해당 변수에는 같은 자료형의 값만 대입 가능

#var1:.3f 소수점 3자리까지

# escape character (문자) 백슬레쉬 (\)
# 다음에 오는 문자가 문법적으로 탈출한다

# "안녕! 이라는 문자열 출력"
print("\"안녕!\"")
print("문자열에서 개행 문자를 넣고 싶을 땐 \\n 을 쓰면 됩니다")

# 표현하려는 문장에 큰따옴표가 있으면 문자열을 작은따옴표로 감싸면 됩
print('"hello"')

print("'ex'")

print(''' "hi" 'hello' ''')



# len 문자열의 길이 파악 문자뿐만 아니라 순서가 있는 데이터형 모두 사용 가능

# upper, lower 대문자를 소문자로 소문자를 대문자로 문자열에 대해서만 적용
# 함수 자체가 str 클래스에서 정의
# 문자열 변수 클래스 함수() 형태로 사용

word = "wtf"
print(len(word))
len(word)


print(word.upper())

# isupper(): 문자열이 모두 대문자이면 true를 반환함

# count() 특정 단어가 변수에 몇번 나왔는지 파악

print(word.count('w'))

# find 어떤 글자가 문자열의 몇 번째에 위치하는 지 알려줌

print(word[2]) # 인덱싱
# 순번 인덱싱은 0 부터 시작


abc = 3.141592
print(f'{abc:.3f}')