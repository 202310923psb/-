def buy(dic):
    while True:
        print('[구입]')
        item = input('상품명? ')
        if item == '':
            print()
            return False
        num = int(input('수량은? '))
        if item in dic:
            dic[item] += num
        else:
            dic[item] = num
        print(f'장바구니에 {item} {num}개가 담겼습니다.\n')

def show(dic):
    print(f'>>> 장바구니 보기:{dic}')
    print()

def find(dic):
    if not dic == {}:
        print('[검색]')
        find_name = input('장바구니에서 확인하고자 하는 상품은? ')
        if find_name not in dic:
            print(f'장바구니에 {find_name}은(는) 없습니다.')
            return None
        print(f'{find_name}은(는) {dic[find_name]}개 담겨있습니다.')
    else:
        print('장바구니가 비어있습니다.')


shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
