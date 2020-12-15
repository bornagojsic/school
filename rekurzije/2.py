##            f(x,y) - 1    , x < y
##  f(x,y) =  f(x-2,y+1) + 2, x > y
##            (x+y) / 2     , x = y

##  f(8,14) = f(8,14) - 1
##  RecursionError: maximum recursion depth exceeded in comparison

def f(x,y):
	if x == y:
		return (x+y)/2
	elif x > y:
		return f(x-2,y+1) + 2
	return f(x,y) - 1

print(f"f(8,14) = {f(8,14)}")

print(f"f(x,y) = {f(int(input('Upiši x: ')), int(input('Upiši y: ')))}")