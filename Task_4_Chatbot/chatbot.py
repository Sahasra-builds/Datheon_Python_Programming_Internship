
from datetime import datetime


def chatbot():
    print("\nWelcome to Python Assistant!")
    print("I am your simple terminal chatbot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.\n")

    while True:
        message = input("You: ").lower().strip()

        if message in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif message == "help":
            print("\nBot: I can help you with:")
            print("1. Greetings")
            print("2. Current date")
            print("3. Current time")
            print("4. Simple calculations")
            print("5. Exit\n")

        elif "date" in message:
            today = datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", today)

        elif "time" in message:
            current_time = datetime.now().strftime("%I:%M:%S %p")
            print("Bot: Current time is", current_time)

        elif "calculate" in message:
            try:
                first = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                second = float(input("Enter second number: "))

                if operator == "+":
                    result = first + second
                elif operator == "-":
                    result = first - second
                elif operator == "*":
                    result = first * second
                elif operator == "/":
                    if second == 0:
                        print("Bot: Cannot divide by zero.")
                        continue
                    result = first / second
                else:
                    print("Bot: Invalid operator.")
                    continue

                print("Bot: Result =", result)

            except ValueError:
                print("Bot: Please enter valid numbers.")

        elif message in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand. Type 'help'.")


if __name__ == "__main__":
    chatbot()
