## print 3 min i 2 najveci broj
def main():
	n = int(input("Upisi duljinu liste: "))

	l = [int(input("Upisi broj: ")) for _ in range(n)]

	l.sort()

	print(f"3 najmanja broja iz liste su: {l[0]}, {l[1]} i {l[2]}. 2. najveci broj iz liste je {l[n-2]}")


if __name__ == "__main__":
	main()