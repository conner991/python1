import random
import sys

# Is a...
insult1 = ["trogladite", "doo doo head", "lily pad", "wet blanket", "Johnny Wohnny", 
"murk lurker", "silly billy", "trap cactus", "con-wap-nay", "reaaaal bummer"]
# Direct (he, she)
insult2 = ["smell", "have a table face", "walk too fast", "is too ressponsible", "looks like a crab",
"sings horribly", "likes to steal chips", "won't give me me $100", "eats beets", "kicks my dog"]


print("\n\nFirst off, I got some things I wanna say to you!\n")

you = True
abuse = True 
i = 0

while abuse:
    
    while you:
        i += 1
        print("You are a " + random.choice(insult1) + ".")
        if i == 2:
            you = False
    
    someone = True
    j = 0

    print("\nOk, ok.. I apologize, I just had to get that out of my system...")

    lovedOne = input("Say, I'm a little curious... Who is someone dear to your heart? ")
    print("\nWell your " + lovedOne + " " + random.choice(insult2) + ".")
        
    while someone:
        j += 1
        print("and " + random.choice(insult2))
        if j == 2:
            someone = False

    final_choice = input("Dang that was fun!... Wanna do it again?? yes or no: ")

    if final_choice == "no":
        abuse = False
        print("Fine! So long!\n")

    elif final_choice == "yes":
        you = True
        i = 0
        print("YAY let's do it!\n\n")

    else :
        i = 0
        print("Wrong answer, here we go again! HAHAHAHA\n\n")

    
    
        





    
        



