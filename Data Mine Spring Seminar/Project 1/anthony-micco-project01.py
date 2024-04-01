#Question 2
print("Hello World")


#Question 3
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
sum = num1 + num2
print("The sum of the two numbers is " + str(sum))


#Question 4
myfruits = []

for x in range(1,6):
    myfruits.append(input(f"Name of fruit {x}: "))

print(myfruits)


#Question 5
import pandas as pd
forest = pd.read_csv("/anvil/projects/tdm/data/forest/ENTIRE_COUNTY.csv")
print(forest.size)
print(forest.info)
print(forest.info())
print(forest.shape)
len(forest)
print(forest.columns)