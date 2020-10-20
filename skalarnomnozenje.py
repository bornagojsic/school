def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(r)]
	print("Ispis matrice:")
	[print(r) for r in t]
	n = int(input("Upisi broj s kojim zelis pomnoziti ovu matricu: "))
	t2 = [[n * t[i][j] for j in range(len(t[0]))] for i in range(len(t))] 
	print("Ispis pomnozene matrice:")
	[print(r) for r in t2]



if __name__ == '__main__':
	main()