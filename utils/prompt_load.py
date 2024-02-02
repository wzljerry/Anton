import re

def load_prompt(text_file, num):
    """
    Extracts a specific string enclosed in double quotes from a text file.

    :param text_file: Path to the text file to be read.
    :param num: The index of the string to be extracted.
    :return: The string at the specified index if found, otherwise None.
    """
    with open(text_file, 'r') as file:  # Open the file in read mode
        content = file.read()  # Read the entire content of the file

    # Use regular expression to find all strings enclosed in double quotes
    strings_in_quotes = re.findall(r'"(.*?)"', content, re.DOTALL)

    # Return the string at the specified index if it exists, else return None
    return strings_in_quotes[num] if num < len(strings_in_quotes) else None