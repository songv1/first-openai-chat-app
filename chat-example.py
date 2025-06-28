from openai import OpenAI

client = OpenAI()

print("Chat with the AI (type 'quit' to exit):")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"quit", "exit"}:
        print("Goodbye!")
        break

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=user_input
    )

    print("AI:", response.output_text)
