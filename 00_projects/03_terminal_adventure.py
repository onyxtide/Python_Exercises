#Teminal-fantasy mini-game
import random

# INTRODUCTION
print("Hello, welcome to the library of Borges")
username = input("What is your name? ")
print(f'Nice to meet you {username}!')

print(f"{username}, we now need to teleport you towards one of Borges' surreal worlds")

# Start of world building
world = random.randint(1, 2)

if world == 1:
    print("Woosh, you are now in Borges' Labyrinth")
    print("Every path seems different... but is it?")

    # --- LABYRINTH GAME ---
    found_exit = False

    while not found_exit:
        choice = input("Time to choose a path (left / right / forward): ")

        if choice == "left":
            print("You walk left... and somehow return to the same place.")
        elif choice == "right":
            print("You walk right... but the corridor bends back to where you started.")
        elif choice == "forward":
            print("You have found the exit!")
            print("Or maybe this is just another beginning.")
            found_exit = True
        else:
            print("That path does not exist.")


elif world == 2:
    print("Woosh, you are now in Borges' Fever Dream")
    print("I'm the voice that occupies your fever dream")
    print("I might let you out of here. Place your trust in me")

    # --- FEVER DREAM GAME ---
    godsflip = random.randint(1, 2)

    if godsflip == 1:
        mode = "echo"
    else:
        mode = "shadow"

    echo_answer1 = "What is the root of four? "
    shadow_answer1 = "What is not the root of four? "
    echo_answer2 = "Is life real? "
    shadow_answer2 = "Is death fake? "

    fever1 = input("What is the root of four? ")
    fever2 = input("Is life real? ")


    if mode == "echo" and fever1 == echo_answer1 and fever2 == echo_answer2:
        print("Correct! You've been released!")
    elif mode == "shadow" and fever1 == shadow_answer1 and fever2 == shadow_answer2:
        print("Correct! You've been released!")
    else:
        print("Hahaha, you are wrong!")
        print("I will now devour you!")