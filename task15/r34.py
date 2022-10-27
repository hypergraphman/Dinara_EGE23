for a in range(1, 100):
    is_a = True
    for k in range(1, 1000):
        for n in range(1, 1000):
            if not ((5 * k + 6 * n > 57) or ((k <= a) and (n < a))):
                is_a = False
                break
        if not is_a:
            break
    if is_a:
        print(a)
        break
