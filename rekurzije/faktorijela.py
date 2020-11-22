def faktorijela(n):
	if n == 0:
		return 1
	elif n > 0:
		return n * faktorijela(n-1)
	else:
		return None


def main():
	print(faktorijela(int(input(":"))))

if __name__ == '__main__':
	main()