import os

def save_text_to_file(text, filename, file_format, folder_path):
    """
    Saves the given text data to a file with the specified format and name in the given folder.

    :param text: String containing the text to be saved.
    :param filename: Name of the file without the format extension.
    :param file_format: Format of the file (e.g., 'txt', 'csv').
    :param folder_path: Path to the folder where the file will be saved.
    """
    # Ensure the folder exists, if not, create it
    os.makedirs(folder_path, exist_ok=True)

    # Construct the full file path
    file_path = os.path.join(folder_path, f"{filename}.{file_format}")

    # Write the text to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"File saved successfully at {file_path}")

# # 使用示例
# text_data = ""
# save_text_to_file(text_data, "example_filename", "txt", "/path/to/folder")
