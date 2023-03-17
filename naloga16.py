def gospod_lisjak(tabela):
    dolzina = len(tabela)
    def pomozna(i, ring = 0, ding = 0):
        if i >= dolzina:
            return 0
        if (i, ring, ding) in memo.keys():
            return memo[(i, ring, ding)]
        if ring == 3 or ding == 3:
            if ring == 3:
                d = -tabela[i] + pomozna(i + 1, ring = 0, ding = ding + 1)
                r = pomozna(i + 1, ring = 0, ding = ding)
            if ding == 3:
                r = tabela[i] + pomozna(i + 1, ring = ring + 1, ding = 0)
                d = pomozna(i + 1, ding = 0, ring = 0)
        else:
            r = tabela[i] + pomozna(i + 1, ring = ring + 1, ding = 0) # Reče 'RING'
            d = -tabela[i] + pomozna(i + 1, ring = 0, ding = ding + 1) # Reče 'DING'
        memo[(i, ring, ding)] = max(r, d)
        return memo[(i, ring, ding)] 
    memo = {}
    return pomozna(0)


# TESTNI PRIMERI
tab = [-1000, -1000, -1000, -1000]
tab1 = [1, 2, 3, 2, -10, -100, -100, -100, -100, -100, -1000000]
print(gospod_lisjak(tab))
