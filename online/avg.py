## sum(brojevi manji od avg())
def main():
	n = int(input("Upisi duljinu liste: "))

	l = [int(input("Upisi broj: ")) for _ in range(n)]

	l = [i for i in l if i < sum(l) / n]

	print(f"Zbroj brojeva manjih od prosjeka je {sum(l)}")


if __name__ == "__main__":
	main()