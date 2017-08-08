import string
from collections import Counter
import re
 
def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str
def getInputFile (filename):
    f = open(filename, "r")
    
    
    bad = True
    while bad:
        try:
            
            f = open(filename, "r") # Note: "r" means open for reading.
            bad = False
        except Exception as err:
            print ("Please enter a valid file name:")
    return f    
 
def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str
 
def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt
 
def main(filename, topwords):
    txt = openfile(filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        print key,value

def count(filename):
    txt = openfile(filename)
    words = string.split(txt)
    word = len(words)   

def word_per_line(filename):
    Text = getInputFile(filename).readlines()
    lines=0
    wordCount=0
    for lineOfText in Text:
        lines += 1
       #print("line number:" +str(lines))
        f1=lineOfText.split()
        #print(f1)
        wordCount=wordCount+len(f1)
        print ("Word count:line" + ' ' +str(wordCount/lines) + ':' +str(lines)) 
count('data.txt')        
word_per_line('data.txt')        
main('data.txt', 10)
