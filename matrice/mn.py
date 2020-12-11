m = int(input("Upiši broj redova prve matrice: "))
p = int(input("Upiši broj stupaca prve matrice: "))
n = int(input("Upiši broj stupaca druge matrice: "))
t1 = [[] for _ in range(m)]
t2 = [[] for _ in range(p)]
[t1[i].append(int(input(f"Upiši {i + 1}. redak, {j + 1}. stupac 1. matrice: "))) for i in range(m) for j in range(p)]
[t2[i].append(int(input(f"Upiši {i + 1}. redak, {j + 1}. stupac 2. matrice: "))) for i in range(p) for j in range(n)]
t3 = [[0 for i in range(n)] for _ in range(m)]
for i in range(m):
	for j in range(n):
		for k in range(p):
			t3[i][j] += t1[i][k] * t2[k][j]
print("Umnožak ovih dviju matrica je: ")
[print(r) for r in t3]














