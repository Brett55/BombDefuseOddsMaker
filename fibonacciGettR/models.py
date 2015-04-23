from django.db import models


class Fibonacci(models.Model):
    user_input = models.BigIntegerField('User Input', null=False, blank=False)
    result = models.BigIntegerField('Result', null=False, blank=False)

