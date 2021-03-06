import urllib.request, json
from .models import Source, Article

api_key = None
base_url = None
base_url2 = None

def configure_request(app):
    global api_key, base_url, base_url2
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url2 = app.config['NEWS_API_BASE_URL2']

def get_source(language):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(language,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_sources = None

        if get_source_response['sources']:
            source_sources_list = get_source_response['sources']
            source_sources = process_sources(source_sources_list)

    return source_sources

def process_sources(source_list):
    '''
    Function  that processes the news sources and transforms them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain news sources

    Returns :
        source_sources: A list of news sources
    '''
    source_sources = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        source_object = Source(id,name,description,url,category)
        source_sources.append(source_object)

    return source_sources

def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    articles_sources_url = base_url2.format(id,api_key)

    with urllib.request.urlopen(articles_sources_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_articles = None

        if get_article_response['articles']:
            article_articles_list = get_article_response['articles']
            article_articles = process_articles(article_articles_list)

    return article_articles

def process_articles(article_list):
    '''
    Function  that processes the article results and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_articles: A list of article objects
    '''
    article_articles = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Article(id,name,author,title,description, url,urlToImage,publishedAt,content)
            article_articles.append(article_object)

    return article_articles