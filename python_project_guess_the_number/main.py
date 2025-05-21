# Guess The Number Game From 1 - 10:

import random
# Importing random number to generate a random number for ai using randint:
ai = random.randint(1,10)
# Initial value of player to make condition true for while loop:
player = 0
# Attempts will increament untill correct answer is found!:
attempts = 0

# While Loop for repetative program like games etc:
while(player != ai):
    

    player = int(input("Guess the number: ")) #user input or you

    #Conditions:
    if player > ai: #if player entered largest number compare to ai then this block will execute:
        print("Lower number please!")

    elif player < ai: #if player entered lowest number compare to ai then this block will execute:
        print("Higher number please!")
    
    attempts += 1 #This will counts the attempts untill correct answer is answered

#finally this will print once the loop breaks after correct answer:
print(f"You have guessed the number {player} correctly in {attempts} attempts!")
