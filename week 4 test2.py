level = input('회원 등급을 적으시오 gold, silver, bronze')
ques = input('지금이 특별 이벤트 기간 입니까? Y/N' )
book = int(input('지금 대출하고 있는 책의 권수를 입력하시오'))
gold = 3
silver = 2

# 삼항 연산자
# cap = 4 if sp == 'yes' else 3


if level == 'bronze':
    print('책을 더이상 대출할 수 없습니다.')
else:
    if ques == 'Y':
        if level == 'gold':
            if book < 4:
                print(gold + 1 - book, '만큼 대출 할 수 있습니다')
            else:
                print('더이상 대출을 할 수 없습니다')
        if level == 'silver':
            if book < 3:
                print(silver + 1 - book, '만큼 대출 할 수 있습니다')
            else:
                print('더이상 대출을 할 수 없습니다')

    if ques == 'N':
        if level == 'gold':
            if book < 3:
                print(gold - book, '만큼 대출 할 수 있습니다')
            else:
                print('더이상 대출을 할 수 없습니다')
        if level == 'silver':
            if book < 2:
                print(silver - book, '만큼 대출 할 수 있습니다')
            else:
                print('더이상 대출을 할 수 없습니다')
