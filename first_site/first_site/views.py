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

        # punctuation
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analysed = ""

        if djtemovepunc == "on":
            for char in djtext:
                if char not in punctuations:
                    analysed = analysed + char
            params = {'purpose': 'Remove Punctuations', 'analysed_text': analysed}
        else:
            params = {'purpose': 'Remove Punctuations', 'analysed_text': djtext}
        return render(request, 'analyse.html', params)