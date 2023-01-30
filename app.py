import openai
from secretPass import apiPass

openai.api_key = apiPass

#pet = input('what kind of pet do you want to see?')
#personality = input('what is their personality like?')
#location = input('where would you like them to be?')


response = openai.Image.create(
    prompt=f"a silhouette of a cat near a boat",
    n=1,
    size = "512x512"
)
image_url = response['data'][0]['url']



print(image_url)