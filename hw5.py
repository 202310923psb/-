def read_single_digit(num):
    if num == '1':
        return '일'
    elif num == '2':
        return '이'
    elif num == '3':
        return '삼'
    elif num == '4':
        return '사'
    elif num == '5':
        return '오'
    elif num == '6':
        return '육'
    elif num == '7':
        return '칠'
    elif num == '8':
        return '팔'  
    elif num == '9':
        return '구'
    elif num == '0':
        return '영'
    else:
        print('오류: 숫자가 아닌 문자가 포함되어 있습니다! "E"가 출력된 자리의 수를 확인하십시오.')
        return 'E'

def read_number(num):
    num = str(num)
    if len(num) == 1:
        a1 = read_single_digit(num)
        return f'{a1}'
    elif len(num) == 2:
        a1 = read_single_digit(num[0])
        a2 = read_single_digit(num[1])
        return f'{a1} {a2}'
    elif len(num) == 3:
        a1 = read_single_digit(num[0])
        a2 = read_single_digit(num[1])
        a3 = read_single_digit(num[2])
        return f'{a1} {a2} {a3}'
    else:
        return '오류: 입력 가능한 자릿수가 초과되었습니다.'

num = int(input('세 자리 정수 입력: '))    
korean = read_number(num)
print(korean)
