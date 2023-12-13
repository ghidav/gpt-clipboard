import pyperclip
from openai import OpenAI
import sys
import os

def main(input_text):
    os.environ["OPENAI_API_KEY"] = "..."
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a coding assistant.\nYou read code and a comment; you take the comment as an instruction to complete the code.\nYou write only the code completion."
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response.choices[0].message.content
    #print(response_text) 
    pyperclip.copy(response_text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        main(input_text)
    else:
        print("No input text provided")
