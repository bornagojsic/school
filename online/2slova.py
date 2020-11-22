def main():
	s = input('Upisi string: ').lower()
	a = input('Upisi prvo slovo: ')
	b = input('Upisi drugo slovo: ')
	if all([len(a) == 1, len(b) == 1, s]):
		print(f"Slova \"{a}\" i \"{b}\" pojavljuju se jednako puta.") if s.count(a) == s.count(b) else print(f"Slovo \"{a if s.count(a) > s.count(b) else b}\" se pojavljuje vise puta.")


if __name__ == '__main__':
	main()