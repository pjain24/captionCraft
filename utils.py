from transformers import pipeline
import os
import openai


image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")


openai.api_key = "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"

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "


# Provide the path to your text file
FILE_PATH = 'preprompt.txt'


def getSummary(imagePath):
    summary = image_to_text(imagePath)
    return summary[0]['generated_text']


def generateCaption(imageText, addText):
    prompt = generatePrompt(imageText, addText)
    print(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

    
def generatePrompt(imageText, addText):
    file_content = read_text_file(FILE_PATH)
    prompt = file_content + "\n" + "The image summary is as follows: " + imageText + ". Also, some additional information about the image is: " + addText + "\nA:"
    # Print the content of the text file
    print("Your prompt is:", prompt)
    return prompt
