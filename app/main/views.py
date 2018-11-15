from flask import render_template, request,redirect,url_for
from . import main
from ..request import get_news
from . import main
from ..models import News 

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting entertainment news
    entertainment_news = get_news('entertain')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,entertain = entertainment_news)




@main.route('/')
def articles():
    # Getting news source
    entertainment_news = get_news('entertain')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('articles.html', title = title,entertain = entertainment_news)

    