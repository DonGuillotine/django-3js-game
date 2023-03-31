from django.shortcuts import render
import random

def home(request):
    if request.method == 'POST':
        secret_number = request.session['secret_number']
        guess = int(request.POST['guess'])
        request.session['attempts'] += 1

        if guess == secret_number:
            message = 'Congratulations! You guessed the number in {} attempts.'.format(request.session['attempts'])
            request.session.flush()
            return render(request, 'results.html', {'message': message})
        elif guess < secret_number:
            message = 'The number is greater than {}'.format(guess)
        else:
            message = 'The number is smaller than {}'.format(guess)

        if request.session['attempts'] >= 10:
            message = 'Sorry! You have used all 10 attempts. The secret number was {}.'.format(secret_number)
            request.session.flush()
            return render(request, 'results.html', {'message': message})

        return render(request, 'index.html', {'message': message})
    else:
        secret_number = random.randint(0, 999)
        request.session['secret_number'] = secret_number
        request.session['attempts'] = 0
        return render(request, 'index.html')
