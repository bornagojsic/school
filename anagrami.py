def main():
	if (A := [letter for letter in input("Upisi prvu rijec: ")]) and (B := [letter for letter in input("Upisi drugu rijec: ")]):
		A.sort()
		B.sort()
		anagrami = (A == B)
	print(f"Rijeci {'ni' if not anagrami else ''}su anagrami.")


if __name__ == '__main__':
	main()