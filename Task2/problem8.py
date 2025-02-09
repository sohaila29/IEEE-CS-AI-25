

import random
def guess_number_game():
    while True:
        wanted_num = random.randint(1,100)
        tries = 3

        while tries > 0:
            player_guess = int(input("guess number from 1 to 100: "))
            
            if  player_guess == wanted_num:
                print("Congratulations Winner!")
                break
            elif player_guess< wanted_num:
                print("Your number is  lower than mine")
            else:
                print("Your number is  higher than mine")
            
            tries -= 1
            if tries == 0:
                print("Run out of tries!!")

guess_number_game()