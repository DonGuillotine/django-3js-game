from django.shortcuts import render
import random

def home(request):
    # Check for POST request
    if request.method == 'POST':
        # Add Secret number to Session
        secret_number = request.session['secret_number']
        # Get the guess and convert to integer
        guess = int(request.POST['guess'])
        # Increase by 1
        request.session['attempts'] += 1

        # If the user answers correctly
        if guess == secret_number:
            message = 'Congratulations! You guessed the number in {} attempts.'.format(request.session['attempts'])
            request.session.flush()
            return render(request, 'results.html', {'message': message})
        
        # Else if the guess is greater
        elif guess < secret_number:
            message = 'The number is greater than {}'.format(guess)
        else:
            message = 'The number is smaller than {}'.format(guess)

        # Checking if attempts are used up
        if request.session['attempts'] >= 10:
            message = 'Sorry! You have used all 10 attempts. The secret number was {}.'.format(secret_number)
            request.session.flush()
            return render(request, 'results.html', {'message': message})

        return render(request, 'index.html', {'message': message})
    else:
        # At the onset this executes
        # Generate random number from 0 - 999
        secret_number = random.randint(0, 999)
        request.session['secret_number'] = secret_number
        request.session['attempts'] = 0
        return render(request, 'index.html')
