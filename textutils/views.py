# I have created this file- Anu
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #params ={'name': 'Anu', 'place': 'Ranchi'}
    return render(request,'index.html')
   # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineRemover = request.POST.get('newlineRemover', 'off')
    ExtraspaceRemover = request.POST.get('ExtraspaceRemover', 'off')

    # Check which checkbox in on
    if removepunc == "on":
        #analyzed = djtext

        punctuations = '''!()-[]{};:'"\,<>.?@#$%^&*/_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if fullcaps =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineRemover =="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if ExtraspaceRemover =="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]== " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text
    if(removepunc != "on" and newlineRemover!="on" and ExtraspaceRemover!="on" and fullcaps!="on"):
        return  HttpResponse("Error")

    return render(request, 'analyze.html', params)


