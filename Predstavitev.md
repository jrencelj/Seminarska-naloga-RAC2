# **NALOGE IZ DINAMIČNEGA PROGRAMIRANJA**
* Adnan Pajalić
* Jernej Renčelj
* Tom Rupnik Medjedovič

## **Naloga 1**

**Navodilo:**

Podan imamo seznam, ki lahko vsebuje cela števila in poljubne ne številske zname. Naša naloga je:

* Opisati in analizirati algoritem, ki poišče največjo vsoto v zaporednem podseznamu danega seznama.
* Opisati in analizirati algoritem, ki poišče največji produkt v zaporednem podseznamu danega seznama.

### **Naivna rešitev:**
BRUTE FORCE PRISTOP:
Poiščemo vsote vseh možnih zaporednih podseznamov in med njimi poiščemo maksimalnega. Izberemo si $i$-ti element v seznamu, ki predstavlja prvo število trenutne vsote in postopoma dodajamo elemente vse do $n$-tega. S tem dobimo lokalni maksimum $i$-te vsote. Naj bo lokalni maksimum, maksimum vsote vseh možnih podseznamov, ki se začnejo z elementom $A[i]$. Ko pregledamo vse indekse od 1 do $n$, imamo shranjene vse lokalne maksimume za vse indekse. Vzamemo maksimum od vseh lokalnih maksimumov in dobimo rešitev. Vendar ta pristop ni najbolj optimalen. Z večanjem seznama se veča množica vseh podseznamov in stem se časovna zahtevnost povečuje. Časovna zahtevnost je torej zaradi dveh gnezdenih zank $O(n)$. Poglejmo si kako bi lahko izboljšali algoritem.

KADANOV ALGORITEM:\
Tokrat začnemo z iskanjem največje vsote podseznama od zadnjega elementa seznama. Poglejmo si podsezname, ki se končajo z $A[i]$-tim elementom. Recimo, da poznamo lokalni maksimum $i$-tega indeksa. Sedaj želimo izračunati lokalni maksimum $i+1$-ga indeksa. Za izračun le tega ni potrebno izračunati vsot vseh podseznamov do $i+1$-ga indeksa, saj že poznamo izračunane vsote podseznamov do $i$-tega. Zanima nas torej samo vrednost največje vsote do $i$-tega podseznama. Ta ideja nas vodi do principa na kakršen deluje Kadanov algoritem. 

$$lokalni_\ maksimum[i] = max(A[i], A[i] + lokalni_\ maksikum[i-1])$$

Na ta način na vsakem indeksu $i$ problem prevedemo na iskanje maksimuma dveh števil, $A[i]$ in ($A[i]$ + $lokalni_\ maksimum[i-1]$). Velja tudi, da je $lokalni_\ maksimum[0]$ enak $A[0]$.

Na ta način moramo po seznami iterirati zgolj enkrat, kar je torej bistveno hitreje kot na prvi opisan način. Časovna zahtevnost Kadanovega algoritma je $O(n)$.

## **Naloga 2**

* krneki