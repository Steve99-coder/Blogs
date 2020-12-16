import unittest
from app.models import Blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog("Sports","Business","European Union assessments of whether to grant market access for banks","https://www.bbc.com/news/business","https://media.wired.com/photos/5fac6afb446b4639b3d5b8d8/191:100/w_1280,c_limit/Security-Microsoft-1229426260.jpg","2020-11-12T14:00:00Z",)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
