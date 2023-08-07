import math

def second_degree_eq(a,b,c):
    delta = b**2 - 4*a*c

    if delta > 0:
        # Two real and distinct solutions
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("first root is: ",x1)
        print("second root is: ",x2)
    elif delta == 0:
        # One real solution
        x = -b/(2*a)
        print("the only root is: ",x)
    else:
        print("No real roots exist")
        
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

second_degree_eq(a, b, c)


