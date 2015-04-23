import models
# import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils.html import escape


def fib(n):
    '''return index of nth position in fibonacci sequence'''

    seed_val_1, seed_val_2 = 1, 1
    for _ in xrange(int(n)):
        yield seed_val_1
        seed_val_1, seed_val_2 = seed_val_2, seed_val_1 + seed_val_2


def main(request):
    '''main landing page'''

    return render_to_response('fibonacciGettR/index.html')


def calculate(request, n):
    '''calculate API, send input to fib function and render result to client'''

    result = list(fib(escape(n)))[-1]
    return HttpResponse(result)

