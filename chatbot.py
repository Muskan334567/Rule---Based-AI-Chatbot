from datetime import datetime

print("="*50)
print("🤖 WELCOME TO RULE-BASED AI CHATBOT 🤖")
print("="*50)

name = input("Enter your name:")
print(f"\nHello, {name}! 👋")
print("I am your AI Chatbot.")
print("You can try the following commands:")
print("➡ hi / hello")
print("➡ how are you")
print("➡ what is your name")
print("➡ time")
print("➡ help")
print("➡ bye")
print("-" * 50)

while True:
    user = input(f"\n{name}: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("🤖 Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("🤖 Bot: I am doing great! Thanks for asking.")

    elif user == "what is your name":
        print("🤖 Bot: I am a Rule-Based AI Chatbot.")

    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"🤖 Bot: Current time is {current_time}")

    elif user == "help":
        print("\n🤖 Bot: Available Commands")
        print("• hi / hello")
        print("• how are you")
        print("• what is your name")
        print("• time")
        print("• bye")

    elif user in ["bye", "exit", "quit"]:
        print(f"🤖 Bot: Goodbye, {name}! Have a great day. 😊")
        break

    else:
        print("🤖 Bot: Sorry, I don't understand that command.")
