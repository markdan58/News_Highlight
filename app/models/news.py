class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content,category,country,language):
        self.source =source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.category = category
        self.country = country
        self.language = language


class source:
    '''
    news source class

    '''
    
    def __init__(self,source,category,country,language):
         self.source = source
         self. category = category
         self. country = country
         self. language = language       
