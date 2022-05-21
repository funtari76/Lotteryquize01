import random
import figlet 
from pyfiglet import Figlet
f = Figlet(font ='5lineoblique')
print(f.renderText('Good!'))

def imagine (x):# create a var imagine and then pass it a random number 
    random_number = random.randint(1, x)
    imagine = 0
    # User input
    
    user = input("*****Please Enter You Name To Begin ->> ")
    
    print("Well Done And Welcome", user, "This is a Lottery Guessing Lucky Numbers Game")
    print("---------------------------------")
    print("#########****Millions****########")
    print("##-----------------------------##")
    print("##-----------------------------##")
    while imagine != random_number: # Create a while condition
        imagine = int(input(f'Guess any number between 1 and {x}: '))
       # data_str =data_str.split(",")#chech how if needed???
        if imagine < random_number:
           print('Eeeh ^o^! Sorry :(, try again. The number was Too low.')
        elif imagine > random_number:
           print('Eeeh ^o^! Sorry :(, try again. The number was Too high.')

    print(f'Perfect! Well Done, You imagined the number {random_number} Exactly')    
    
imagine(20)  