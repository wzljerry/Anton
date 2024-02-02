from anton import anton_gpt
from utils.prompt_load import load_prompt

class anton_cv_process:
    # Define a class named 'anton_cv_process' for processing CV-related tasks.

    def __init__(self):
        pass
        # An initializer method that currently does nothing (pass).

    # To extract the text information in a cv
    def cv_content_extraction(self, file):
        # Define a method to extract text content from a CV. It takes a file as an argument.

        text_file='./prompt/prompt_cv.txt'
        # Set the path to the text file containing the default prompt for CV content extraction.

        prompt=load_prompt(text_file, 0) # The prompt is default
        # Load the default prompt from the specified text file.

        msg=[{'role': 'user', 'text': prompt, 'image_inputs': [file]}]
        # Create a message structure with the role set to 'user', the loaded prompt, and the input file.

        return anton_gpt.anton_ai().gpt_4_img(msg)
        # Call the Anton AI's method to process the message with GPT-4 for image-related tasks,
        # and return the extracted content from the CV.

    def cv_optimization(self, jd_content, cv_content):
        # Define a method for optimizing a CV based on job description content.

        text_file='./prompt/prompt_cv.txt'
        # Set the path to the text file containing prompts for CV optimization.

        prompt=load_prompt(text_file, 1) + jd_content + cv_content
        # Load the specific prompt for CV optimization and concatenate it with job description
        # and CV content.

        msg=[{'role': 'user', 'text': prompt}]
        # Create a message structure with the role set to 'user' and the combined text as the prompt.

        return anton_gpt.anton_ai().gpt_4_text(msg)
        # Call the Anton AI's method to process the message with GPT-4 for text-based tasks,
        # and return the optimized CV content.

    def cv_generation(self, polished_cv_text, template):
        # Define a method for generating a CV based on polished CV text and a template.

        text_file='./prompt/prompt_cv.txt'
        # Set the path to the text file containing prompts for CV generation.

        prompt = load_prompt(text_file, 2) + polished_cv_text

        #prompt=load_prompt(text_file, 2) + polished_cv_text+ template
        # Load the specific prompt for CV generation and concatenate it with polished CV text
        # and a template.

        msg=[{'role': 'user', 'text': prompt}]
        # Create a message structure with the role set to 'user' and the combined text as the prompt.

        ## Here can call the latex_to_pdf_doc.py to get the cv directly
        # (This commented line indicates a possible integration with a script for converting
        # LaTeX to PDF, which would be useful for generating a formatted CV document.)

        return anton_gpt.anton_ai().gpt_4_text(msg)
        # Call the Anton AI's method to process the message with GPT-4 for text-based tasks,
        # and return the generated CV content.
