
class Player: 
    def __init__(self, score, age): 
        self.score = score
        self.age = age 

    def set_score(self, extra): 
        self.score += extra 
        print(f"Total score: {self.score}")
    def __str__(self) :
        return f"The score is {self.score}, age is {self.age}"

num_players = int(input("Enter number of players:"))
# List to store player names
players_name = [input("enter names of players:") for num in range(num_players)]



# Dictionary to store player instances
players = {}

# Input age and score for each player
for name in players_name: 
    age = int(input(f"Enter age of {name}: "))  # Convert to int
    score = int(input(f"Enter score of {name}: "))  # Convert to int
    players[name] = Player(score, age)  # Store in the dictionary
  

# Ask user if they want to add scores
confirmation = input("Do you want to add scores to a player (y/n)? ")

if confirmation.lower() == 'y':  # Check for 'y' or 'Y'
    ch_name = input(f"Among these, who do you want to change the score? {players_name}: ")
    
    if ch_name in players:  # Check if the name exists in the players
        extra_score = int(input("Enter extra score: "))  # Convert to int
        players[ch_name].set_score(extra_score)  # Call the method
    else:
        print(f"{ch_name} is not a valid player.")

view_confrim = input("Do you want to see all the players details y/n")

if view_confrim.lower() == "y" : 
    for name in players_name: 
       print(f"{name} :{players[name]}")
    file_confrim = input("Do you want to print the these details in text file y/n")
    if file_confrim.lower() == 'y':
        with open("output.txt",'w') as file :
            for name in players_name: 
                file.write(f"\n{name} :{players[name]}") #here \n is to write in next line 


print("thank  you")
