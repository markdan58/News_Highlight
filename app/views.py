from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting entertainment news
    entertainment_news = get_news('entertain')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,entertain = entertainment_news)




@app.route('/')
def articles():
    # Getting news source
    entertainment_news = get_news('entertain')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('articles.html', title = title,entertain = entertainment_news)

    