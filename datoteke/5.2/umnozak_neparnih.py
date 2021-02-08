from functools import reduce

with open("brojevi.txt", 'r') as f:
	brojevi = [list(map(int, line.split())) for line in f]

umnosci = [reduce(lambda x,y: x*y if x % 2 and y % 2 else x*(x%2) + y*(y%2), broj) for broj in brojevi]

umnozak = reduce(lambda x,y: x*y if x % 2 and y % 2 else x*(x%2) + y*(y%2), umnosci)

with open("umnozak_neparnih.txt", 'w') as f:
	f.write(str(umnozak))