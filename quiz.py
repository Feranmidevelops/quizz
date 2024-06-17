print('welcome to the quiz!')

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("ok lets quiz!")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score +=1
else:
    print("incorrect!")

answer = input("what does ram stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score +=1
else:
    print("incorrect!")

answer = input("what does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score +=1
else:
    print("incorrect!")

answer = input("what does html stand for? ")
if answer.lower() == "hypertext markup language":
    print('correct!')
    score +=1
else:
    print("incorrect!")

print("you got" + str(score) + " questions correct.")
print("you got" + str((score / 4) * 100) + "%.")
