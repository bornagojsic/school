def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(r)]
	print("Ispis matrice:")
	[print(r) for r in t]
	b = False
	for i in range(r):
		if b:
			break
		for j in range(s):
			if t[i][j] != 0 and i != j:
				b = True
				break
	print(f"Matrica {'ni' if b else ''}je dijagonalna.")



if __name__ == '__main__':
	main()