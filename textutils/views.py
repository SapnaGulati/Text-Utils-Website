# Created by -- Dream Girl

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text 
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Removed Punctions', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed 

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":           
                analyzed += char
        params = {'purpose':'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose':'Removed extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed 

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on":
        analyzed = djtext
    
    if charcounter == "on":
        len = 0
        for char in djtext:
            if char == "\n" or char == "\r":
                continue
            len += char.count(char)
            print(len)
        params = {'purpose':'Total number of characters are: ', 'length': len, 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on":
        return HttpResponse("<pre><h3>So Sorry!!! You haven't choose any operation which can be performed on the text provided by you... \nSelect some operation to do and try again...</h3></pre>")

    return render(request, 'analyze.html', params)