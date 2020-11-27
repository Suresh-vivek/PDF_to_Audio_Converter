#import library
import pyttsx3
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw()
filename=askopenfilename()
print(filename)

#Code to open book
book=open(filename,'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print("Number of Pages :")
print(pages)

#Taking user's Inputs
start= int(input("Starting page Number.."))
end= int(input("Ending Page Number.."))

#Intializing Speaker
speaker= pyttsx3.init()


for num in range(start-1,end):



    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
