from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Harry','place':'mars'}
    return render(request,'index.html',params) # using template



def analyze(request):
    #get the text
    djtext=(request.POST.get('text',"default"))
    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    newlineremover=(request.POST.get('newlineremover','off'))
    extraspaceremover=(request.POST.get('extraspaceremover','off'))
    print(djtext)
    print(removepunc)
    if removepunc=="on":
        #analyse the text
        Punctiuations ='''/[-[\]{}()*+?.,:@#'"<>^$|#\s]$&;'''
        analyzed=" "
        for char in  djtext:
            if char not in Punctiuations:
                analyzed=analyzed+ char

        params={'purpose':'Remove Punctiuations ','analyze_text':analyzed}
        djtext=analyzed
        #return  render(request,'analyze.html', params) 
    if(fullcaps=="on"):
        analyzed=" "
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to uppercase ','analyze_text':analyzed}
        djtext=analyzed
       # return  render(request,'analyze.html', params)
    if(newlineremover=="on"):
        analyzed=" "
        for char in djtext:
            if char !="\n" and char!='\r':
                 analyzed=analyzed+char
        params={'purpose':'Remove new lines ','analyze_text':analyzed}
        djtext=analyzed
       # return  render(request,'analyze.html', params) 
    elif(extraspaceremover=="on"):
        analyzed=" "
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]== " "):
                analyzed=analyzed+char
        params={'purpose':'Ertra Space Remover','analyze_text':analyzed}
        djtext=analyzed
        
    if(removepunc!="on" and fullcaps!="on"and newlineremover!= "on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation and try again")
        
    return  render(request,'analyze.html', params)
    
       # return HttpResponse("Error")
# def analyze(request):
#     #get the text
#     djtext=(request.GET.get('text',default))
#     removepunc=(request.GET.get('removepunc','off'))
#     print(djtext)
#     print(removepunc)
#     #analyse the text
#     return  HttpResponse("my name is Er bheeekha ram")  #using HttpResponse
# Punctuation Marks  ?…!.,—––:;“‘[ ]( )

# PUNCTUATION =  /[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&";


def myapp(request):
    return render(request,'myapp.html')

def about(request):
    return render(request,'about.html')