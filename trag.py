def main():
	## broj redaka
	n = int(input("Upisi broj n: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(n)]
	print(f"Trag matrice je {sum([t[i][j] for i in range(n) for j in range(n) if i == j])}")

if __name__ == '__main__':
	main()