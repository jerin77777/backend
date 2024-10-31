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


def nim(model, query):

    client = OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = os.getenv("NVIDIA_API_KEY") 
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role":"user","content":query}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
    )

    result = ""

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            result += chunk.choices[0].delta.content

    result = result.replace("```","").replace("```","")

