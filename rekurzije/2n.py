def dva_na_n(n):
	if n == 0:
		return 1
	elif n > 0:
		return 2 * dva_na_n(n-1)
	else:
		return 1/2 * dva_na_n(n+1)


def main():
	print(dva_na_n(int(input(":"))))

if __name__ == '__main__':
	main()