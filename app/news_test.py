import unittest

from models import news

News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('NewsDaily', 'Vicky Rubadiri', 'A day in the life of a Haberdasher', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.', 'www.newsdaily.net', 'www.newsdaily.net/images/haber', '2020/9/11', 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()