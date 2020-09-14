from flask import render_template
from . import main
from ..request import get_source, get_article

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources_english = get_source('en')
    sources_strange = get_source('fr')

    print(sources_english)
    print(sources_strange)

    title = 'Home - Welcome to NewsHub'
    return render_template('index.html', title = title, en = sources_english, fr = sources_strange)



@main.route('/articles/<id>')
def article(id):

    '''
    View articles page function that returns the articles details page and its data
    '''

    title = 'Sources'
    article = get_article(id)
    print(article)
    return render_template('articles.html', title=title, article = article)
