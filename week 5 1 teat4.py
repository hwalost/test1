# 2. 부호를 번갈아 가면서 함산하는 방법
n = 2
result = 3
sign = 1


while True:
    mul = 1
    for i in range(n, n+3):
        print(i, end=' ')
        mul = mul*i
    result = result + sign * 4 / mul
    print(f'결과 : {result}')
    n += 2
    sign = -sign