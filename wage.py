hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the Rate:")
x = float(rate)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)
