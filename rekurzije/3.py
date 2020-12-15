##          2 - f(x-3) - 3,  x > 6
##  f(x) =  f(x+2) + 1    ,  4 < x <= 6
##          x + 4         ,  x <= 4

##          -(f(x-3) + 1),  x > 6
##  f(x) =  f(x+2) + 1   ,  4 < x <= 6
##          x + 4        ,  x <= 4

##  f(12) = -( f(9) + 1 )
##        = -( -( f(6) + 1 ) + 1 )
##        = -( -( ( f(8) + 1 ) + 1 ) + 1)
##        = -( -( ( -( f(5) + 1 ) + 1 ) + 1 ) + 1)
##        = -( -( ( -( ( f(7) + 1) + 1 ) + 1 ) + 1 ) + 1)
##        = -( -( ( -( ( -( f(4) + 1 ) + 1) + 1 ) + 1 ) + 1 ) + 1)
##        = -( -( ( -( ( -( 8 + 1 ) + 1) + 1 ) + 1 ) + 1 ) + 1)
##        = -( -( ( -( ( -9 + 1) + 1 ) + 1 ) + 1 ) + 1)
##        = -( -( ( -( -8 + 1 ) + 1 ) + 1 ) + 1)
##        = -( -( ( 7 + 1 ) + 1 ) + 1)
##        = -( -( 8 + 1 ) + 1)
##        = -( -9 + 1)
##        = -( -8 )
##        = 8

def f(x):
	if x > 6:
		return -(f(x-3) + 1)
	elif x <= 4:
		return x + 4
	return f(x + 2) + 1

print(f"f(12) = {f(12)}")

print(f"f(x) = {f(int(input('Upiši x: ')))}")
