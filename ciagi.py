from math import gcd, lcm

actual_diff = (0, 0)


# obliczanie roznic dla kazdych dwoj kolejnych wyrazow tego ciagu
def fractions_difference(a, b):
    #   a[0]    b[0]    a[0]b[1] - b[0][a1]
    #   a[1]    b[1]        a[1]b[1]
    new_numerator = a[0] * b[1] - b[0] * a[1]
    new_denumerator = a[1] * b[1]

    dzielnik = gcd(new_denumerator, new_numerator)

    return (new_numerator // dzielnik, new_denumerator // dzielnik)


# obliczanie najwiekszej roznicy mozliwej dla tego ciagu
def biggest_diference(R):
    a = R[0]
    b = R[1]
    result = (gcd(a[0], b[0]), lcm(a[1], b[1]))
    for i in range(2, len(R)):
        a = R[i]
        result = (gcd(result[0], a[0]), lcm(result[1], a[1]))

    return result


# obliczanie kolejnego wyrazu ciagu za pomoca poprzedniego i najwiekszej reszty
def calculate_new_fraction(a):
    global actual_diff

    new_denumerator = lcm(a[1], actual_diff[1])
    new_numerator = a[0] * (new_denumerator // a[1]) + actual_diff[0] * (new_denumerator // actual_diff[1])

    nwdResult = gcd(new_denumerator, new_numerator)
    return (new_numerator // nwdResult, new_denumerator // nwdResult)


def main_function(T):
    global actual_diff

    diffs = []
    for i in range(1, len(T)):
        diffs.append(fractions_difference(T[i], T[i - 1]))

    actual_diff = biggest_diference(diffs)

    indeks = 1
    indeksMax = len(T) - 1
    new_fraction = T[0]
    while indeks <= indeksMax:
        new_fraction = calculate_new_fraction(new_fraction)

        if new_fraction == T[indeks]:
            indeks += 1
        else:
            print(f"{new_fraction[0]} {new_fraction[1]}")


k = int(input(""))
fractions = []
for i in range(k):
    line = input()
    a, b = line.split(' ')
    fractions.append((int(a), int(b)))

main_function(fractions)
