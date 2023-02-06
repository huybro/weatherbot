import openai

openai.api_key = "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"

def create_image(prompt):
    response = openai.Image.create(
    prompt=prompt,
     n=1,
    size="1024x1024"
)
    response = response['data'][0]['url']
    return response
