#from idlelib.rpc import response_queue

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def client_message(message, response_id=None):
    if message == 'q':
        exit()

    response = client.responses.create(
        model="gpt-4o",
        input=message,
        previous_response_id=response_id

    )
    print(response.output_text)
    return response.id

response_id=None
while True:
    response_id = client_message(input("You: "), response_id)