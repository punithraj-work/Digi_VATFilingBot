#install using: pip install PyMuPDF, alternatively
import fitz 

def readpdf():
    #Program to read pdf and get the data in it and save in textfile
    with fitz.open("./PDF/example.pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    with open("test.txt", "w") as f:
        data = f.write(text)


    with open(r"test.txt", 'r') as fp:
        lines = sum(1 for line in fp)
        print('Total Number of lines:', lines)

    # print(text)
    
    
    # Open and read file into buffer
    f = open("test.txt","r")
    lines = f.readlines()
    
    # If we need to read line 33, and assign it to some variable
#     x = lines[14]
#     print(x)
    return lines