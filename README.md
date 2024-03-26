# Homework
I wrote this code back in summer of 2020. The goal was to get search results for all questions in my holiday homework pdfs. Back then, there were no LLMs to do such homework tasks, so google results were pretty much the best I could do.

## Usage
This project accomplishes the goal in 2 steps:
1. Extract questions from the provided PDFs into text files using `extract-text-from-pdf.py`.
2. extract questions from the text file using `extract-questions-cs.py`, `extract-questions-maths.py`, `extract-questions-english.py`, and `extract-questions-physics.py`
3. Run script `get_results.py` to get search results for all the questions extracted in step 2.

## Files in the repository
+ _CS.pdf, English.pdf, Maths.pdf, Physics.pdf_ are the starting point files, which I had as Homework Assignments. Other than the Python scripts, only these files are necessary to run this project. Other files (mentioned below) are only provided for completeness.
+ _CS--text.txt, English--text.txt, Maths--text.txt, Physics--text.txt_ have extracted questions. These files are created by the scripts `extract-questions-cs.py`, `extract-questions-english.py`, `extract-questions-maths.py`, and `extract-questions-physics.py`, respectively.
