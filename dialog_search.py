import re
def string_search(string,pattern,chapname):  ### function to match substring with any occurance of the substring in every paragraph of the book
    string=string.replace("\n"," ")
    x=re.findall("[\"“”](.*?)[\"“”]", string,re.S)  
    for i in x:  
        if pattern.lower() in i.lower():
            print(i)
            print(chapname) # prints the chapter name, that is being traversed

def dialog_search(a,b):      #### function to identify body of the chapter and update the chapter flag which stores the chapter being traversed
    #initialising variables
    dcont=set()   # set that stores the name of all the chapters under the content section of the book 
    found_content=1   # flag that saves the state of the running program
    match1=["CONTENTS","Contents"]    #string that identifies the title to find the content's section of the book
    match2=["chapter","CHAPTER"]      # one of the two types of format that is recognised by the program to understand a chapter title
    case=0;                       # stores the type of title format used by the given file

    f=open(a, mode='r+',encoding="utf8") #open a file object
    line=f.read()  #read the entire file as a single string
    line=line.split("\n\n")
    st=0
    for i in line:
        if(found_content==1):                               # program trying to search for the contents section
            for j in match1: #searches for the content 
                if j in i:
                    found_content=2
                    continue
        if (found_content==3):                              # program traversing each paragraph while updating chapter flag
            state=0
            if case==1:
                if (i in dcont): #done extracting the chapters from content
                    chap_flag=i
                else: st=1
            if case==2:
                g=re.search('.*(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})\..*',i)
                if g!=None:    
                    i=i.split(" ")
                    str_new=""
                    for j in i:
                        if (j==''):
                            continue
                        str_new+=(str(j.upper())+" ")
                    if (str_new) in dcont:
                        chap_flag=str_new
                else: st=1
            if st==1:
                string_search(i,b,chap_flag)
                st=0
        if (found_content==2):                              #  extracting the chapter names after identifying the contents section
            if(case==0 or case==1):
                if (i in dcont): #done extracting the chapters from content
                    chap_flag=i
                    found_content=3
                    continue
                for j in match2:
                    if j in i:
                        if case==0: case=1
                        i=i.split(" ")
                        if(i[1][-1]=='\n'):
                            i[1]=i[1][:-1]
                        lo="\n"+i[0]+" "+i[1]
                        if(i[0][0]=='\n'):
                            dcont.add(lo[1:])
                        else:
                            dcont.add(lo)
            if(case==0 or case==2):
                g=re.search('.*(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})\..*',i)
                if g!=None:    
                    case=2
                    i=i.split("\n")
                    for h in i:
                        h=h.split(" ")
                        str_new=""
                        for j in h:
                            if (j==''):
                                continue
                            str_new+=(str(j.upper())+" ")
                        if (str_new) in dcont:
                            chap_flag=str_new
                            found_content=3
                            continue
                        else:           dcont.add(str_new.upper())

#### taking inputs from the user (1) name of the file (2) substring to be searched               
file_in=input("Enter the name of the file to read from : ")
str_sub=input("Enter the substring to search :")
dialog_search(file_in,str_sub)
