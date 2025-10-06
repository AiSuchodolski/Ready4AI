import ast
from math import degrees
import random
import json
import ast
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from openai import OpenAI
from unicodedata import category

load_dotenv()

model = init_chat_model('gpt-4o-mini', model_provider='openai')

category = input('Podaj kategorię: ')
# degrees_of_difficult = input('Podaj stopień trudności: ')

questions = []

i = 0
point = 0
while i < 10:
    formatted_questions = "\n".join([f"- {q}" for q in questions])
    message = [
        SystemMessage(content='Your role is to provide answers in JSON format as follows: {"Question": "Question content", "Answers_4options": "4 answer options", "CorrectAnswer": "Number of the correct answer"}'),
        AIMessage(content=f'You only ask a question in {category} category without commentary in polish language'),
        AIMessage(content=f'You only provide 4 answers (1,2,3,4) of which only one is correct. Do not repeat any of these previous questions: {formatted_questions}'),
]
    result = model.invoke(message)
    try:
        question_dir = {}
        parsed_data = ast.literal_eval(result.content)
        question_dir.update(parsed_data)
        questions.append(question_dir['Question'])
    except json.JSONDecodeError:
         print("JSONDecodeError")

    print(question_dir['Question'])
    print(question_dir['Answers_4options'])
    user_answer = input('Podaj nr prawidłowej odpowiedzi ')
    if user_answer == question_dir['CorrectAnswer']:
        print("Brawo! Prawidłowa odpowiedź masz punkt!")
        point += 1
    else:
        print(f'Niestety zła dopowiedź. Prawidłowa odpowiedź to {question_dir["CorrectAnswer"]}')
    message.append(AIMessage(question_dir['Question']))
    i += 1
print(f"Zdobyłeś {point} punktów na {i} możliwych.")