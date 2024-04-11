num_list = [0, 0, 0, 0]

# 인덱스를 이용해 num_list 에 직접 접근하여 값을 수정
# 인덱스에 해당하는 0 ~ 3 수열이 필요
for i in range(4): # for i in range(len(num_list))
    num_list[i] = int(input('숫자 :'))

print(num_list)


# 인덱스를 이용한 값 접근
hap = 0
for i in range(4):
    hap += num_list[i]
print(f'총합 : {hap}')


hap = 0
for n in num_list:
    hap += n
print(f'총합 : {hap}')

