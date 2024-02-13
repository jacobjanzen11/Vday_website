#######################################################
#
# Purpose: Handles main flask program for website
# Website: 
# Author: Jacob Janzen
# Last Updated: 12/10/2020
#
#######################################################

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this to a secure secret key

valid_user = {'name': 'Kiannah', 'valid_answers': ['Jacob', 'jacob', 'jacob janzen', 'Jacob Janzen', 'Boyfriend', 'boyfriend']}


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        answer = request.form.get('answer')

        if answer.lower() == 'yes': # and valid_user['name'].lower() == 'jacob'
            # Redirect to the security question page
            return redirect(url_for('security_question'))

        else:
            return render_template('get_out.html')

    return render_template('login.html', error=error)


@app.route('/security_question', methods=['GET', 'POST'])
def security_question():
    error = None

    if request.method == 'POST':
        security_answer = request.form.get('security_answer')

        if security_answer.lower() in valid_user['valid_answers']:
            return redirect(url_for('index'))

        else:
            return render_template('try_again.html')

    return render_template('security_question.html', error=error)


@app.route('/valentine')
def valentine():
    return render_template('valentine.html')


@app.route('/no_valentine')
def no_valentine():
    return render_template('no_valentine.html')


if __name__ == '__main__':
    app.run(debug=True)