from django.forms import ModelForm
import models


class Fibonacci(ModelForm):
    class Meta:
        model = models.Fibonacci
        fields = ('user_input',)