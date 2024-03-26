from string import digits
from pprint import pprint

with open("Maths---text.txt", encoding="utf-8") as file:
    string = file.read()
    string = string.replace("\n", " ")


def check_form(two_char_string):
    correct = False
    if two_char_string[0] in digits:
        if two_char_string[1] == ".":
            correct = True
    return correct


def extract_questions(s):
    start = stop = 0
    length = len(s)
    questions = []
    while start < length:

        if check_form(s[start : start + 2]):
            for i in range(start + 2, length):
                if check_form(s[i : i + 2]):
                    stop = i - 1

                    if s[start - 1] in digits:
                        if s[start - 2] in digits:
                            questions.append(s[start - 2 : stop - 1])
                        else:
                            questions.append(s[start - 1 : stop - 1])
                    else:
                        questions.append(s[start : stop - 1])

                    start = stop

                elif i == length - 1:

                    if s[start - 1] in digits:
                        if s[start - 2] in digits:
                            questions.append(s[start - 2 : length - 1])
                        else:
                            questions.append(s[start - 1 : length - 1])
                    else:
                        questions.append(s[start : stop - 1])

                    start = length
        else:
            start += 1
    return questions


questions = extract_questions(string)