def main():
	## broj redaka
	n = int(input("Upisi broj n: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(n)]
	print(f"Trag matrice je {sum([t[i][i] for i in range(n)])}")

if __name__ == '__main__':
	main()