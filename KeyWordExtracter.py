# Keyword extractor


import PyPDF2
import textract
import pandas as pd
from gensim.summarization import keywords

filename ='JavaBasics.pdf' 

file = open(filename,'rb')              
reader = PyPDF2.PdfFileReader(file)  
pages = reader.numPages                 
text = ""
                                                        
for i in range(0,pages):                      
    page =  reader.getPage(i)
    text += page.extractText()
    
if text != "":
    text = text
else:
    text = textract.process('http://bit.ly/epo_keyword_extraction_document',
           
                            method='tesseract', language='eng')

text = text.lower() 
values = keywords(text=text,split='\n',scores=True ,lemmatize = True)
data = pd.DataFrame(values,columns=['keyword','score'])
data = data.sort_values('score',ascending=False)
data.to_csv('Extracted_Words.csv')


