def determinanta(A, total=0):
	indices = list(range(len(A)))

	if len(A) == 2 and len(A[0]) == 2:
		return A[0][0] * A[1][1] - A[1][0] * A[0][1]
 
	for fc in indices:
		As = copy_matrix(A)
		As = As[1:]
		height = len(As)

		for i in range(height): 
			As[i] = As[i][0:fc] + As[i][fc+1:] 
 
		sign = (-1) ** (fc % 2) 
		sub_det = determinanta(As)
		total += sign * A[0][fc] * sub_det 

	return total


def invert(A, tol=None):
	if type(A) == Matrica and A.m == A.n and A.d != 0:
		n = A.n
		AM = [[A.v[i][j] for j in range(n)] for i in range(n)]
		I = Matrica(n, n, [[1 if i == j else 0 for j in range(n)] for i in range(n)])
		IM = Matrica(n, n, [[1 if i == j else 0 for j in range(n)] for i in range(n)])

		# Section 3: Perform row operations
		indices = list(range(n)) # to allow flexible row referencing ***
		for fd in range(n): # fd stands for focus diagonal
			fdScaler = 1.0 / AM[fd][fd]
			# FIRST: scale fd row with fd inverse. 
			for j in range(n): # Use j to indicate column looping.
				AM[fd][j] *= fdScaler
				IM.v[fd][j] *= fdScaler
			# SECOND: operate on all rows except fd row as follows:
			for i in indices[0:fd] + indices[fd+1:]: 
				# *** skip row with fd in it.
				crScaler = AM[i][fd] # cr stands for "current row".
				for j in range(n): 
					# cr - crScaler * fdRow, but one element at a time.
					AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
					IM.v[i][j] = IM.v[i][j] - crScaler * IM.v[fd][j]
	 
		# # Section 4: Make sure IM is an inverse of A with specified tolerance
		# if check_matrix_equality(I,matrix_multiply(A,IM),tol):
		return IM
		# else:
		# 	raise ArithmeticError("Matrix inverse out of tolerance.")


class Matrica():
	def __init__(self, m, n, v):
		super(Matrica, self).__init__()
		self.m = m
		self.n = n if n else m
		self.v = v
		self.d = determinanta(self.v)

	def print(self):
		[print(redak) for redak in self.v]
	
	def plus(self, other):
		if type(other) == Matrica and self.m == other.m and self.n == other.n:
			self.v = [[self.v[i][j] + other.v[i][j] for j in range(self.n)] for i in range(self.m)]

	def puta(self, other):
		if type(other) == float or type(other) == int:
			self.v = [[self.v[i][j] * other for j in range(self.n)] for i in range(self.m)]
		elif type(other) == Matrica and self.n == other.m:
			v = []
			for i in range(self.m): 
				v.append([])
				for j in range(other.n): 
					v[i].append(0)
					for k in range(self.n):
						v[i][j] += self.v[i][k] * other.v[k][j]
			self.n = other.n
			self.v = v

	def minus(self, other):
		self.plus(self, other.puta(-1))

	def podijeljeno(self, other):
		if type(other) == float or type(other) == int:
			self.v = [[self.v[i][j] / other for j in range(self.n)] for i in range(self.m)]
		elif type(other) == Matrica and self.n == other.m:
			try:
				self.puta(invert(other))
			except:
				pass


def plus(A, B):
	if type(A) == Matrica and type(B) == Matrica and A.m == B.m and A.n == B.n:
		return Matrica(A.m, A.n, [[A.v[i][j] + B.v[i][j] for j in range(A.n)] for i in range(A.m)])


def puta(A, B):
	if type(A) == Matrica and type(B) == Matrica:
		v = []
		for i in range(A.m): 
			v.append([])
			for j in range(B.n): 
				v[i].append(0)
				for k in range(A.n):
					v[i][j] += A.v[i][k] * B.v[k][j]
		return Matrica(A.m, B.n, v)
	elif type(A) == Matrica and type(B) in [float, int]:
		return Matrica(A.m, A.n, [[A.v[i][j] * B for j in range(A.n)] for i in range(A.m)])


def podijeljeno(A, B):
	if type(A) == Matrica and type(B) == Matrica:
		try:
			puta(A, invert(B))
		except:
			pass
	elif type(A) == Matrica and type(B) in [int, float]:
			puta(A, 1/B)

A = Matrica(2, 2, [[1,2],[3,4]])
#A = Matrica((m := int(input("Upiši broj redaka: "))), (n := int(input("Upiši broj stupaca: "))), [[int(input(f"Upiši {i + 1}. redak, {j + 1}. stupac matrice: ")) for j in range(n)] for i in range(m)])