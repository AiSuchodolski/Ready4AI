#from idlelib.rpc import response_queue

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

model = {
1 : "gpt-4o",
2 : "gpt-4o-mini",
3 : "gpt-4-turbo",
4 : "gpt-4-1106-preview",
5 : "gpt-4",
6 : "gpt-4-32k",
7 : "gpt-3.5-turbo",
8 : "gpt-3.5-turbo-16k",
9 : "gpt-3.5-turbo-instruct"
}
for key, value in model.items():
    print(f'{key} - ', value)

model_choice = int(input('Press the model number of your choice : '))
if model_choice > 9 or model_choice == str:
    print('Error wrong number')

selected_model = model.get(model_choice)
print(f'Your choice is: {selected_model}')

def client_message(message, response_id=None):
    if message == 'q':
        exit()

    response = client.responses.create(
        model=selected_model,
        input=message,
        previous_response_id=response_id

    )
    print(response.output_text)
    return response.id

response_id=None
while True:
    response_id = client_message(input("You: "), response_id)