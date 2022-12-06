import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

initial_prompt = "/*How do you print in javascript?*/### To print in JavaScript you can use the console.log() function. For example, console.log('Hello World!') will print Hello World! to the console.###"


def ask(q):
    # write each question to a json file
    with open("questions.json", "a") as f:
        f.write(q + "\n")

    prompt = initial_prompt.join(f"/*{q}*/###")
    response = openai.Completion.create(
        engine="code-davinci-001",
        prompt=prompt,
        temperature=0,
        max_tokens=2500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    return response.choices[0].text
