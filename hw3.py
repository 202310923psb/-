def get_fixed_price(cut, name):
    price = int(input(name + ' 상품의 할인된 가격은? '))
    result = price / (100 - cut) * 100
    return result

cut = int(input("할인율은? "))
A_original = get_fixed_price(cut, 'A')
B_original = get_fixed_price(cut, 'B')
print('A 상품의 정가는', A_original, '원')
print('B 상품의 정가는', B_original, '원')
