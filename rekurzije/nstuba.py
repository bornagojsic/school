## n - broj stuba
## m - max broj skokova
## s - string
def f( N, M, S="" ):
	if N == 0:
		print(S)
	elif 1 <= N <= M:
		for i in range(1,N + 1):
			f(N-i, M, S+str(i))
	else:
		for j in range(1,M + 1):
			f(N-j, M, S+str(j))


N = int( input( 'UPISI N: ' ) )
M = int( input( 'UPISI M: ' ) )
print("REZULTAT:")
f(N, M)