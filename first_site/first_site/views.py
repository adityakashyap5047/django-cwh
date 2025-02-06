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

    # punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''

    analysed = ""

    if djtemovepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Remove Punctuations', 'analysed_text': analysed}
    elif djfullcaps == "on":
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Upper Case', 'analysed_text': analysed}
    elif djnewlineremover == "on":
        for char in djtext:
            if char != '\n':
                analysed = analysed + char
        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
    elif djextraspaceremover == "on":
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        params = {'purpose': 'Remove Extra Space', 'analysed_text': analysed}
    else:
        params = {'purpose': 'Your text', 'analysed_text': djtext}
    return render(request, 'analyse.html', params)

