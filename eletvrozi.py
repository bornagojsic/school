def main():
	s = input('Upisi string: ')
	if s:
		print(s[:(n := len(s) // 2)][::-1] + s[n] + s[n + 1:][::-1] if len(s) % 2 else s[:n][::-1] + s[n:][::-1])


if __name__ == '__main__':
	main()