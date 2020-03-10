import random
import sys

abuse = True 

# Is a...
insult1 = ["a trogladite", "a doo doo head", "a lily pad", "wet blanket"]
# Direct (he, she)
insult2 = ["smells", "has a table face", "walks too fast", "is too responsible"]

print("\n\nFirst off, I got some things I wanna say to you!")

print(insult1[2])




##### FUNCTION-ING #####
def hey(name, age):
    print("\nhey " + name + " you are " + str(age))

hey("john", 28)

print("Done\n")

##### WHILE LOOP ######
print("WHILE LOOP")
i = 0
while i < 5:
    print(i)
    i += 1
print("Done with While loop\n")

##### FOR LOOP ######
print("FOR LOOP")
set = "some text"
count = 0

for i in set:
    if i == "t":
        count += 1

print("found " + str(count) + " t's")
print(str(count) + "\n")


###### FUNCTION 2 #######
print("FUNCTION 2\n")
def power(base, exp):
    result = 1
    for index in range(exp):
        result *= base
    return result

print(str(power(3, 4)) + "\n")


##### 2D LISTS AND NESTED LOOPS ######
print("2D LISTS AND NESTED FOR LOOPS")
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

print("\n")


