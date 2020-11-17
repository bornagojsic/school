def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(r)]
	[print(f"{i + 1}. stupac, {j + 1}. redak: {t[i][j]}") for i in range(r) for j in range(s) if not (c := t[i][j]) % 2 and c > 5]
	print(f"Zbroj neparnih brojeva je {sum([t[i][j] for i in range(r) for j in range(s) if t[i][j] % 2])}.")


if __name__ == '__main__':
	main()