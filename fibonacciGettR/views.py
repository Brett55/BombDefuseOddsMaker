import models
# import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, Template
from django.utils.html import escape


def fib(n):
    seed_val_1, seed_val_2 = 1, 1
    for _ in xrange(n):
        yield seed_val_1
        seed_val_1, seed_val_2 = seed_val_2, seed_val_1 + seed_val_2


def main(request):
    return render_to_response('fibonacciGettR/index.html')


def calculate(request, n):
    result = list(fib(n))
    return HttpResponse("It worked!")

