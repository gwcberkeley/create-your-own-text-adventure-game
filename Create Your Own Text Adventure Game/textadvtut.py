# Create your own text adventure game using Python!

# Step 1: Determine your storyline
    # A sample storyline is shown below.

# High Level Story Description: You’re walking on campus looking for your intro to CS class.
# Story Element: "As you walk into a class, you notice you are in the wrong building. You exit and see he quad splits revealing two science buildings. The building on the RIGHT has more people entering. The building to the LEFT is where most computer labs are located."
# Question: "Do you choose to go RIGHT or LEFT?"
# Answer A, Story Element: If RIGHT: "You look for women from your GWC College Loop to ask for directions."
# Answer B, Story Element: If LEFT: "You start to power walk into the building. You break into a run when you catch a glimpse of a friend in the computer lab.”

# Step 2: Input / Output
# The first step with any text-based programming language is to learn how to do Input/Output.

# Let's first print the storyline!

print("As you walk into a class, you notice you are in the wrong building. You exit and see he quad splits revealing two science buildings. The building on the RIGHT has more people entering. The building to the LEFT is where most computer labs are located.")

# Now, we want to ask the question: "Do you choose to go RIGHT or LEFT?"
answer = str(input("Do you choose to go RIGHT or LEFT?"))

# Answer A, Story Element: If RIGHT: "You look for women from your GWC College Loop to ask for directions."
# Answer B, Story Element: If LEFT: "You start to power walk into the building. You break into a run when you catch a glimpse of a friend in the computer lab.”

# Step 3: Variables
#   A variable is a value that you want to save and re-use.
#   How? Assign a name to the value you are storing by using the equals ("=") sign.
#   We want to re-use variables because it would be cumbersome to type out (in our case) long strings.

# Let's store our storyline
storyline = "As you walk into a class, you notice you are in the wrong building. You exit and see he quad splits revealing two science buildings. The building on the RIGHT has more people entering. The building to the LEFT is where most computer labs are located."

# Let's store our question
question = "Do you choose to go RIGHT or LEFT?"

# Let's store answer A first.
right = "You look for women from your GWC College Loop to ask for directions."

# Now, store answer B.
left = "You start to power walk into the building. You break into a run when you catch a glimpse of a friend in the computer lab."


# Step 4: Conditionals
# Now, let's use a conditional to decide whether to go to Story Element 2A or 2B.

# Check if the user wants to exit the program
if(answer == "QUIT"):
    quit()

# Check if user wants to go RIGHT, then print StoryElement for A
if(answer == "RIGHT"):
    print("You look for women from your GWC College Loop to ask for directions.")

# Check if user wants to go LEFT, then print StoryElement for B
if(answer == "LEFT"):
    print("You start to power walk into the building. You break into a run when you catch a glimpse of a friend in the computer lab.")

# Step 5: Loops
# What are loops?
#   A loop is a sequence of instructions that is repeated until x condition is reached
# In our case, we want to continuously check if the user typed "RIGHT", "LEFT", "QUIT", or utter nonsense.
# The code will continue running until the user types "RIGHT", "LEFT", or "QUIT".
while(answer != right and answer != left):
    # Ask question of which direction you would like to go and store their response
    answer = str(input(question + " "))
    if(answer == "QUIT"):
        exit()

# If the while loop exits, this means that the user has typed "RIGHT", "LEFT", OR "QUIT".
# Now, let's add our conditional statements we made in Step 4 down below.
if(answer == "RIGHT"):
    print("You look for women from your GWC College Loop to ask for directions.")

if(answer == "LEFT"):
    print("You start to power walk into the building. You break into a run when you catch a glimpse of a friend in the computer lab.")

# Step 6: Functions
# What is a function?
#   A function is a block of reusable code that serves a single purpose.
#   In our case, we want to create a function that takes in our story element, a question, answerA to question, answerB to question
# We want to reuse our function to take in different story elements, different questions, and different responses to that question.
# Yet, we want our code to be the same.
# Each question answered will open up a path or paths to new questions and this process repeats!

# Here is our main function:
# We are taking in the current storyline description, a question, and two possible answer choices -- going right or left.
def myTextAdvGame(storyline, question, answerA, answerB):
    print(storyline)
    answer = ""
    while(answer != answerA and answer != answerB):
        answer = str(input(question + " "))
        if(answer == "QUIT"):
            exit()
    return answer

# Now that we have created a function to answer our first question, let's call the function to get our first answer.
# Then, let's reuse this function to ask new questions with new answer choices.

# Here is our first function call.
currentAnswer = myTextAdvGame(storyline, question, "RIGHT", "LEFT")

# Check if the user answered "RIGHT"
if(currentAnswer == "RIGHT"):
    currentAnswer = myTextAdvGame("You just found a friend in your a college loop!", "Do you want to say hi?", "YES", "NO")

# Check if the user answered "LEFT"
if(currentAnswer == "LEFT"):
    currentAnswer = myTextAdvGame("You made it to your class! You've won the game!", "Do you want to play again?", "YES", "NO")
    # The code below is an example of how you would either "win" or "lose" the game!
    if(currentAnswer == "YES"):
        myTextAdvGame(storyline, question, right, left)
    else:
        exit()
