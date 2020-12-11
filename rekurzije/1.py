##          f(x-1) + 2 - f(x-2),  x > 5
##  f(x) =  2                  ,  x = 5
##          -2                 ,  x < 5

##  f(9) = f(8) + 2 - f(7) 
##       = (f(7) + 2 - f(6)) + 2 - f(7)
##       = 4 - f(6)
##       = 4 - (f(5) + 2 - f(4))
##       = 4 - (2 + 2 + 2)
##       = -2

def f(x):
	if x == 5:
		return 2
	elif x > 5:
		return f(x - 1) + 2 - f(x - 2)
	return -2

print(f"f(9) = {f(9)}")

print(f"f(x) = {f(int(input('Upiši x: ')))}")
