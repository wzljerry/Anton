from anton import anton_gpt
from utils.prompt_load import load_prompt


class anton_tk_letter_process:
    def __init__(self):
        pass

    def tk_letter_generation(self, interviewer_name, interviewee_name, company_name,job_name):
        # Define a method for extracting content from a job description (JD)

        text_file = './prompt/prompt_tk_letter.txt'
        # Set the path to the text file containing the default prompt

        prompt = load_prompt(text_file, 0)+interviewer_name+interviewee_name+company_name+job_name
        # Load the default prompt from the specified text file

        msg = [{'role': 'user', 'text': prompt}]
        # Create a message structure with the role of the user, the loaded prompt, and the input file

        return anton_gpt.anton_ai().gpt_4_img(msg)
        # Call the Anton AI's method to process the message with GPT-4 and an image, and return the result
