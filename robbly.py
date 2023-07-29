import random
import time

#Thhis is a simple command based bot where you can do simple things
#Run the command .help to get a full list of commands available.



print("Hello There! This is Robbly! I am a simple command based bot where you can do simple tasks!")
print("Run .help for a list of commands available!")

loop = True
while loop:

    cmd = input("command : ")

    if cmd == ".help":
        print("Here's a List of Commands Available")
        time.sleep(1)
        print(".cal - Open up the Calculator")
        print(".roll - Roll a Dice")
        print(".randRange - Get a Random Number within a Range of numbers")
        print(".bet - Place a bet with your Friend")
        print(".random - Get A Random Gift From Me!!!")
        print(".end - End this session")
        time.sleep(3)

    elif cmd == ".roll":
        print("Rolling...")
        time.sleep(1)
        print("You Rolled ", random.randint(1,6))
        time.sleep(2)

    elif cmd == ".randRange":
        range1 = int(input("Enter the Number that the range should start from : "))
        range2 = int(input("Enter the Number that the range should end at : "))
        if range1 == range2:
             print("Are You Drunk?")
        elif range1 < range2:
            print("Generating...")
            time.sleep(1)
            print("You got", random.randint(range1,range2))
        else:
             print("This is Invalid")
        time.sleep(3)

    
    elif cmd == ".cal":
        print("Welcome to Robbly Calculator")
        time.sleep(1)
        answer = input ("Do you want to add, substract, multiply or divide : ")
        if answer == "add" or "Add" or "ADD" or "1":
                num1 = float(input ("First Number is : "))
                num2 = float(input ("Second Number is : "))
                num3 = num1 + num2
                print(num3)
        elif answer == "substract" or "Substract" or "SUBSTRACT" or "2":
                print("You can substract here")
                num1 = float(input ("First Number is : "))
                num2 = float(input ("Second number is : "))
                num3 = num1 - num2
                print(num3)
        elif answer == "multiply" or "Multiply" or "MULTIPLY" or "2":
                print("You can multiply here")
                num1 = float(input ("First Number is : "))
                num2 = float(input ("Second number is : "))
                num3 = num1 * num2
                print(num3)
        elif answer == "divide" or "Divide" or "DIVIDE"or "4":
                print("You can divide here")
                num1 = float(input ("First Number is : "))
                num2 = float(input ("Second number is : "))
                num3 = num1 / num2
                print(num3)
        else:
                print("Service not available")
        print("Thank you for visiting")
        time.sleep(3)

    elif cmd == ".bet":
        print("Place a Bet with Your Friend!")
        time.sleep(1)
        fr1 = input("Enter Your Name : ")
        fr2 = input("Enter Your Friends Name : ")
        print("Rolling...")
        time.sleep(1)
        rand1 = random.randint(1,2)
        if rand1 == 1:
            print("You Won the Bet", fr1, "! Congrats!")
        else :
            print(fr2, "Won the Bet! Congrats!")
        time.sleep(3)

    elif cmd == ".random":
        rand2 = random.randint(1,4)
        if rand2 == 1:
            print("WOW!!! You won a valuable gift!")
            time.sleep(1)
            print("To claim it, go to serendibytes.rf.gd and purchase a plan!")
            time.sleep(1)
            print("You'll Never Fell Bad about It! I guarantee!")
        elif rand2 == 2:
            print("Oh Yeah! You won a link to an Amazing Github Profile!")
            time.sleep(1)
            print("Visit github.com/nejanx")
            time.sleep(1)
            print("You'll find some amazing JavaScript content there!")
        elif rand2 == 3:
            print("OMG! You found the link to the Best Python github profile ever!")
            time.sleep(1)
            print("Go to github.com/whitehackerneth")
            time.sleep(1)
            print("Best Python Github Page Ever!!!")
        elif rand2 == 4:
            print("Congrats! You won the link to the Best ever website of BULLS!!!")
            time.sleep(1)
            print("Visit parliament.lk to claim your prize!!!")


    elif cmd == ".end":
        loop = False
        print("Thank You for Using Robbly! See You Later!")
        print("Suggest anything to add to this bot to me on Discord. My Username - uthum.minisaa")  

    else:
        print("Command not Available.")
        time.sleep(1)
        print("Request to Add that command with some features by sending a Direct Message to uthum.minisaa on Discord")
        print("Or run .end to End this session")
        time.sleep(3)