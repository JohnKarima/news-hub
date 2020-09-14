class Source:
    '''
    Sources class to define news sources objects
    '''

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        

class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,name,author,title,description,url, urlToImage, publishedAt, content):
        self.id =id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content