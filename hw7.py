shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    num = int(input('수량은? '))
    if item in shopping_bag:
        shopping_bag[item] += num
    else:
        shopping_bag[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다.\n')
print()
print(f'>>> 장바구니 보기:{shopping_bag}\n')
if not shopping_bag == {}:
    print('[검색]')
    find_name = input('장바구니에서 확인하고자 하는 상품은? ')
    while find_name not in shopping_bag:
        print(f'{find_name}은 장바구니에 존재하지 않습니다. 다시 입력해주세요.')
        find_name = input('장바구니에서 확인하고자 하는 상품은? ')
    print(f'{find_name}은(는) {shopping_bag[find_name]}개 담겨있습니다.')
else:
    print('장바구니가 비어있습니다.')
