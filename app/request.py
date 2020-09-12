from app import app
import urllib.request, json
from .models import source

Source = source.Source


api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_BASE_URL']

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