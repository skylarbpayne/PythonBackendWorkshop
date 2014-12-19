from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

ideas = [
    {
        'author': 'Skylar',
        'idea': 'robot hands'
    },
    {
        'author': 'Rick',
        'idea': 'motorized hammer'
    },
    {
        'author': 'Laina',
        'idea': 'kitten incubator'
    }
]

@app.route('/')
def index():
    return render_template('index.html', ideas=ideas)

@app.route('/new', methods=['GET'])
def new_form():
    return render_template('new.html')

@app.route('/new', methods=['POST'])
def new_form_post():
    #Processing stuff
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
