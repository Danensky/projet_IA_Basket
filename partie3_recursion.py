import time
import sys

# augmenter la limite de recursivite pour evité toutes les erreur
sys.setrecursionlimit(2000)

# 1. liste des joueurs tirés par score
joueurs_tries = [
    {"nom": "David", "score": 93},
    {"nom": "Bob",   "score": 91},
    {"nom": "Hugo",  "score": 89},
    {"nom": "Alice", "score": 88},
    {"nom": "Frank", "score": 87},
    {"nom": "Grace", "score": 85},
    {"nom": "Clara", "score": 84},
    {"nom": "Emma",  "score": 79},
]

# A. Score CUMULÉ RECURSIF

# on va calcule la somme des k meilleurs score un par un par cette fonction
def score_cumule(liste, K):
    if K == 0:
        return 0
    
    # le score actuel + somme des scores precedents

    resultat = liste[K-1]['score'] + score_cumule(liste, K-1)

    print(f"score_cumule(joueurs, {K}) = {resultat} pts ({liste[K-1]['nom']})")
    return resultat


# B. Fibonacci des scores
# on va utilisé les scores de David (93) et bob (91) comme points de depart
# fib(0) = 93, fib(1) = 91

def fib_naif(n):
    if n == 0: return 93
    if n == 1: return 91
    return fib_naif(n-1) + fib_naif(n-2)

# utiliser une dictionnaire

memoire = {}
def fib_memo(n):
    if n in memoire:
        return memoire[n]
    if n == 0: return 93
    if n == 1: return 91

    # on enregistre les calcules dans la memoire
    memoire[n] = fib_memo(n-1) + fib_memo(n-2)
    return memoire[n]

# EXECUTION ET MESURE DU TEMPS

if __name__ == "__main__":
    print("\n" + "-"*40)
    print("SCORE CUMULÉ RÉCURSIF")
    print("-"*40)
    # calcule pour les 3 meilleurs joueurs
    score_cumule(joueurs_tries, 3)

    print("\n" + "-"*40)
    print("FIBONACCI (n=35)")
    print("-"*40)

    # Test de Naive
    debut = time.perf_counter()
    res_naif = fib_naif(35)
    fin = time.perf_counter()
    print(f"FIB_NAIF(35) = {res_naif} | temps : {fin - debut:.4f} s")


    # test Memoisée
    debut = time.perf_counter()
    res_memo = fib_memo(35)
    fin = time.perf_counter()
    print(f"FIB_MEMO(35) = {res_memo} | temps : {fin - debut:.6f} s")
    print("-"*40)