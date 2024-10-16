from openai import OpenAI
from typing import Dict
from string import Template
import os

current_dir = os.path.dirname(__file__)
key_file = os.path.join(current_dir, 'key.local')

PROMPTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts")

with open(key_file, 'r') as f:
    key = f.read().replace('\n', '')
    

client = OpenAI(
    api_key=key
)

class clientOpenAI:
    def __init__(self):
        self.client = client
        self.prompts: Dict[str,str] = self.load_prompts()
        
        
    def call_gpt(self, prompt):
        respons = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            # max_tokens=100,
            # temperature=0.3,
            # response_format= { "type": "json_object" }
        ).choices[0].message.content
        
        return respons
    
    def load_prompts(self):
        prompts = {}
        for file in os.listdir(PROMPTS_PATH):
            if file.endswith(".txt"):
                prompts[file] = self.load_text_from_txt(os.path.join(PROMPTS_PATH, file))
        return prompts

    def output_prompt(self, statistics_data):
        prompt = self.prompts["output_prompt.txt"]
        prompt = Template(prompt)
        data_to_replace = {"statistics_data": statistics_data}
        prompt = prompt.substitute(data_to_replace)
        
        return self.call_gpt(prompt)
    
    def load_text_from_txt(self, file_path):
        with open(file_path, "r") as f:
            return f.read()