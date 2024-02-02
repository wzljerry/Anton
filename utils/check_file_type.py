import os
from urllib.parse import urlparse
from pathlib import Path

class FileAnalyzer:
    def __init__(self, file_input):
        self.file_input = file_input

    def analyze(self):
        if self._is_url(self.file_input):
            return self._handle_url()
        elif isinstance(self.file_input, str):
            return "Input is a string."
        else:
            return self._analyze_file()

    def _is_url(self, string):
        try:
            result = urlparse(string)
            return all([result.scheme, result.netloc])
        except:
            return False

    def _handle_url(self):
        # This method should be expanded based on how you want to handle URLs
        return f"Input is a URL: {self.file_input}"

    def _analyze_file(self):
        if not os.path.exists(self.file_input):
            return "File does not exist."

        file_extension = Path(self.file_input).suffix.lower()

        if file_extension in ['.pdf', '.doc', '.txt']:
            return f"File is a text document: {file_extension}"
        elif file_extension in ['.jpg', '.jpeg', '.png']:
            return f"File is an image: {file_extension}"
        else:
            return "Unsupported file format."

# # Example Usage
# file_analyzer = FileAnalyzer("example.pdf")
# print(file_analyzer.analyze())
