from pprint import pprint
import requests
from bs4 import BeautifulSoup
import random

# How to use: get questions list by running the extract-questions-... files.
# Make a list of those question here, like below.
# run get_search_results

questions = ['Q. Who is the author of the story “ The Last Lesson”?', ' Q. What is the life term of the writer?', ' Q. Which country does the writer belong to ?', ' Q. Which war does the writer mention in the story ?', ' Q. Which country was defeated in the war ?']

def get_search_results():

    for i, question in enumerate(questions, start=1):
        output_for_one_question = str(i) + '. ' + question + '\n'
        output_for_all_questions = ''
        text = question.strip('Q. ?')
        url = 'https://google.com/search?q=' + text
        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
            )

        Agent = A[random.randrange(len(A))]

        headers = {'user-agent': Agent}
        r = requests.get(url, headers=headers)

        soup = BeautifulSoup(r.text, 'lxml')
        for result_number, head in enumerate(soup.find_all('h3'), start=1):
            # print(head.text)
            if result_number > 5:
                break
            try:
                a_tag = head.find_parent('a')

                link = a_tag['href']
                # print(link)
                output_for_one_question += str(result_number) + '. '
                output_for_one_question += head.text + '\n'
                output_for_one_question += link + '\n\n'
                output_for_one_question += '-' * 100 + '\n'
                print(output_for_one_question)
            except:
                continue

            output_for_all_questions += output_for_one_question

    return output_for_all_questions


print(get_search_results())