import re
def dialog(a):  
    f=open(a, mode='r',encoding="utf8") #open a file object
    line=f.read()  #read the entire file as a single string
    line=line.split("\n\n") #split the file into paragraphs to remove para that start with a quote and left unquoted
    f1 = open("Dialog_"+a, "w") #creates output file object - dialog_<name of original file>
    for il in line:    #for every paragraph
        x=re.findall("[\"“”](.*?)[\"“”]", il,re.S)  #search for string with dumb and smart quotes
        for i in x:  #for every dialogue, format it into output file appropriately
            i=i.replace('\n'," ")
            i=i.replace("    "," ")
            f1.write("\""+i+"\"\n")

file_in=input("Enter the name of the file to read from : ")
dialog(file_in)  #calling the dialog extracting function