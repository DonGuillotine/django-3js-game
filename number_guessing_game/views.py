from django.shortcuts import render
from random import randint


def index(request):
    number = randint(0, 999)
    attempts = 0
    max_attempts = 10
    hint_text = ""


    if request.method == 'POST':
        guess = int(request.POST['guess'])