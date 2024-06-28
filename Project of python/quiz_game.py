# Quiz Game

print("Welcome to my computer quiz!")

playing  = input("Do you want to play? ")
if playing.lower() != "yes":
          quit()


print("okay! lets play:")
score = 0

#1st ques ->
answer= input("what does the CPU stands for ? ")
if answer.lower() ==  "central processing unit":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        score -= 1

#2nd ->
answer = input("what does the GPU stands for ? ").lower()
if answer ==  "graphics processing unit":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        score -= 1

#3rd ->
answer = input(" what does RAM stands for ? ")
if answer.lower() ==  "random access memory":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        score -= 1

#4th ->
answer = input("what does ROM stands for? ")
if answer.lower() ==  "read only memory":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        score -= 1

#5th ->
answer = input("what does CD stands for?  ").lower()
if answer ==  "compact disk":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        score -= 1

print("You got  " + str(score) + "  Marks!")
print("You got  " + str((score/5)*100) + " %. ")

if score == 5:
        print("Congratulation! You got the Highest marks ")

if score == -5:
        print("You have to work on yourself! I hope you understand")