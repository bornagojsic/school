def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak 1. matrice: ").split())) for i in range(r)]
	for i in range(s):
		z = 0
		for j in range(r):
			z += t[j][i]
		print(f"Zbroj elemenata {i + 1}. stupca je {z}.")


if __name__ == '__main__':
	main()