import PyPDF2

subjects = ['CS', 'English', 'Maths', 'Physics']
for subject in subjects:
    reader = PyPDF2.PdfFileReader(subject + ".pdf")
    pages = reader.getNumPages()

    for i in range(pages):
        page = reader.getPage(i)

        text = page.extractText()

        with open(subject + "---text.txt", 'a') as out:
            out.write(text)
print("Done!")