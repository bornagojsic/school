def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(r)]
	print("Ispis matrice:")
	[print(r) for r in t]
	t2 = [[t[j][i] for j in range(len(t))] for i in range(len(t[0]))] 
	print("Ispis transponirane matrice:")
	[print(r) for r in t2]
	print(f"Matrica {'ni' if not t == t2 else ''}je simetrična.")



if __name__ == '__main__':
	main()