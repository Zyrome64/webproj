from math import sqrt
while True:
    try:
        a, b, c = [int(n) for n in input().split()]
        
        if a != 0 and a != 1:
            for i in range(a, 1, -1):
                if a % i == 0 and b % i == 0 and c % i == 0:
                    b /= i
                    if str(b).endswith('.0'):
                        b = int(b)
                    c /= i
                    if str(c).endswith('.0'):
                        c = int(c)
                    a /= i
                    if str(a).endswith('.0'):
                        a = int(a)
                    print(a, b, c, '/{}'.format(i))
                    break
        b = -b
        d = (b ** 2) - (4 * a * c)
        if str(d).endswith('.0'):
            d = int(d)

        x1 = -(a * (sqrt(d) - b) / (2 * a))
        if str(x1).endswith('.0'):
                x1 = int(x1)

        x2 = -(a * (-sqrt(d) - b) / (2 * a))
        if str(x2).endswith('.0'):
                x2 = int(x2)

        if x1 == 0 and str(x1).startswith('-'):
            x1 = 0

        elif x2 == 0 and str(x2).startswith('-'):
            x2 = 0

        if x1 + x2 == b and x1 * x2 == c:
            print('\nD =', d)
            print('x1 =', x1)
            print('x2 =', x2)
            print()

        else:
            print('Нет корней.\nD = {}\n'.format(d))
            continue

    except ValueError:
        try:
            print('Нет корней.\nD = {}\n'.format(d))

        except NameError:
            print('Ошибка\n')
            continue
    except KeyboardInterrupt:
        break

    except ZeroDivisionError:
        print('Нет корней.\nD = {}\n'.format(d))

    except:
        print('Неизвестная ошибка')
