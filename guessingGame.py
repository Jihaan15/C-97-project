import random

rand=random.randint(1,9)

chances=0

while chances<5:
   guess=int(input('Enter your number : '))    

   if guess==rand:

       print("CONGRATULATIONS YOU WON !!!")


   elif guess<rand:
       print("YOUR NUMBER IS LOW")

   if guess>rand:
       print("YOUR NUMBER IS HIGH")  

   chances+=1      
if not chances<5:
    print("YOU LOSE, THE NUMBER IS : ",rand)   

