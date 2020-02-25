score = 0 # initialise the score variable, it should be 0 at the start

print("What is 2 + 2?")
answer = input ()
answer = int(answer)
if answer == 4:
    print("Well done")
    score = score + 1 # Increase the score by 1
else:
    print("Sorry the answer was 4")

print("What is 4 x 6?")
answer = input ()
answer = int(answer)
if answer == 24:
    print("Well done")
    score = score + 1
else:
    print("Sorry the answer was 24")

print(score)