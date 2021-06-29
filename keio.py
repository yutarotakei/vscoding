upper = int(input('１からなにまで'))

def multiple(n):
    if 1 <= n <= 3: w = 2
    elif 4 <= n <= 9: w = 3
    elif 10 <= n <= 30: w = 4
    else: return False

    f = '{{:{}d}}'.format(w)
    print('=' * w * n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f.format(i*j), end='')
        print()
    print('=' * w * n)
    return True

multiple(upper)