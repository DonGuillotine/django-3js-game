import random
from django.shortcuts import render, redirect
from .models import Game
from random import randint


def game_view(request):
    # Checking for a POST request
    if request.method == 'POST':

        # Get the guess from the user
        guess = int(request.POST['guess'])

        # Get the first item in the Game Model
        game = Game.objects.first()

        # Increase the attempts by one
        game.attempts += 1

        # Condition for a successful guess
        if guess == game.number:
            message = f'Congratulations! You guessed the number in {game.attempts} attempts.'
            return render(request, 'result.html', {'message': message})
        
        # Condition for a higher guess
        elif guess < game.number:
            message = 'The number is greater than your guess. Try again!'

        # Condition for a smaller guess
        else:
            message = 'The number is smaller than your guess. Try again!'

        # Condition for 10 Limits
        if game.attempts >= 10:
            message = f'Sorry, you lost! The number was {game.number}.'
            return render(request, 'result.html', {'message': message})
        # Save to database
        game.save()
        # Render to index.html
        return render(request, 'index.html', {'message': message})  
    else:
        game = Game.objects.create(number=random.randint(0, 999))
        return render(request, 'index.html')