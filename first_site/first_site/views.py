# # I have created this file  - Aditya Kumar

from django.http import HttpResponse
from django.shortcuts import render

# Starting with the django
    # def index(request):
    #     return HttpResponse("Hello from 1st site")

    # def about(request):
    #     return HttpResponse("<h1>Hello from About</h1>")

# Laying the pipeline
    # def index(request):
    #     return HttpResponse("Home")

    # def  removepunc(request):
    #     return HttpResponse("remove punc <a href='/'>back</a>")

    # def capfirst(request):
    #     return HttpResponse("Capatalize first <a href='/'>back</a>")

# Templates
def index(request):
    params = {'name': 'Adam', 'place': 'Titan'}
    return render(request, 'index.html', params)

def text_analyse(request):
    return render(request, 'text.html')

def  analyse(request):
    # access the data
    djtext = request.POST.get('text', 'default')
    djremovepunc = request.POST.get('removepunc', 'off')
    djfullcaps = request.POST.get('fullcaps', 'off')
    djnewlineremover = request.POST.get('newlineremover', 'off')
    djextraspaceremover = request.POST.get('extraspaceremover', 'off')
    djcharcount = request.POST.get('charcount', 'off')

    # punctuation
    punctuations = '''!()-[]{};:'",<>.\/?@#$%^&*_~`'''

    params = {'purpose': 'Your text', 'analysed_text': djtext}
    purpose = ""

    if djremovepunc == "on":
        if purpose != "":
            purpose = purpose + " & " + 'Remove Punctuations'
        else:
            purpose = 'Remove Punctuations'
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        djtext = analysed
        params = {'purpose': purpose, 'analysed_text': analysed}
    if djfullcaps == "on":
        if purpose != "":
            purpose = purpose + " & " + 'Upper Case'
        else:
            purpose = 'Upper Case'
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        djtext = analysed
        params = {'purpose': purpose, 'analysed_text': analysed}
    if djnewlineremover == "on":
        if purpose != "":   
            purpose = purpose + " & " + 'Remove NewLines'
        else:
            purpose = 'Remove NewLines'
        analysed = ""
        for char in djtext:
            # To detect a new line, we must also consider the carriage return (\r).
            # In network communication, both newline characters (\n) and carriage returns (\r) are used for data transmission.
            if char != '\n' and char != '\r':
                analysed = analysed + char
        djtext = analysed
        params = {'purpose': purpose, 'analysed_text': analysed}
    if djextraspaceremover == "on":
        if purpose != "":
            purpose = purpose + " & " + 'Remove Extra Space'
        else:
            purpose = 'Remove Extra Space'
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        djtext = analysed
        params = {'purpose': purpose, 'analysed_text': analysed}
    if djcharcount == "on":
        if purpose != "":
            purpose = purpose + " & " + 'Count Character'
        else:
            purpose = 'Count Character'
        params = {'purpose': purpose, 'analysed_text': f"{djtext} <--> LENGTH - {len(djtext)}"}
    return render(request, 'analyse.html', params)

