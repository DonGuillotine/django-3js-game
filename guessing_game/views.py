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

        if guess == game.number:
            message = f'Congratulations! You guessed the number in {game.attempts} attempts.'
            return render(request, 'result.html', {'message': message})
        
        elif guess < game.number:
            message = 'The number is greater than your guess. Try again!'

        else:
            message = 'The number is smaller than your guess. Try again!'

        game.save()
        return render(request, 'game.html', {'message': message})
    
    else:
        game = Game.objects.create(number=random.randint(0, 999))
        return render(request, 'game.html')