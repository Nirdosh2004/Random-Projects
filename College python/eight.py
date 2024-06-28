# guess = int(input("Guess the number : "))
# number = guess.randint(1,4)
# while():
#           if(guess != number):
#                     print("Try again sir")
          
#           else:sh
#                     print("Congratulation hero")
#                     break
          
import random
number = random.randint(1,5)
playerName = input("Enter your name: ")
numberOfGuesses = 0
print("okay " + playerName + " I am guessing a number between 1 and 5")

while(numberOfGuesses<3):
          guess = int(input("Enter your guess number :") )
          numberOfGuesses += 1
          if(guess < number):
                  print("Your guess is too low")
          if(guess > number):
                  print("Your guess is too high")
          if(guess == number):
                  break
if(guess == number):
        print("You guess the number in " + str(numberOfGuesses) + " tries")

else :
        print("You didn't guess the number the number was : " , number)