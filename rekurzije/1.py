##              f(x-3) + 3,  x > 3
##	f(x) =  2x + 1    ,  x = 3   ==>  f(3) = 7
##              x^2 + 2   ,  x < 3

##  f(9) = f(6) + 3 = (f(3) + 3) + 3 = (7 + 3) + 3 = 10 + 3 = 13

def f(x):
	if x == 3:
		return 7
	elif x > 3:
		return f(x - 3) + 3
	return x**2 + 2

print(f"f(9) = {f(9)}")

print(f"f(x) = {f(int(input('Upiši x: ')))}")
