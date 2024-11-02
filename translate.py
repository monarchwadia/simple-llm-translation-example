# read all files from /files

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from openai import OpenAI
import os
import sys

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def read_files():
    path = os.path.join(os.path.dirname(__file__), 'files')
    files = os.listdir(path)
    print(files)
    for file in files:
        with open(os.path.join(path, file), 'r') as input_file:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a full-text translator. You have been given a text in a foreign language. Translate the text to English in its entirety.",
                    },
                    {
                        "role": "user",
                        "content": input_file.read() + "\n\n\nTranslate the above text to English in its entirety.",
                    }
                ],
                model="gpt-4o-mini",
            )
            translation = chat_completion.choices[0].message.content
            # write to /translated/*
            with open(os.path.join(os.path.dirname(__file__), 'translated', file), 'w') as t:
                t.write(translation)
                # for line in input:
                #     t.write(line)

read_files()