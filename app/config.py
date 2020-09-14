class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language={}&apiKey={}'
    NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    # 29b2fc954c1f4a0984f179de7a14f202

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
