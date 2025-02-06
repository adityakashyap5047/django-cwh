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
    djtext = request.GET.get('text', 'default')
    djtemovepunc = request.GET.get('removepunc', 'off')
    djfullcaps = request.GET.get('fullcaps', 'off')
    djnewlineremover = request.GET.get('newlineremover', 'off')
    djextraspaceremover = request.GET.get('extraspaceremover', 'off')
    djcharcount = request.GET.get('charcount', 'off')

    # punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''

    params = {'purpose': 'Your text', 'analysed_text': djtext}

    if djtemovepunc == "on":
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        djtext = analysed
        params = {'purpose': 'Remove Punctuations', 'analysed_text': analysed}
    if djfullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        djtext = analysed
        params = {'purpose': 'Upper Case', 'analysed_text': analysed}
    if djnewlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != '\n':
                analysed = analysed + char
        djtext = analysed
        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
    if djextraspaceremover == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        djtext = analysed
        params = {'purpose': 'Remove Extra Space', 'analysed_text': analysed}
    if djcharcount == "on":
        params = {'purpose': 'Count Character', 'analysed_text': f"{djtext} -- LENGTH - {len(djtext)}"}
    return render(request, 'analyse.html', params)

