class player : 
    def __init__(self,score,age) :
        self.score = score 
        self.age = age 


    def set_score(self, extra): 
        self.score += extra 
        print(f"total score:{self.score}")


num_players = int(input("Enter numberof players:"))

for x in range(num_players): 
    name = input("enter name ")
    age = input("enter age")
    score = input("enter score")

    globals()[name]= player(score,age)



