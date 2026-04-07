# données du problème
joueurs = [
{"nom": "Alice", "score": 88, "salaire": 1200, "poids": 72},
{"nom": "Bob",   "score": 91, "salaire": 1800, "poids": 85},
{"nom": "Clara", "score": 84, "salaire": 950,  "poids": 68},
{"nom": "David", "score": 93, "salaire": 2100, "poids": 90},
{"nom": "Emma",  "score": 79, "salaire": 800,  "poids": 65},
{"nom": "Frank", "score": 87, "salaire": 2400, "poids": 95},
{"nom": "Grace", "score": 85, "salaire": 1050, "poids": 70},
{"nom": "Hugo",  "score": 89, "salaire": 1600, "poids": 80},
]


# Meilleur score, strategie 1

def glouton_score():
    #trier le score par ordre decroissant
    joueurs_tries = sorted(joueurs, key=lambda x: x['score'], reverse=True)
    equipe_A = []
    equipe_B = []
    
    #compteur pour surveiller les limites
    budget_total = 0
    poids_A = 0
    poids_B = 0


    for j in joueurs_tries:
        # on rempli l'equipe A d'abord (max 3)
        if len(equipe_A) < 3:
            # On verifie les limites
            if (budget_total + j['salaire'] <= 8500) and (poids_A + j['poids'] <= 250):
                equipe_A.append(j)
                budget_total += j['salaire']
                poids_A += j['poids']


        # on tente d'ajouter l'equipe B
        elif len(equipe_B) < 3:
            # on va verifier si les joueurs n'est pas deja dans l'equipe A
            if j not in equipe_A:
                # on verifie les limites
                if (budget_total + j['salaire'] <= 8500) and (poids_B + j['poids'] <= 250):
                    equipe_B.append(j)
                    budget_total += j['salaire']
                    poids_B += j['poids']

    total_points = sum(j['score'] for j in equipe_A + equipe_B)
    print("Glouton Score total :", total_points)

    return total_points, budget_total


# Ratio score/Salaire, strategie 2

def glouton_ratio_salaire():
    #Trier par le meilleur rapport qualité ou le prix
    joueurs_tries = sorted(joueurs, key=lambda x: x['score']/x['salaire'], reverse=True)
    equipe_A = []
    equipe_B = []
    budget_total = 0
    poids_A = 0
    poids_B = 0

    for j in joueurs_tries:
        # l'equipe A
        if len(equipe_A) < 3:
            # on verifie budget global et poids de l'equipe A
            if (budget_total + j['salaire'] <= 8500) and (poids_A + j['poids'] <= 250):
                equipe_A.append(j)
                budget_total += j['salaire']
                poids_A += j['poids']

            # on verifie l'equipe B    
        elif len(equipe_B) < 3:
            # on verifie le budget global et poid de l'equipe B
            if (budget_total + j['salaire'] <= 8500) and (poids_B + j['poids'] <= 250):
                equipe_B.append(j)
                budget_total += j['salaire']
                poids_B += j['poids']


    score = sum(j['score'] for j in equipe_A + equipe_B)
    print("Glouton Ratio Salaire total :", score, "pts")
    return score, budget_total


# Ratio score/Poids strategie 3

def glouton_ratio_poids():
    joueurs_tries = sorted(joueurs, key=lambda x: x['score'] /x['poids'], reverse=True)
    equipe_A = []
    equipe_B = []
    budget_total = 0
    poids_A = 0
    poids_B = 0

    for j in joueurs_tries:
        if len(equipe_A) < 3:
            if (budget_total + j['salaire'] <= 8500) and (poids_B + j['poids'] <= 250):
                equipe_A.append(j)
                budget_total += j['salaire']
                poids_A += j['poids']
        elif len(equipe_B) < 3:
            if (budget_total + j['salaire'] <= 8500) and (poids_B + j['poids'] <= 250):
                equipe_B.append(j)
                budget_total += j['salaire']
                poids_B += j['poids']


    score = sum(j['score'] for j in equipe_A + equipe_A)
    print("Glouton Ratoio POids total :", score, "pts")
    return score, budget_total


# on appel les fonctions pour voir les resultats

# recuperer les resultats
s1, b1 = glouton_score()
s2, b2 = glouton_ratio_salaire()
s3, b3 = glouton_ratio_poids()

# valeur de Pulp
score_optimal = 524
budget_optimal = 8450

# Affichage
print("\n" + "="*85)
print(f"{'STRATEGIE':<25} | {'score':<10} | {'BUDGET':<10} | {'ECART VS OPTIMAL'}")
print("-" * 85)


# calcul des ecarts

def afficher_ligne(nom, s, b):
    diff = s - score_optimal
    pourcent = (diff / score_optimal) * 100
    print(f"{nom:<25} | {s:<10} | {b:<10} | {diff} pts({pourcent:1f}%)")

afficher_ligne("1. Meilleur Score", s1, b1)
afficher_ligne("2. Ratio SCore/Salaire", s2, b2)
afficher_ligne("3. Ratio Score/Poids", s3, b3)
print(f"{'4. PuLP (Optimal)':<25} | {score_optimal:<10} | {budget_optimal:<10} | ---")
print("-"*85)

