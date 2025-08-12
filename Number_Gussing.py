import random

print('Hello, World! Welcome to the number guessing Game.\nYou will get 7 chances to guess the number.')
print("Instruction:-\n1-First choice any one number must be an integer.\n2-Choose a second number which must be greater than first number it should be an integer. ")
print("< Now the wait is over,Let's start!")

low =int(input('Enter first choice='))
high =int(input('Enter last choice='))

print(f'You have 7 chances to guess the right number between {low} and {high}.')

num =random.randint(low,high)
ch = 7 #Number of chances to guess the number
gc = 0 

while gc < ch :
    gc += 1
    uguess =int(input("Enter your Guess="))

    if uguess == num:
       print(f"Correct! The number is {num}.You gussed it in {gc} attempts.")
       break
    
    elif gc >= ch and uguess!= num:
        print(f'Sorry! The number is {num}.')
        
    elif uguess > num:
        print('To high ! Try a lower number.')
        
    elif uguess < num:
        print('To low! Try a higher number.')
        
        
print("Thank you, Visit again!")