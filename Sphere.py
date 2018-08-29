import math

start = input("Do you wanna know the volume of your theoretical ball? Yes (y) or no (n)?")
b = "Bye."
i = "Invalid answer."
while start == "y":
    radius = input("Input the radius you wanna use.")
    volume = ((4/3)*(math.pi))*(int(radius)*int(radius)*int(radius))
    print("The volume of your theoretical ball is " + str(volume))
    again = input("Wanna play again? Yes (y) or no (n)")
    if again == "y":
        start = "y"
    if again == "n":
        start = "n"



if start == "n":
    sure = input("You sure?")
    if sure == "y":
        print(b)
    if sure == "n":
        play = input("Do you wanna know the volume of your theoretical ball? Yes (y) or no (n)?")
        if play == "y":
            start == "y"
        if play == "no":
            start = "bitch"

if start == "bitch":
    print(b)

else:
    print(i)
