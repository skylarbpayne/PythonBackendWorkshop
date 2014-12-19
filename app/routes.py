from flask import Flask
from flask import render_template

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

if __name__ == "__main__":
    app.run(debug=True)
