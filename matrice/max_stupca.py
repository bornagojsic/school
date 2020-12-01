def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak 1. matrice: ").split())) for i in range(r)]
	for i in range(s):
		m = t[0][i]
		for j in range(r):
			m = t[j][i] if t[j][i] > m else m
		print(f"Najveći element {i + 1}. stupca je {m}.")


if __name__ == '__main__':
	main()