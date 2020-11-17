def zbroj(n):
	if n == 0:
		return 0
	elif n > 0:
		return n + zbroj(n-1)
	else:
		return n + zbroj(n+1)


def main():
	print(zbroj(int(input(":"))))

if __name__ == '__main__':
	main()