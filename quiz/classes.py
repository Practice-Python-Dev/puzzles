#------------------------------
# CLASS HOLDS ...
#------------------------------

# Create a class, Define initialize function
    # Initialize the function with '__init__(self, ...)'
    # Define the attributes to be included in a question - (... , prompt, answer)
class Question:
    # Define the different attributes that will be included in a questin
    def __init__(self, prompt, answer):
        # Asign the values to the actual class object
        self.prompt = prompt
        self.answer = answer
