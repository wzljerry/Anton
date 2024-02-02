# Anton: AI-powered Resume Generation Tool

## Set Up
Please ensure that Anton is running with Python3.9+.

In terminal:
```shell
pip3 install -r requirements.txt
```
There could be some requirements not listed in requirements.txt. If you want to
compile the LaTeX file, please ensure that you have installed LaTeX on your machine, please see <https://www.latex-project.org/get/>. Besides, if you
want to compile the .tex file into .doc file, please install pandoc, see <https://pandoc.org/installing.html>.

## Example
Here we provide the simple use cases of Anton. Anto first transfer the document with any format  into image format:

PDF to image
```python
from utils import pdf_to_img
convert_and_merge_pdf_to_jpg(pdf_path, output_folder)
```
URL to image
```python
from utils import web_to_img
capture_fullpage_screenshot(url, folder)
```
Then, we can use Anto to process the resume and job description.
### 1. Extract the CV content
```python
from anton.anton_cv import anton_cv_process
cv_path="./data/CV/text.jpg"
cv_text=anton_cv_process().cv_content_extraction(cv_path)
```
We can save the extracted content via

```python
from utils import save_text_data
save_text_dat(cv_text,"extracted_cv","json","./data/stored_cv")
```

### 2. Extract the JD content
```python
from anton.anton_jd import anton_jd_process
jd_path="./data/CV/jd_text.jpg"
jd_text=anton_jd_process().jd_content_extraction(jd_path)
```

### 3. Polish the CV based on the extracted CV and JD
```python
from anton.anton_cv import anton_cv_process
polished_cv=anton_cv_process().cv_optimization(jd_text,cv_text)
```
### 4. Generate CV based on the given LaTeX format
```python
from anton.anton_cv import anton_cv_process
template="./data/compiled_file/template.tex"
cv_latex_code=anton_cv_process().cv_generation(polished_cv,template)
```

Assume the latex source code is extracted and saved as text.tex, we can get the pdf and doc of a cv
```python
from utils.latex_to_pdf_doc import compile_latex_and_convert_to_word
compile_latex_and_convert_to_word(text.tex, path_to_save)
```
### 5. Cover letter generation
```python
from anton.anton_cover_letter import anton_letter_process
cover_letter=anton_letter_process().cover_letter_generation(polished_cv,jd_text)
```
### 6. Interview Q&A
```python
from anton.anton_interview import anton_interview_process
q_a=anton_interview_process().interview_qa(polished_cv,jd_text)
```

### 7. Self introduction
```python
from anton.anton_interview import anton_interview_process
self_intro=anton_interview_process().interview_self_introduction(polished_cv,jd_text,'1') # 1 is the time of self introduction
```
