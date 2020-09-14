import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('NewsDaily', 'NewsDailyTrue', 'A big name in truth-seeking','www.newsdaily.net', 'finance')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))