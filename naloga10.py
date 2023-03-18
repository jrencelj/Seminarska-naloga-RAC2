def najdaljse_podzaporedjeV2(tab):
    d = len(tab)
    def pomozna(z, k, m):
        print(z, k, m)
        tabele = []
        if z == k:
            if tab[z] > m:
                memo[(z, k, m)] = 1
            else:
                memo[(z, k, m)] = 0
        if k < z:
            return 0
        if (z, k, m) in memo.keys():
            return memo[(z, k, m)]
        t = 0
        for i in range(z, k + 1):
            if tab[i] < m:
                continue
            if (i + 1) % 2 == 0:
                t = 1 + pomozna(0, i - 1, tab[i])
            elif (i + 1) % 2 == 1:
                t = 1 + pomozna(i + 1, d - 1, tab[i])
            tabele.append(t)
        memo[(z, k, m)] = max(tabele) if tabele != [] else 0
        print(memo)
        return memo[(z, k, m)]
    memo = {}
    return pomozna(0, d - 1, -float("inf"))

def najdaljse_naprej_nazaj_zaporedje(tab):
    n = len(tab)
    # def L(i):
    #     for j in range(i):
    # 
    #     return None
    # def R(i):
    #     return None
    def pomozna(i):
        if i >= n:
            return 0
        if (i) in memo.keys():
            return memo[i]
        for i in range(n):
            if (i + 1) % 2 == 1:
                continue # Gledamo desne.
            elif (i + 1) % 2 == 0:
                continue # Gledamo leve.

    memo = {}
    return pomozna(0)

def najdaljse_podzaporedje(tab):
    d = len(tab)
    tab = tuple(tab)
    def pomozna(z, k, m):
        # print(tab[z:k+1], m)
        tabele = []
        if z == k:
            if tab[z] > m:
                memo[(tab[z:k+1], m)] = 1
            else:
                memo[(tab[z:k+1], m)] = 0
        if k < z:
            return 0
        if (tab[z:k+1], m) in memo.keys():
            # print("HELLO")
            return memo[(tab[z:k+1], m)]
        t = 0
        for i in range(z, k + 1):
            if tab[i] <= m:
                continue
            if (i + 1) % 2 == 0:
                t = 1 + pomozna(0, i - 1, tab[i])
            elif (i + 1) % 2 == 1:
                t = 1 + pomozna(i + 1, d - 1, tab[i])
            tabele.append(t)
        memo[(tab[z:k+1], m)] = max(tabele) if tabele != [] else 0
        print(memo)
        return memo[(tab[z:k+1], m)]
    memo = {}
    return pomozna(0, d - 1, -float("inf"))
        
    

# TESTNI PRIMERI
tab = [1, 1, 8, 7, 5, 6, 3, 6, 4, 4, 8, 3, 9, 1, 2, 2, 3, 3, 4, 0]
tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
tab2 = [1, 1, 8, 7, 5, 6, 3, 6, 4, 4]
tab3 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
tab4 = [1, 1, 8, 7, 5, 6, 3, 6, 4]
tab5 = [10, 9, 1, 2, 3, 5, 0]
print(najdaljse_podzaporedje(tab))