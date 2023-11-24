from openai import OpenAI

def ChatGPT():
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "아스날이 우승할수 있을까??"}
    ]
    )
    
    
    return completion.choices[0].message.content

# print(completion.choices[0].message)