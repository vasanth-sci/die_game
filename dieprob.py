import random
import numpy as np 
import pandas as pd 


def random_die():
    return random.randint(1,6)

x = np.linspace(1,100,100)
y= []
for number in x : 
    value = random_die()
    y.append(value)

print(y)
probabilities = {i: 0 for i in range(1, 7)} 
for value in y:
    probabilities[value] += 1  # Count occurrences of each value

for key in probabilities:
    probabilities[key] /= len(y)


print("Die Rolls:", y)
print("Probabilities:", probabilities)


file=pd.DataFrame({"die_values":y})
file.to_excel('probout1.xlsx',index = False)
