# Engineering_4_Notebook

<details><summary>Calculator</summary>
  
### Calculator

### Assignment Description

In this assignment we were tasked with creating a program that can succsessfully solve simple math problems like a calculator.  In fact, I'm pretty sure I created a calculator. 

### Evidence 

```python3
 def doMath(a,b,c):
   #do the actual calc here and return
    if c == 1:
        return str(a + b)
    if c == 2:
        return str(a - b)
    if c == 3:
        return str(a * b)
    if c == 4:
        return str(a / b)
    if c == 5: 
        return str(a % b)
        
     
     

a = int(input("type first"))
b = int(input("type second"))
        
        
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))

```

### Reflection

This assignment gave me a rude awakening that I probably should have payed more attention in online schooling last year, relearning basic things such as what a function is comes to mind (a function being a "named section of code that performs a specific task").  In hindsight it was rather easy as the "DoMath" function was doing most of the heavy lifting. however, DoMath was both our geatest asset, but our greatest hinderance, as the catch of the assignment was to create the entire calculator using ONLY the DoMath function.
  
</details>


<details><summary>Quadratic Calculator</summary>
  
### Quadratic Calculator

### Assignment Description

in this assingment we were tasked with creating a quadratic calculator in python.  the user types in A,B, and C and the calculator finds all the possible answers.

### Evidence 

```python3
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
```

### Reflection

similar to the first calculator assignment, I had to go through a small period of grieving for my short attention span in online school, and finally admit to myself that im not only python stunted, but as well as mathmatically stunted.  In order for me to successfully do this assignment I had to essentually relearn what "quadratic" means.  my advice for this assignment:  ASK QUESTIONS!  if you dont understand something get some clarity on the matter.

  </details>
  
  
