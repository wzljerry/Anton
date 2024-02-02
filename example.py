from anton.anton_cv import anton_cv_process
from anton.anton_jd import anton_jd_process
from anton import anton_gpt
from anton.anton_cover_letter import anton_letter_process
from anton.anton_interview import anton_interview_process
from utils.save_text_data import save_text_to_file
from utils.latex_to_pdf_doc import compile_latex_and_convert_to_word

# Extract the CV content
cv_path="./data/CV/test_5.jpg"

prompt="Let's think step by step. You are a professional image text extractor. Please extract the text from the given image, which \
is the resume. Given me only the extracted contents."
cv_text_only=anton_gpt.anton_ai().gpt_4_img([{'role': 'user', 'text': prompt, 'image_inputs': [cv_path]}])
print(cv_text_only)
# cv_text=anton_cv_process().cv_content_extraction(cv_path)
# print(cv_text)
# # We should save the extracted content
#
# # Extract the JD content
#
#
jd_path="./data/CV/jd_text.jpg"
jd_text=anton_jd_process().jd_content_extraction(jd_path)

# Polish the CV based on the extracted CV and JD
polished_cv=anton_cv_process().cv_optimization(jd_text,cv_text_only)

# Generate CV based on the given LaTeX format
template="./data/compiled_file/template.tex"
cv_latex_code=anton_cv_process().cv_generation(polished_cv,template)

save_text_to_file(cv_latex_code, "test_1", "tex", "./data/compiled_file")

## assume the latex source code is extracted and saved as text.tex, we can get the pdf and doc of a cv

compile_latex_and_convert_to_word('./data/compiled_file/test_1.tex', './data/compiled_file')

# # cover letter generation
# cover_letter=anton_letter_process().cover_letter_generation(polished_cv,jd_text)
#
# # interview Q&A
# q_a=anton_interview_process().interview_qa(polished_cv,jd_text)
# #print(q_a)
#
#
# # self_introduction
# self_intro=anton_interview_process().interview_self_introduction(polished_cv,jd_text,'1') # 1 is the time of self introduction
# #print(self_intro)
#












