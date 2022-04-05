print("welcome to my computer quiz")

playing=input("do you want to play? ")
if playing !="yes":
    quit()
print("okay! Let's play :)")
score=0
answer=input("what does CPU stands for? ")
if answer == "central processing unit":
    print('correct!')
    score+=1
else:
    print("incorrect")
answer=input("What does RAM stands for? ")
if answer == "random access memory":
    print('correct!')
    score+=1
else:
    print("incorrect")
answer=input("what does GPU stands for ? ")
if answer == "graphics processing unit":
    print('correct!')
    score+=1
else:
    print("incorrect")
answer=input("yours college name ? ")
if answer == "aditya engineering college":
    print('correct!')
    score+=1
else:
    print("incorrect")
print("you got"+ str(score)+"questions correct!")
print("you got"+str(score/4))


