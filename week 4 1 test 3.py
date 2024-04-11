fac = 1
N = int(input('answer'))


for n in range(1, N+1):
    fac = fac * n
    fac2 = fac + '*'

print(f'{N}!은 {}이므로 {fac}입니다')