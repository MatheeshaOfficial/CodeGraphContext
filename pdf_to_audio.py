
import pyttsx3
import PyPDF2

book = open("sample.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
speaker = pyttsx3.init()

for page in pdfReader.pages:
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

book.close()
