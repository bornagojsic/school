##          f(x-2) + 1    ,  x > 8
##  f(x) =  2 - f(x-1) - 2,  5 <= x <= 8
##          x - 1         ,  x < 5

##          f(x-2) + 1,  x > 8
##  f(x) =  - f(x-1)  ,  5 <= x <= 8
##          x - 1     ,  x < 5

##  f(f(f(13))) = f( f( f(11) + 1 ) ) 
##              = f( f( f(9) + 2 ) ) 
##              = f( f( f(7) + 3 ) ) 
##              = f( f( -(f(6)) + 3 ) ) 
##              = f( f( f(5) + 3 ) ) 
##              = f( f( -(f(4)) + 3 ) ) 
##              = f( f( -3 + 3) ) 
##              = f( f(0) )
##              = f( 0 - 1 )
##              = f( -1 )
##              = -1 - 1
##              = -2


def f(x):
	if x > 8:
		return f(x-2) + 1
	elif x < 5:
		return x - 1
	return -f(x-1)

print(f"f(f(f(13))) = {f(f(f(13)))}")

print(f"f(x) = {f(int(input('Upiši x: ')))}")
