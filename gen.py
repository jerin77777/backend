from openai import OpenAI
import os 



def gen(query):

    client = OpenAI(
        api_key = os.getenv("OPEN_AI_KEY") 
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": query}],
        stream=False,
    )

    result =  response.choices[0].message.content.replace("```json","").replace("```","")
    return result

