def main():
	## broj redaka
	n = 2
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(n)]
	d = t[0][0] * t[1][1] - t[0][1] * t[1][0]
	print(f"Determinanta je {d}")


if __name__ == '__main__':
	main()