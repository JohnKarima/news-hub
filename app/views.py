from flask import render_template
from app import app
from .request import get_source, get_article

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources_english = get_source('en')
    sources_strange = get_source('fr')

    print(sources_english)
    print(sources_strange)

    title = 'Home - Welcome to NewsHub; Global news at your fingertips'
    return render_template('index.html', title = title, en = sources_english, fr = sources_strange)



@app.route('/articles/<id>')
def article(id):

    '''
    View articles page function that returns the articles details page and its data
    '''

    article = get_article(id)
    print(article)
    return render_template('articles.html',article = article)

    #title = f'{article.title}'
    #print(article_cool)
    #articles_cool = get_article('id')
    #print(articles_cool)


    
    # title = 'yoooh brooooo - Welcome to NewsHub; Global news at your fingertips'





    # articles_cool = get_article('bloomberg')
    # print(articles_cool)

    
    # title = f'{articles.name}'
    # title = 'not home - Welcome to NewsHub; Global news at your fingertips'

    # return render_template('index.html',title = title, cnn = articles_cool)

    # bloomberg_articles = get_article('bloomberg')
    # print(bloomberg_articles)

    # title = 'Articles'