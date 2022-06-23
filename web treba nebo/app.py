from flask import Flask, render_template, request
import random
from win_function import is_win

app = Flask(__name__)

@app.route('/gaykarol', methods = ['post'])
def gaykarol():
    data = request.form
    userinput = data['button']
    print (userinput)
    computer = random.choice(['rock', 'paper', 'scissors'])
    if computer == userinput:
        return render_template('index.html', userinput = f'It is a tie, you both chose {computer}')

    if is_win(userinput, computer):
        return render_template('index.html', userinput = f'You won! The computer chose {computer} and you chose {userinput}')
    else:
        return render_template('index.html', userinput = f'You lost! The computer chose {computer} and you chose {userinput} ')

    return render_template('index.html', userinput = userinput)


@app.route('/gaykarol')
def gaykarol2():
    return render_template('index.html')

