n = int(input("Upisi n: "))

l = [int(input(f"Upisi {i +1 }. broj: ")) for i in range(n)]

with open("ulaz.txt", 'w') as f:
	f.write(' '.join(list(map(str, l))))

prvi = sum(filter(lambda x: not x % 2, l))
drugi = reduce(lambda x,y: x*y, filter(lambda x: -10 <= x <= 10, l))
treci = sum(pozitivni := list(filter(lambda x: x > 0, l)))/len(pozitivni)

with open("izlaz.txt", 'w') as f:
	f.write(f"{prvi}\n{drugi}\n{treci}")