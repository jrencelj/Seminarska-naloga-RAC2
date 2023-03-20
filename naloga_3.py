import time                         # Štoparica

import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov

def lisjak_kot_kovanci(tabela):
    n = len(tabela) - 1
    memo = {}
    def pomozna(i, ring, ding):
        if i > n:
            return 0
        if (i, ring, ding) in memo:
            return memo[(i, ring, ding)]
        if ring == 3:
            r = -tabela[i] + pomozna(i + 1, 0, ding + 1)
            d = -tabela[i] + pomozna(i + 1, 0, ding + 1)
        elif ding == 3:
            d = tabela[i] + pomozna(i + 1, ring + 1, 0)
            r = tabela[i] + pomozna(i + 1, ring + 1, 0)
        else:
            r = tabela[i] + pomozna(i + 1, ring + 1, 0)
            d = -tabela[i] + pomozna(i + 1, 0, ding + 1)
        memo[(i, ring, ding)] = max(r, d)
        return memo[(i, ring, ding)]
    return pomozna(0, 0, 0)


def lisjak_kateri(tabela):
    n = len(tabela) - 1
    memo = {}

    def vrednost(i, izreci):
        vsota = 0
        for j in range(i, len(izreci) + i):
            if izreci[j - i] == 'D':
                vsota -= tabela[j]
            elif izreci[j - i] == 'R':
                vsota += tabela[j]
        return vsota
    
    def pomozna(i, ring, ding):
        if i > n:
            return []
        if (i, ring, ding) in memo:
            return memo[(i, ring, ding)]
        if ring == 3:
            r = ['D'] + pomozna(i + 1, 0, ding + 1)
            d = ['D'] + pomozna(i + 1, 0, ding + 1)
        elif ding == 3:
            d = ['R'] + pomozna(i + 1, ring + 1, 0)
            r = ['R'] + pomozna(i + 1, ring + 1, 0)
        else:
            r = ['R'] + pomozna(i + 1, ring + 1, 0)
            d = ['D'] + pomozna(i + 1, 0, ding + 1)
        vrednost_r = vrednost(i, r)
        vrednost_d = vrednost(i, d)
        if vrednost_r > vrednost_d:
            memo[(i, ring, ding)] = r
        else:
            memo[(i, ring, ding)] = d
        return memo[(i, ring, ding)]
    return pomozna(0, 0, 0)



def lisjak(tabela):
    n = len(tabela)
    memo = {}
    def pomozna(i, ring, ding):
        if i >= n:
            return 0
        if (i, ring, ding) in memo:
            print("HELLO")
            return memo[(i, ring, ding)]
        if ring == 3:
            d = -tabela[i] + pomozna(i + 1, 0, ding + 1)
            r = -float("inf")
        elif ding == 3:
            r = tabela[i] + pomozna(i + 1, ring + 1, 0)
            d = -float("inf")
        else:
            r = tabela[i] + pomozna(i + 1, ring + 1, 0)
            d = -tabela[i] + pomozna(i + 1, 0, ding + 1)
        memo[(i, ring, ding)] = max(r, d)
        print(memo)
        return memo[(i, ring, ding)]
    return pomozna(0, 0, 0)

def lisjak_ring_in_ding(tabela):
    n = len(tabela)
    memo = {}
    def vrednost(i, izreci):
        vsota = 0
        for j in range(i, len(izreci) + i):
            if izreci[j - i] == 'D':
                vsota -= tabela[j]
            elif izreci[j - i] == 'R':
                vsota += tabela[j]
        return vsota
    def pomozna(i, ring, ding):
        if i >= n:
            return []
        if (i, ring, ding) in memo:
            return memo[(i, ring, ding)]
        if ring == 3:
            d = ['D'] + pomozna(i + 1, 0, ding + 1)
            r = []
        elif ding == 3:
            r = ['R'] + pomozna(i + 1, ring + 1, 0)
            d = []
        else:
            r = ['R'] + pomozna(i + 1, ring + 1, 0)
            d = ['D'] + pomozna(i + 1, 0, ding + 1)
        vrednost_r = vrednost(i, r)
        vrednost_d = vrednost(i, d)
        if vrednost_r > vrednost_d:
            memo[(i, ring, ding)] = r
        else:
            memo[(i, ring, ding)] = d
        print(memo)
        return memo[(i, ring, ding)]
    return pomozna(0, 0, 0)

def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    # NAMIG: klic funkcije `time.perf_counter()` vam vrne število sekund od 
    # neke točke v času. Če izmerite čas pred izračunom funkcije in čas po 
    # končanem izračunu, vam razlika časov pove čas izvajanja (funkcija je 
    # natančnejša od time.time()).
    zacetni = time.perf_counter()
    fun(primer)
    koncni = time.perf_counter() - zacetni
    return koncni


def oceni_potreben_cas(fun, gen_primerov, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """

    # NAMIG: `k`-krat generirajte nov testni primer velikosti `n` s klicem
    # `gen_primerov(n)` in izračunajte povprečje časa, ki ga funkcija porabi za
    # te testne primere.
    vsota = 0
    for _ in range(k):
        primer = gen_primerov(n)
        vsota += izmeri_cas(fun, primer)    
    return vsota / k

def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k, shrani = False):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev. """

    # NAMIG: preprost graf lahko narišemo z `plt.plot(sez_x, sez_y, 'r')`, ki z
    # rdečo črto poveže točke, ki jih definirata seznama `sez_x` in `sez_y`. Da
    # se graf prikaže uporabniku, uporabimo ukaz `plt.show()`. Za lepše grafe
    # si poglejte primere knjižnice [matplotlib.pyplot] (ki smo jo preimenovali
    # v `plt`).
    sez_x = sez_n
    sez_y = [oceni_potreben_cas(fun, gen_primerov, n, k) for n in sez_n]
    plt.plot(sez_x, sez_y, 'r')
    if shrani:
        plt.savefig("casovna_zahtevnost.png")
    plt.show()

def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(-n, n) for _ in range(n)]

# TESTNI PRIMERI
tab = [-1000, -1000, -1000, -1000, -1000]
# tab1 = [-10, 10, -10, 10, 10, 10]
tab1 = [5, 2, 3, 20, -10, -13, 10, 22]
tab2 = [-10, 10]
tab3 = [i for i in range(100)]
print(lisjak_kot_kovanci(tab1))
print(lisjak_kateri(tab1))
# narisi_in_pokazi_graf(lisjak, test_gen_sez, [i for i in range(100)], 30, True)
