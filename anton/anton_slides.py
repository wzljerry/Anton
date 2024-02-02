from anton import anton_gpt
from utils.prompt_load import load_prompt

class anton_slides_process:
    def __init__(self):
        pass
        # Constructor for the anton_slides_process class. Currently, it does nothing (pass).

    def slides_generate(self, tmp="", asiss_infor="", cv="", jd=""):
        # This method generates slides. It now allows empty inputs for all parameters:
        # tmp - a template identifier (default empty),
        # asiss_infor - additional assistant information (default empty),
        # cv - the curriculum vitae (resume) of the applicant (default empty),
        # jd - job description (default empty).

        text_file = './prompt/prompt_slides.txt'
        # Specifies the path to the text file containing prompts for slide generation.

        # Initialize an empty prompt string
        prompt = load_prompt(text_file, 0)
        # Add CV, job description, assistant information, and template identifier to the prompt, if they are not empty.
        for content in [cv, jd, asiss_infor, tmp]:
            if content:
                prompt += "\n" + content

        msg = [{'role': 'user', 'text': prompt}]
        # Create a message structure with the role set to 'user' and the combined text as the prompt.

        return anton_gpt.anton_ai().gpt_4_text(msg)
        # Call the Anton AI's method to process the message with GPT-4 (text-based),
        # and return the generated slides.
