from utils.prompt_load import load_prompt
from anton import anton_gpt

class anton_interview_process:
    def __init__(self):
        pass

    def interview_qa(self, cv, jd):
        """
        Generates interview questions and answers based on the given CV and job description (jd).

        :param cv: The curriculum vitae or resume of the candidate.
        :param jd: The job description for the position.
        :return: Generated interview questions and answers.
        """
        text_file = './prompt/prompt_interview.txt'  # Path to the text file containing prompts.
        prompt = load_prompt(text_file, 0) + cv + jd  # Combining the first prompt with CV and JD.
        msg = [{'role': 'user', 'text': prompt}]  # Creating a message format for processing.
        return anton_gpt.anton_ai().gpt_4_text(msg)  # Invoking the GPT-4 model for text generation.

    def interview_self_introduction(self, cv, jd, time):
        """
        Generates a self-introduction script for an interview based on CV, job description, and allotted time.

        :param cv: The curriculum vitae or resume of the candidate.
        :param jd: The job description for the position.
        :param time: The time allocated for the self-introduction.
        :return: Generated self-introduction script.
        """
        text_file = './prompt/prompt_interview.txt'  # Path to the text file containing prompts.
        # Combining the second prompt with CV, JD, and the self-introduction time.
        prompt = load_prompt(text_file, 1) + cv + jd + "The self introduction is " + time + " minutes"
        msg = [{'role': 'user', 'text': prompt}]  # Creating a message format for processing.
        return anton_gpt.anton_ai().gpt_4_text(msg)  # Invoking the GPT-4 model for text generation.



