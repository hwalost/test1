# 가위바위보
import random

me = input('가위 바위 보 중에 입력')
com = random.choice(['가위', '바위', '가위'])

print(f'나: {me}')
print(f'컴: {com}')

if me == '가위':
    if com == '가위':
        print('비겼습니다')
    elif com == '바위' :
        print('lose')
    elif com == '보' :
        print('win')

if me == '가위':
    if com == '가위':
        print('비겼습니다')
    elif com == '바위' :
        print('lose')
    elif com == '보' :
        print('win')

if me == '가위':
    if com == '가위':
        print('비겼습니다')
    elif com == '바위' :
        print('lose')
    elif com == '보' :
        print('win')
