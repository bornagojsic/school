n = int(input("Upisi n: "))

l = [int(input(f"Upisi {i +1 }. broj: ")) for i in range(n)]

with open("podaci.txt", 'w') as f:
	f.write(' '.join(list(map(str, l))))

with open("podaci.txt", 'r') as f:
	l = list(map(int, f.read().split()))

prvi = min(filter(lambda x: x > 0, l))
drugi = list(filter(lambda x: x < 0, l))
drugi.sort()
treci = sum(list(map(lambda x: not x % 5, list(filter(lambda x: x > 0, l)))))

with open("rezultati.txt", 'w') as f:
	f.write(f"{prvi}\n{' '.join(list(map(str, drugi)))}\n{treci}")