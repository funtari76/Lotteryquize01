
import random

# create a var imagine and then pass it a random number 

def imagine (x):
    random_number = random.randint(1, x)
    imagine = 0
    
# User input
    print('--------------------------------------------------')
    print('               -----------------                  ')
    print("Welcome to The Lottery Guessing Lucky Game" )
    print("This is a Lottery Guessing Lucky Numbers Game")
    print("All you have to do from here is choose any number" )
    print("                   GOOD LUCK!                     ")
    print('               -----------------                  ')
    print('--------------------------------------------------')
    print('                                                  ')
    user = input(">>>> Please Enter You Name To Begin ->> ")
    
    print("--------------------------------------------------")
    print("          Well Done And Welcome", user,            )
    print("--------------------------------------------------")
    print('                                                  ')
    print("################******Millions******##############")
    print("##----------------------------------------------##")
    print("##----------------------------------------------##")
    print("################******* START *******#############")
    print('                                                  ')
    print("###########                              #########")
    print("########                                    ######")
    print("######                                        ####")
    print("--------------------------------------------------")

# Create a while condition

    while imagine != random_number: 
        print("----------------------------------------------------")
        imagine = int(input(f'Guess any number between 1 and {x}: '))
   
        if imagine < random_number:
           print("--------------------------------------------------")
           print('               -----------------                  ')
           print('Eeeh ^o^! Sorry :(, try again. Number was Too low.')
           print('               -----------------                  ')
           print("--------------------------------------------------")
        elif imagine > random_number:
           print("--------------------------------------------------")
           print('               -----------------                  ')
           print('Eeeh ^o^! Sorry :(, try again. Number was Too high.')
           print('               -----------------                  ')
           print("--------------------------------------------------")

    print(f'Perfect! Well Done, You imagined the number {random_number} Exactly')
    print("------------------------------------------------------")
    print("------------------- Thank You!.... -------------------")    
    
imagine(20)  