from flask import render_template
from app import app
from .request import get_source

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources_english = get_source('en')
    print(sources_english)
    title = 'Home - Welcome to NewsHub; Global news at your fingertips'
    return render_template('index.html', title = title, en = sources_english)
