from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()


def client_message(message, response_id=None):
    response = client.responses.create(
        model="gpt-4",
        input=message,
        previous_response_id=response_id
)
    print(response.output_text)
    return response.id


response_id = None
while True:
    client_single_message = input("Enter a message (q to quit): ")
    if client_single_message == "q":
        print("Goodbye")
        break
    response_id = client_message(client_single_message, response_id)

