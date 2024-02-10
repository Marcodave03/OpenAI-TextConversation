# import openai
# import os

# #Ensure you have your OPENAI_API_KEY set in your environment variables, or set it directly here
# openai.api_key = "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" # Replace with your API key if not using environment variables

# def chat_with_openai(prompt):
#     try:
#         response = openai.Completion.create(
#             model="gpt-3.5-turbo",  #Update the model if necessary
#             prompt=prompt,
#             temperature=0.7,
#             max_tokens=150
#         )
#         message = response.choices[0].text.strip()
#         print(f"OpenAI: {message}")
#     except openai.error.OpenAIError as e:
#         print(f"Error: {e}")

# def main():
#     print("OpenAI Chat Terminal (type 'exit' to quit)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             break
#         chat_with_openai(user_input)

# if __name__ == '__main__':
#     main()


import os
import requests
import json

# Assuming you have already set the OPENAI_API_KEY in your environment variables
api_key = "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"

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

def chat_with_openai(message):
    data = {
        'model': "gpt-3.5-turbo",  # Replace with the correct model name
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        chat_message = response_data['choices'][0]['message']['content']
        print(f"OpenAI: {chat_message}")
    else:
        print(f"Error: {response.text}")

def main():
    print("OpenAI Chat Terminal (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        chat_with_openai(user_input)   

if __name__ == '__main__':
    main()
