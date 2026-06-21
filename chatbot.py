print("=" * 50)
print("🤖 Welcome to DecodeBot")
print("Type 'bye' to exit the chatbot")
print("=" * 50)

while True:
    user_input = input("\nYou: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("Bot: Hello! How can I help you today?")

    # Name
    elif "your name" in user_input:
        print("Bot: My name is DecodeBot.")

    # About AI
    elif "what is ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It enables machines to perform tasks that usually require human intelligence.")

    # Internship
    elif "internship" in user_input:
        print("Bot: This project is part of your AI internship training.")

    # Time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Date
    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # How are you
    elif "how are you" in user_input:
        print("Bot: I am fine and ready to help you!")

    # Thank you
    elif user_input in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    # Help
    elif "help" in user_input:
        print("Bot: You can ask me:")
        print("     • What is AI?")
        print("     • What is your name?")
        print("     • Tell me the date")
        print("     • Tell me the time")
        print("     • Internship")
        print("     • How are you?")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown question
    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Type 'help' to see available commands.")
