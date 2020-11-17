def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t1 = [list(map(int, input(f"Upisi {i + 1}. redak 1. matrice: ").split())) for i in range(r)]
	t2 = [list(map(int, input(f"Upisi {i + 1}. redak 2. matrice: ").split())) for i in range(r)]
	t3 = [[] for i in range(r)]
	for i in range(r):
		for j in range(s):
			t3[i].append(t2[i][j] + t1[i][j])
	print(f"Zbroj matrica je:")
	[print(r) for r in t3]


if __name__ == '__main__':
	main()