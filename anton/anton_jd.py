from anton import anton_gpt
from utils.prompt_load import load_prompt

class anton_jd_process:
    def __init__(self):
        pass
    def jd_content_extraction(self, file):
        # Define a method for extracting content from a job description (JD)
        text_file = './prompt/prompt_jd.txt'
        # Set the path to the text file containing the default prompt
        prompt = load_prompt(text_file, 0)
        # Load the default prompt from the specified text file
        msg = [{'role': 'user', 'text': prompt, 'image_inputs': [file]}]
        # Create a message structure with the role of the user, the loaded prompt, and the input file
        return anton_gpt.anton_ai().gpt_4_img(msg)
        # Call the Anton AI's method to process the message with GPT-4 and an image, and return the result
