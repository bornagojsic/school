def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(r)]
	print("Ispis matrice:")
	[print(r) for r in t]
	for i in range(r):
		for j in range(s):
			if t[i][j] != -t[j][i]:
				print("Matrica nije antisimetrična.")
				quit()
	print("Matrica je antisimetrična.")


if __name__ == '__main__':
	main()