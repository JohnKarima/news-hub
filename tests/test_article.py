import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('NewsDaily', 'NewsDailyTrue','Larry Madowo', 'Hummus...thoughts?','Literally talking about hummus sir','www.newsdaily.net','www.newsdaily.net/picOfHummus6', '2020/2/3', 'lorem gang et all')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
