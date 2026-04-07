import pulp

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

def optimisation_equipe():
    # 1. je vais creer un conteneur du probleme pour maximiser le score
    mon_probleme = pulp.LpProblem("Selection_Equipes", pulp.LpMaximize)

    # 2. créer les variables 0 ou 1 pour chaque joueur dans chaque equipe
    choix_A = []
    choix_B = []
    for j in joueurs:
        nom_joueur = j['nom']
        var_A = pulp.LpVariable("A_" + nom_joueur, cat='Binary')
        var_B = pulp.LpVariable("B_" + nom_joueur, cat='Binary')
        choix_A.append(var_A)
        choix_B.append(var_B)

    # 3. La somme des scores
    score_total = 0
    for i in range(len(joueurs)):
        score_total += joueurs[i]['score'] * (choix_A[i] + choix_B[i])
        mon_probleme += score_total

    # 4. Contraite: nombre de joueur par equipe
    mon_probleme += pulp.lpSum(choix_A) == 3
    mon_probleme += pulp.lpSum(choix_B) == 3

    
    # 5. contrainte: Faire en sorte qu'un joueur ne peut pas etre dans deux equipes
    for i in range(len(joueurs)):
        mon_probleme += choix_A[i] + choix_B[i] <= 1
    
    
    # 5. Contrainte: Le poid max par equipe (250kg)
    poids_A = 0
    poids_B = 0
    for i in range(len(joueurs)):
        poids_A += joueurs[i]['poids'] * choix_A[i]
        poids_B += joueurs[i]['poids'] * choix_B[i]
    mon_probleme += poids_A <= 250
    mon_probleme += poids_B <= 250


    # 6. Contrainte: respecter le budget maximal (8500$)
    budget_total = 0
    for i in range(len(joueurs)):
        budget_total += joueurs[i]['salaire'] * (choix_A[i] + choix_B[i])
        
    # 7. on ajoute la limite du budget en dehors du "for"
    mon_probleme += budget_total <= 8500

    # 8. la resolution
    mon_probleme.solve(pulp.PULP_CBC_CMD(msg=0))


    # 9. o va additionne les salaires des joueurs
    argent_depense = 0
    for i in range(len(joueurs)):
        # on prend la valeur de 0 ou 1 donne par pulp.value(x) trouve par l'ordinateur
        if pulp.value(choix_A[i]) == 1 or pulp.value(choix_B[i]) == 1:
            argent_depense += joueurs[i]['salaire']


    # 10. l'affichage simple
    print("-" * 40)
    print("SCore optimal trouvé :", pulp.value(mon_probleme.objective))
    print("Budget total utilisé :", argent_depense, "$")

    print("-" * 40)
    # 9. Garder ces valeurs pour le tableau pour comparer
    return pulp.value(mon_probleme.objective), argent_depense

optimisation_equipe()