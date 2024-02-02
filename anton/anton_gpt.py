from openai import OpenAI
from utils import msg_generation

class anton_ai:
    # Define a class named 'anton_ai' to interface with the OpenAI API.

    def __init__(self):
        self.key='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'
        # Initialize the class with an API key for authenticating requests to OpenAI.

    # Image process
    def gpt_4_img(self, msg):
        # Define a method to process image-related tasks using GPT-4.

        client = OpenAI(api_key=self.key)
        # Create an OpenAI client instance with the provided API key.

        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=msg_generation.generate_messages_list(msg),
            max_tokens=3000,
        )
        # Make a request to the OpenAI API using the 'gpt-4-vision-preview' model,
        # sending a generated list of messages and specifying a maximum token limit.

        return response.choices[0].message.content
        # Return the content of the first response from the generated choices.

    # Text process
    def gpt_4_text(self, msg):
        # Define a method to process text-related tasks using GPT-4.

        client = OpenAI(api_key=self.key)
        # Create an OpenAI client instance with the provided API key.

        response = client.chat.completions.create(
            model="gpt-4",
            messages=msg_generation.generate_messages_list(msg),
            max_tokens=3000,
        )
        # Make a request to the OpenAI API using the 'gpt-4' model,
        # sending a generated list of messages and specifying a maximum token limit.

        return response.choices[0].message.content
        # Return the content of the first response from the generated choices.


#print(anton_ai().gpt_4_text([{'role': 'user', 'text': "can you read csv file"}]))




