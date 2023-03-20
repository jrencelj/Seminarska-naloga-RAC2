# Vaje 
**Datum:** 22. 3. 2023 
1. Napišite funkcijo `najvecja_vsota(tab)`, ki poišče največjo vsoto v zaporednem podseznamu danega seznama <br>
[-2, 3, 5, -6, -4, 5, -13, 2, 1, 7, -5, -7, 3, 8, -30, -13, 7]\
**Namig:** [Kadanov algoritem](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
---
2. Napišite funkcijo `najvecji_produkt(tab)`, ki poišče največji produkt v zaporednem podseznamu danega seznama <br>
[3, -3, -5, 2, -1, -2, 3, -2]
---
3. Podane so daljice v obliki $(x_1,x_2)$, kjer se $x_1$ nahaja na premici $y=0$ ter $x_2$ na premici $y=1$.<br>
$\Big[(1,2), (3,13), (4,6), (6,8), (7,4), (8,11), (9,12), (10,9), (12,7), (13,3), (14,14)\Big]$\
Napišite funkcijo `najvecja_podmnozica(tab)`, ki poišče in nariše največjo podmnožico, kjer se nobeni dve daljici med seboj ne sekata.\
Prav tako napišite funkcijo, ki poišče in nariše največjo podmnožico, kjer se vsi pari daljic med seboj sekajo.\
**Namig:** [Longest increasing subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)
---
4. Podan imamo seznam števil $A=[a_1 \ldots a_n]$.
* Števila $a$ so lahko negativna, pozitivna ali enaka 0.
* Na vsakem koraku se odločimo ali rečemo *"Ring"* ali *"Ding"*.
> V primeru da rečemo *"Ding"* poberemo $-A[i]$\
> V primeru da rečemo *"Ring"* poberemo $A[i]$

**Omejitve:** Zaporedoma lahko samo trikrat rečemo *“Ring“* ali *“Ding“*.\
[Podrobna navodila so na voljo na 133. strani (16. naloga).](https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf)

Podana koda vrne največjo možno vsoto:
```python
def lisjak(tabela):
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
```
Tvoja naloga je, da zgornjo kodo dopolniš. Koda naj vrne seznam $D$-jev in $R$-jev, ki nam predstavljajo, kaj moramo izreči na $i$-tem indeksu, da bo naša vsota največja možna.
> **Pred dopolnitvijo:** `lisjak([5, 2, 3, 20, -10, -13, 10, 22])`\
> \>>> 81\
> **Po dopolnitvi:** `lisjak([5, 2, 3, 20, -10, -13, 10, 22])`\
> \>>> ['R', 'D', 'R', 'R', 'D', 'D', 'R', 'R']