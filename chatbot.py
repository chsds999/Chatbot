import ollama

def chatbot():
    print("Welcome to the Ollama ChatBot! Type 'exit' or 'quit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break

        # Stream the response
        print("ChatBot: ", end="", flush=True)
        stream = ollama.generate(model='llama3', prompt=user_input, stream=True)
        
        for chunk in stream:
            print(chunk['response'], end="", flush=True)  # Print each chunk as it arrives
        print()  # Newline after the response is complete

if __name__ == "__main__":
    chatbot()