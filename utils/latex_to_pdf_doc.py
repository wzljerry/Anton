import subprocess
import os
def compile_latex_and_convert_to_word(file_name, output_folder):
    """
    Compiles a LaTeX file to PDF, converts the same LaTeX file to a Word document,
    and cleans up auxiliary files.
    First we should download the Tex compiler on the server, see https://www.latex-project.org/get/

    :param file_name: The name of the LaTeX file to be compiled.
    :param output_folder: The folder where the output files (PDF and Word) will be saved.
    """
    # Ensure the output folder exists, create if it does not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Replace with the path to your pdflatex executable
        pdflatex_path = "/Library/TeX/texbin/pdflatex" # this is the path of pdflatex on the machine, use 'which pdflatex' to get

        # Compile the LaTeX file to PDF
        subprocess.run([pdflatex_path, "-output-directory", output_folder, file_name], check=True)
        print(f"File {file_name} compiled to PDF successfully in {output_folder}.")

        # Base name of the LaTeX file
        base_name = os.path.splitext(os.path.basename(file_name))[0]

        # Convert the LaTeX file to a Word document using Pandoc
        docx_file = os.path.join(output_folder, base_name + ".docx")
        subprocess.run(["pandoc", file_name, "-o", docx_file], check=True) # pandoc is a package
        print(f"File {file_name} converted to Word document {docx_file}.")

        # Clean up .aux and .log files
        for ext in ['.aux', '.log', '.out']:
            file_to_remove = os.path.join(output_folder, base_name + ext)
            if os.path.exists(file_to_remove):
                os.remove(file_to_remove)
                print(f"Deleted file: {file_to_remove}")

    except subprocess.CalledProcessError:
        print(f"Failed to process {file_name}.")

# Compile test.tex and convert it to a Word document
compile_latex_and_convert_to_word("./data/compiled_file/test.tex", "./data/compiled_file")

