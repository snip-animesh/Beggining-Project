import pyttsx3
import PyPDF2
bn=input("kon boi porte chao?\n")
book=open(bn,'rb')                      #Je pdf ta porte chai seta open korlam.
speaker = pyttsx3.init()                #speaker hocche variable. init means start kora.
pdfReader=PyPDF2.PdfFileReader(book)    #book name er variable take porbe
pages=pdfReader.numPages                #kotogula page ase bole dibe
print("Boi e total page ase - ",pages)
x=int(input("Koto page theke porbo?\n"))
y=int(input("Koto page porjonto porbo?\n"))
print("Portesi . Shunte Thako .Good Luck.\n")

for i in range(x,y):
    page=pdfReader.getPage(i-1)           #je page porte chai seta bolte hobe
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
