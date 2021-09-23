import math
a=float(input("Enter the coefficient a ")) # type in coefficient a
b=float(input("Enter the coefficient b ")) # type in coefficient b
c=float(input("Enter the coefficient c ")) # type in coefficient c
d=b*b-4*a*c;

if d>0:
 r1 = (-b + math.sqrt(d)) / (2 * a) # show answer
 r2 = (-b - math.sqrt(d)) / (2 * a)
 print("Roots are real and unequal ",r1, " and ",r2) # if roots are real and unequal
elif d==0:
 r1=-b/(2*a)
 print("Roots are real and equal ",r1) # if roots are real
else:
 print("No real roots ") # if there's no roots
 