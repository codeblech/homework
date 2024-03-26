from pprint import pprint

with open("English---text.txt", encoding="utf-8") as file:
    string = file.read()
    string = string.replace("\n", " ")


def check_form(two_char_string):
    correct = False
    if two_char_string[0] == "Q":
        if two_char_string[1] == ".":
            correct = True
    return correct


def extract_questions(s):
    start = stop = 0
    length = len(s)
    questions = []

    while start < length:
        if check_form(s[start : start + 2]):
            for i in range(start + 1, length):
                if check_form(s[i : i + 2]):
                    stop = i - 1
                    questions.append(s[start:stop])
                    start = stop

                elif i == length - 1:
                    questions.append(s[start:length])
                    start = length
        else:
            start += 1
    return questions


questions = extract_questions(string)