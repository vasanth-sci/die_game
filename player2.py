class player : 
    def __init__(self,score,age) :
        self.score = score
        self.age = age 


    def set_score(self, extra): 
        self.score += extra 
        print(f"total score:{self.score}")
    
    def __str__(self) :
        return f"The score is {self.score}, age is {self.age}"


players_name =['vasanth']

for name in players_name: 
    
    age = int(input(f"enter age of {name}"))
    score =int(input(f"enter score of {name}"))

    globals()[name]= player(score,age)

confirmation = input(" do you want to add scores to person y/n ?")

if confirmation == 'y' :
    ch_name = input(f"among these who u want to change the score: {players_name}")
    globals()[ch_name].set_score(int(input("extra score")))
else : 
    print("thank you")

view_confrim = input("Do you want to see all the players details y/n")

if view_confrim =="y" : 
    for name in players_name: 
       print(globals()[name])
else:
    print("thank  you")




