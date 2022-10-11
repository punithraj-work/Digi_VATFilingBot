# importing all the required modules
from PyPDF2 import PdfFileReader as PdfReader

# creating an object 
reader = PdfReader("example.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open("test.txt", "w") as f:
        data = f.write(text)

# print(text)

#install using: pip install PyMuPDF
import fitz 

with fitz.open("example.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

with open("test.txt", "w") as f:
        data = f.write(text)

print(text)