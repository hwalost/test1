person = int(input('총 인원수를 입려하세요'))
place = int(input('총 숙박비를 입력하세요'))
eat = int(input('예상 총 식비를 입력하세요'))
etc = int(input('기타 경비를 입력하세요'))
mass = place + eat + etc
print(f'전체 경비는 {mass}원이며 인원 수가 {person}명일때 각자 부담 해야 할 금액은 {mass/person}원 입니다')


msg = f'전체 여행 경비'
msg = msg + f'인원수'
msg += f''