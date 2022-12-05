import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def ask(q):
    response = openai.Completion.create(
        engine="code-davinci-001",
        prompt=f"\"\"\"\n{q}\n\"\"\"",
        temperature=0,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    return response.choices[0].text
