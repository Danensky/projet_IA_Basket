import matplotlib.pyplot as plt

# 1. Graphique des Scores
methodes = ['Glouton Score', 'Ratio $/pts', 'PuLP (Optimal)']
scores = [443, 516, 524]

plt.figure(figsize=(8, 5))
plt.bar(methodes, scores, color=['salmon', 'skyblue', 'green'])
plt.axhline(y=524, color='red', linestyle="--", label="Optimal (524)")
plt.title("Comparaison des scores totaux")
plt.ylabel("Points")
plt.legend()
plt.savefig("score_comparaison.png")
plt.show

# 2. Graphique Fibonacci 
n = [10, 20, 30, 35]
# temps approximité
temps_naif = [0.001, 0.05, 1.2, 5.0]
temps_memo = [0.0001, 0.0001, 0.001, 0.0001]


plt.figure(figsize=(8, 5))
plt.plot(n, temps_naif, 'r-o', label="Naif (très lent)")
plt.plot(n, temps_memo, 'b-o', label="Mémoisé (instantané)")
plt.yscale('log')
plt.title("Temps de calcul Fibonacci (Echelle log)")
plt.xlabel("Valeur de n")
plt.ylabel("Temps (secondes)")
plt.legend()
plt.savefig("fibonacci_time.png")
plt.show()