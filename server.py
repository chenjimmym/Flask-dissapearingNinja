from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('index.html')
@app.route('/ninja/')
def ninjaPage():
    return render_template('ninja.html')
@app.route('/ninja/<color>')
def ninjaColorPage(color):
    if color == 'blue':
        return render_template('blue.html')
    elif color == 'orange':
        return render_template('orange.html')
    elif color == 'red':
        return render_template('red.html')
    elif color == 'purple':
        return render_template('purple.html')
    else:
        return render_template('notapril.html')

app.run(debug=True)