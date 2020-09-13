from app import app
import urllib.request, json
from .models import source

Source = source.Source


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

# def get_selected_source(id):
#     get_source_details_url = base_url2.format(id,api_key)

#     with urllib.request.urlopen(get_source_details_url) as url:
#         selected_source_details_data = url.read()
#         selected_source_details_response = json.loads(selected_source_details_data)

#         source_object = None
#         if selected_source_details_response:
#             id = selected_source_details_response.get('id')
#             name = selected_source_details_response.get('name')
#             author = selected_source_details_response.get('author')
#             title = selected_source_details_response.get('title')
#             description = selected_source_details_response.get('description')
#             url = selected_source_details_response.get('url')
#             urlToImage = selected_source_details_response.get('urlToImage')
#             publishedAt = selected_source_details_response.get('publishedAt')
#             content = selected_source_details_response.get('content')

#             source_object = Source(id,name,author,title,description,url,urlToImage, publishedAt,content)

#     return source_object
    