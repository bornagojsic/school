def f( N, S="" ):
	if N == 0:
		print(S)
	else:
		for o in '0 1 2 3 4 5 6 7'.split():
			f(N-1, S+o)

f(3)