def main():
	## broj redaka
	n = int(input("Upisi dimenziju matrice: "))
	## tablica
	t = [list(map(int, input(f"Upisi {i + 1}. redak: ").split())) for i in range(n)]
	d = 0
	b = 0
	print("")
	for i in range(n):
		k = 1
		for j in range(n):
			k *= t[j][(i + j) % n]
			print(k,j % n, (i + j) % n)
		d += k
	for i in range(n):
		k = 1
		for j in range(n):
			k *= t[n - j - 1][(i + j) % n]
			print(k,j % n, (i + j) % n)
		d -= k

	print(f"Determinanta je {d}.")


if __name__ == '__main__':
	main()

##
## [a00 a01 a02] a00 a01
## [a10 a11 a12] a10
## [a20 a21 a22] a20 a21
##

## zasad radi samo za 3 dimenzionalnu matricu