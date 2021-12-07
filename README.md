# Engineering_4_Notebook

 <details><summary>Python</summary>

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
  
  <details><summary>Hangman(MSP)</summary>
  
  I TOTALLY did this assignment (SARCASM).  this project was pretty complicated, which is why I TOTALLY did it (SARCASM).  We had to make a game of hangman entirly localized within python,  this had many hurdles I didnt cross,  making the hangman, analizing every character, and displaying the hangman, word, and missed charcters to name a few.
 the program should work as follows;  the game diplays "player 1, enter your word."  player one enters their word, and then proptly leaves as they dont do anything else.  THE PROGRAM MUST DELETE THE WORD BEFORE PLAYER 2 CAN SEE IT!  than the program shows the following graphic.
  
  ![image](https://user-images.githubusercontent.com/57536671/139086477-047ff8b4-bbe0-43aa-aecc-f305f6a547a0.png)
  
  if player 2 guesses a wrong charecter than an additinal body part should appear on jeremy (his name) and if are a spicy boy, than a list of missed charcter should appear. like so:
  
  ![image](https://user-images.githubusercontent.com/57536671/139086513-02f2a4e8-f0c8-4cac-9e4e-319e47dafeb7.png)

  
  the miller man has graciously given me these images
  </details>
  <details><summary>RPi GPIO Pin introduction</summary>
   
   In this assignment we were tasked with making two LED lights switch on and off after eachother.  We had to write and run the code entirly within a raspberry pi.  I went through about three PI's desperatley trying to get github, Python, and the T-cobbler to work.  Normally i struggle the most with getting the code itself to work, but the simple function of this assignment made it so i didnt have to spend more than half an hour on it.  the challenge most certainly lay in getting the hardware to work.
   
   ```python3
import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM) #this sets my pin numbering scheme as the BCM numbering scheme
# Variable for the GPIO pin number  
LED_pin_Red = 20
LED_pin_Green = 21
# Tell the Pi we are using the breakout board pin numbering
GPIO.setmode(GPIO.BCM)
 
# Set up the GPIO pin for output
GPIO.setup(LED_pin_Red, GPIO.OUT)
GPIO.setup(LED_pin_Green, GPIO.OUT)
# Loop to blink our led
while True:
        GPIO.output(LED_pin_Red, GPIO.HIGH)  
        GPIO.output(LED_pin_Green, GPIO.LOW) 
        sleep(.5)
        GPIO.output(LED_pin_Red, GPIO.LOW)
        GPIO.output(LED_pin_Green, GPIO.HIGH)
        sleep(.5)
  ```
   
   </details>
   </details>
   
  <details><summary>CAD</summary>
  
  <details><summary>Skamtbord</summary>
  
  In this assignment we were tasked with creating a stakeboard from the instructions of a virtual dr. shields.  I never felt too challenged with this skateboard as we had really in depth intructiuons from our cyberghost friend. it was rather relaxing, a similar experience to building a lego set. 
  
  ![image](https://user-images.githubusercontent.com/57536671/139074585-23d387d7-4d63-4781-bdf5-32b7a2788c5e.png)
  
  The deck was a pretty easy section of this build.  the process of bending the stairboard consited of splitting a face into two and then using the "move face" function was very interesting, i can definitly see myself using that technique again.
  
![image](https://user-images.githubusercontent.com/57536671/139075293-0b2add71-814f-4dfe-8459-2f2e1cdc0550.png)

  the trucks were the most fun to make.  the process of entirely remodeling the trucks was pretty fun.
  
![image](https://user-images.githubusercontent.com/57536671/139075344-a6c4f639-0d57-4cf3-95e9-8cd14174a958.png)
  
  by the time I got to the wheels I started to get a little board, so I went on a journey making my own skate company named "indestructable" and wanted to put the name on the wheels.  the issue I ran into was fgetting the text to be in a circular pattern, so I learned how to import a text editing tool from the onshape public library called "surface text." I had never realized before doing this how usful these tools that other people made in onshape can be, I really felt that my skill grew after making indestructable. 

</details>
<details><summary>Lemgo</summary>
 
 This assignment was far from hard, but it was certainly tedious, as i type this i feel my braincelss disintegrating.  i learned about configurations, which is something i wish i knew for the swing arm assignment.  the ability to create multiple variants of one part is a powerful tool that im certainly going to use again.
![image](https://user-images.githubusercontent.com/57536671/141320017-63348ec0-3761-410c-a2e1-e55c6741cb44.png)
</details>
