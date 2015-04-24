import models
import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils.html import escape


def fib(n, seed_val_1, seed_val_2):
    '''return index of nth position in fibonacci sequence'''

    seed_val_1 = int(seed_val_1)
    seed_val_2 = int(seed_val_2)

    for _ in xrange(int(n)):
        yield seed_val_1
        seed_val_1, seed_val_2 = seed_val_2, seed_val_1 + seed_val_2


def main(request):
    '''main landing page with previous submissions'''
    args = {}
    args.update(csrf(request))
    args['fib_submissions'] = models.Fibonacci.objects.all()
    return render_to_response('fibonacciGettR/index.html', args)


def calculate(request, n, seed_val_1, seed_val_2):
    '''calculate API, send input to fib function and render result to client'''

    if request.method == 'POST':
        result = list(fib(escape(n), escape(seed_val_1), escape(seed_val_2)))[-1]
        form_main = forms.Fibonacci(request.POST)
        if form_main.valid():
            cleaned_data = form_main.cleaned_data
            new_fibonacci = models.Fibonacci()
            new_fibonacci.user_input = cleaned_data['user_input']
            new_fibonacci.result = cleaned_data['result']
            new_fibonacci.save()
            return HttpResponse(result)
        else:
            return HttpResponse(form_main.errors)

    else:
        HttpResponse("Error: Wrong REST Endpoint")



