def main():
	n = len(s := input('Upisi string: ')) // 2
	print(s[:n][::-1] + s[n] + s[n + 1:][::-1] if len(s) % 2 else s[:n][::-1] + s[n:][::-1])


if __name__ == '__main__':
	main()