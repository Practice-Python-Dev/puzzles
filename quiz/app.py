# From 'the question file' import 'the Question class' - Note, all the code could be in one file
from classes import Question

#------------------------------
# CREATE QUESTION PROMPTS
#------------------------------

# Two parts to each question:
    # The prompt
    # The answers
question_prompts = [
    "\nWhat color are bananas?\n(a) Red\n(b) Purple\n(c) Yellow\n\n",
    "\nWhat color are oranges?\n(a) Red\n(b) Orange\n(c) Yellow\n\n",
    "\nWhat color are strawberries?\n(a) Green\n(b) Purple\n(c) Red\n\n",
    "\nWhat color are blueberries?\n(a) Blue\n(b) Purple\n(c) Yellow\n\n",
    "\nWhat color are potatoes?\n(a) Green\n(b) Brown\n(c) Black\n\n"
]

#------------------------------
# CREATE QUESTION OBJECTS
#------------------------------

# Hold the objects in a list (array)
questions = [
    # Pass the first 'question_prompt', Pass the correct answer
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
]

#------------------------------
# FUNCTION THAT RUNS THE QUIZ
#------------------------------

# Take one parameter (a list of 'questions')
    # 1) Loop through each question
    # 2) Ask the question to the user
    # 3) Get the users answer
    # 4) Check if it's right (and save)
def run_quiz(questions):
    score = 0  # Score counter

    for question in questions:
        # Get user answer
        answer = input(question.prompt)
        # Check if it's right
        if answer == question.answer:
            score += 1
    # Print the users score
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct.")

# Call the function
run_quiz(questions)
