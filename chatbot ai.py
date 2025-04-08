import random

# Predefined responses
responses = {
    'hello': ['Hi there!', 'Hello!', 'Hey! How can I help you?'],
    'how are you': ['I am just a program, but I am doing great!', 'I am fine, thanks for asking!', 'I am always good!'],
    'bye': ['Goodbye!', 'See you later!', 'Take care!'],
    'default': ['Sorry, I did not understand that. Can you try again?', 'I am not sure what you mean. Can you rephrase?']
}

# Function to process user input
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check for predefined queries and respond accordingly
    if 'hello' in user_input:
        return random.choice(responses['hello'])
    elif 'how are you' in user_input:
        return random.choice(responses['how are you'])
    elif 'bye' in user_input:
        return random.choice(responses['bye'])
    else:
        return random.choice(responses['default'])

# Main function for the chatbot
def chatbot():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'bye':
            print("Chatbot: " + get_response(user_input))
            break
        
        # Get and display chatbot's response
        response = get_response(user_input)
        print("Chatbot: " + response)

# Run the chatbot
chatbot()
