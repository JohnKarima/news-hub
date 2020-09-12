from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    africa_news = get_news('africa')
    us_news = get_news('us')
    uk_news = get_news('uk')


    print(africa_news)
    title = 'Home - Welcome to NewsHub; Global news at your fingertips'
    return render_template('index.html', title = title, africa = africa_news, us = us_news, uk = uk_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)