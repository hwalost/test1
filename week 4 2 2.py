#for _ in range(5):    # 언더바 : 와일드 카드 / 값을 버림
 #   print("hello")


ap = range(3, 20, 4)
list_ap = list(ap)
print(list_ap)


for i in range(5):
    print(i, end=' ')

    # 팩토리얼 구하는 프로그램
    fac = 1
    N = int(input("enter"))


    for n in range(1, N+1):
        fac = fac * n

    print(f'{N}!은 {fac}입니다')
