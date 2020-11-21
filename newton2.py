import math

tolerance=0.00001
approximation=1.0
x = float(input("Enter a positive number: "))

def newton(number,approximation):
    approximation=(approximation+number/approximation)/2
    difference_value =abs(number-approximation**2)
    
    if difference_value<= tolerance:
        return approximation
    else:
        return newton(number,approximation)
#Output the result
print("The programs estimate of the square root of ", newton(x, approximation))
print("Python's estimate: ", math.sqrt(x))
