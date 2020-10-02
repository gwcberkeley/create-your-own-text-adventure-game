def myTextAdvGame(storyline, question, answerA, answerB):
    print(storyline)
    answer = ""
    while(answer != answerA and answer != answerB):
        answer = (input(question + " "))
        if(answer == "QUIT"):
            exit()
    return answer

storyline = "As you walk into a class, you notice you are in the wrong building. You exit and see he quad splits revealing two science buildings. The building on the RIGHT has more people entering. The building to the LEFT is where most computer labs are located."
question = "Do you choose to go RIGHT or LEFT?"
currentAnswer = myTextAdvGame(storyline, question, "RIGHT", "LEFT")

if(currentAnswer == "RIGHT"):
    currentAnswer = myTextAdvGame("You just found a friend in your a college loop!", "Do you want to ask for directions?", "YES", "NO")
    if(currentAnswer == "YES"):
      print("You found your class!")
      exit()


if(currentAnswer == "LEFT"):
    currentAnswer = myTextAdvGame("You made it to your class! You've won the game!", "Do you want to play again?", "YES", "NO")
    if(currentAnswer == "YES"):
        currentAnswer = myTextAdvGame(storyline, question, "RIGHT", "LEFT")
    else:
        exit()
