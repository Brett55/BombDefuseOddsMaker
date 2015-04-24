import models
import forms
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
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

    return render_to_response('fibonacciGettR/index.html')


def calculate(request, n, seed_val_1=1, seed_val_2=1):
    '''calculate API, send input to fib function and render result to client'''

    if request.method == 'GET':
        if check_input(n):
            start_time = time.time()
            result = list(fib(escape(n), escape(seed_val_1), escape(seed_val_2)))[-1]
            end_time = round(time.time() - start_time, 4)
            return HttpResponse("Result: " + str(result) + " Finished in " + str(end_time))
        else:
            return HttpResponse("Input too large!")

    else:
        HttpResponseBadRequest('<h1>Page not found</h1>')


def calculate_and_save(request):
    '''calculate API, send input to fib function and render result to client'''

    if request.method == 'POST':
        form_main = forms.Fibonacci(request.POST)
        if form_main.valid():
            cleaned_data = form_main.cleaned_data
            new_fibonacci = models.Fibonacci()
            if check_input(cleaned_data['user_input']):
                new_fibonacci.user_input = cleaned_data['user_input']
                start_time = time.time()

                # check value is within range and process
                result = list(fib(int(escape(cleaned_data['user_input']))))[-1]

                end_time = round(time.time() - start_time, 4)
                new_fibonacci.result = result
                new_fibonacci.save()
                return HttpResponse("Result: " + str(result) + " Finished in " + str(end_time))
            else:
                return HttpResponse("Input too large!")
        else:
            return HttpResponse(form_main.errors)

    else:
        HttpResponseBadRequest('<h1>Page not found</h1>')


def check_input(n):
    return int(n) < 9999



