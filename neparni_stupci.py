def main():
	## broj redaka
	r = int(input("Upisi broj redaka: "))
	## broj stupaca
	s = int(input("Upisi broj stupaca: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(r)]
	print(f"Zbroj brojeva u neparnim stupcima je {sum([t[i][j] for i in range(r) for j in range(s) if not j % 2])}.")


if __name__ == '__main__':
	main()