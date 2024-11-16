# In this programme the break syntax is rewritten as stop fucntion
import random

def roll_die():
    return random.randint(1, 6)
class Condition: 
    def __init__(self, value):
        self.value = value 

    def stop(self): 
        self.value = 0  # This will stop the loop

k = Condition(1)

print(f"Initial value: {k.value}")

while k.value == 1:
    # Prompt the user to press 1 to roll the die
    x = int(input("Press 1 to roll the die, or any other key to stop: "))
    
    if x == 1  :  # Compare with the string 
        # Roll the die
        result = roll_die()
        print(f"You rolled a {result}!")

        # Check if the rolled result is one of the dangerous numbers
        if result in [1, 4, 5]:
            print("You are dead!")
        else:
            print("You are safe!")
    else:
        k.stop()  # Stop the game if any other input is given

print("Game over!")








