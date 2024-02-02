from anton import anton_gpt
from utils.prompt_load import load_prompt

class anton_letter_process:
    # Define a class named 'anton_letter_process'.

    def __init__(self):
        pass
        # An initializer method that currently does nothing (pass).

    def cover_letter_generation(self, polished_cv, jd_text):
        # Define a method for generating a cover letter.
        # It takes two arguments: 'polished_cv' (a candidate's CV) and 'jd_text' (job description text).

        text_file='./prompt/prompt_letter.txt'
        # Set the path to the text file containing the default prompt for the cover letter.

        prompt=load_prompt(text_file,0) + polished_cv + jd_text
        # Load the default prompt from the specified text file and concatenate it with
        # the polished CV and job description text to form a combined prompt.

        msg=[{'role': 'user', 'text': prompt}]
        # Create a message structure with the role set to 'user' and the combined text as the prompt.

        return anton_gpt.anton_ai().gpt_4_text(msg)
        # Call the Anton AI's method to process the message with GPT-4 (text-based),
        # and return the generated cover letter.





