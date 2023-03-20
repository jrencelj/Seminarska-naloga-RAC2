def naj_nar_podzap(sez):
    '''vrne dolzino in seznam najdaljsih narascajocih podzaporedji'''
    n = len(sez)
    pom = []
    naj_v = 0
    naj_zap = []
    for el in sez:
        pom.append([1,[el]])
    for i in range(n):
        for j in range(i):
            if sez[i]>sez[j] and pom[i][0] < pom[j][0] + 1:
                pom[i][0] = pom[j][0] + 1
                pom[i][1] = pom[j][1] + [sez[i]]
        if pom[i][0] > naj_v:
            naj_v = pom[i][0]
            naj_zap = pom[i][1]
        elif pom[i][0] == naj_v:
            naj_zap = [naj_zap] + [pom[i][1]]
    return (naj_v, naj_zap)


def naj_pad_podzap(sez):
    '''vrne dolzino in seznam najdaljsih padajocih podzaporedji'''
    n = len(sez)
    pom = []
    naj_v = 0
    naj_zap = []
    for el in sez:
        pom.append([1,[el]])
    for i in range(n):
        for j in range(i):
            if sez[i]<sez[j] and pom[i][0] < pom[j][0] + 1:
                pom[i][0] = pom[j][0] + 1
                pom[i][1] = pom[j][1] + [sez[i]]
        if pom[i][0] > naj_v:
            naj_v = pom[i][0]
            naj_zap = pom[i][1]
        elif pom[i][0] == naj_v:
            naj_zap = [naj_zap] + [pom[i][1]]
    return (naj_v, naj_zap)
