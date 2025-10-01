from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Podaj 5 powodów dla których warto uczyć się pythona"
)

print(response.output_text)