def a_na_n(a, n):
	if n == 0:
		return 1
	elif n > 0:
		return a * a_na_n(a, n-1)
	else:
		return 1/a * a_na_n(a, n+1)


def main():
	print(a_na_n(int(input("Upiši bazu: ")), int(input("Upiši potenciju: "))))

if __name__ == '__main__':
	main()