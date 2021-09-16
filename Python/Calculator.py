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
