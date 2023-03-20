def produkt(sez):
    glob_max = sez[0]
    lok_max = sez[0]
    lok_min = sez[0]
    for i in range(1, len(sez)):
        el = sez[i]
        if el < 0:
            lok_max, lok_min = lok_min, lok_max
        lok_max = max(lok_max*el, el)
        lok_min = min(lok_min*el, el)
        glob_max = max(glob_max, lok_max)
    return glob_max


def produkt2(sez):
    glob_max = sez[0]
    produkt1 = sez[0]
    produkt2 = sez[0]
    for i in range(1, len(sez)):
        el = sez[i]
        produkt1, produkt2 = max(
            produkt1*el, produkt2*el, el), min(produkt2*el, produkt1*el, el)
        glob_max = max(glob_max, produkt1, produkt2)
    return glob_max


testi = [[[9, -6, 10, 3], 30], [[6, -3, -10, 0, 2], 180],
         [[-2, -3, 0, -2, -40], 80]]

for test in testi:
    print(f'{produkt(test[0])==test[1]} and {produkt2(test[0])==test[1]}')
