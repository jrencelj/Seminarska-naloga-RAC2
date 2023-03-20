def vsota(sez):
    vsi = []

    def pomozna(i):
        if i == 0:
            vsi.append(sez[0])
            return sez[0]
        else:
            trenutni = max(pomozna(i-1)+sez[i], sez[i])
            vsi.append(trenutni)
            return trenutni
    pomozna(len(sez)-1)
    return max(vsi)


def vsota2(sez):
    glob_naj = 0
    lok_naj = 0
    for i in range(0, len(sez)):
        lok_naj = max(lok_naj+sez[i], sez[i])
        glob_naj = max(lok_naj, glob_naj)
    return glob_naj


def vsota3(sez):
    def pomozna(i):
        if i == 0:
            return (sez[0], sez[0])
        else:
            trenutni = max(pomozna(i-1)[0]+sez[i], sez[i])
            return (trenutni, max(pomozna(i-1)[1], pomozna(i-1)[0]+sez[i], sez[i]))
    return pomozna(len(sez)-1)[1]


testi = [[[-3, -4, 5, -1, 2, -4, 6, -1], 8],
         [[-2, 3, -1, 2], 4], [[-2, -3, 4, -1, -2, 1, 5, -3], 7]]

for test in testi:
    print(
        f'{vsota(test[0])==test[1]} and {vsota2(test[0])==test[1]} and {vsota3(test[0])==test[1]}')
