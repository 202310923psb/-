def display_multiplication_table(n):
    a = 1
    for k in range(1, 10):
        for i in range(n, n + 4):
            print(f'{i} x {a} = {i*a:2d}\t', end = '')
        a += 1
        print()
    print()

display_multiplication_table(2)
display_multiplication_table(6)
