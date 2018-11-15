import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1,'Danmark.com','Vodoo','Life With A Cat Is Full Of Adventures','A cat is full of adventures',"https://izismile.com/2018/11/09/life_with_a_cat_is_full_of_adventures_18_pics.html","https://img.izismile.com/img/img11/20181109/640/life_with_a_cat_is_full_of_adventures_640_18.jpg","2018-11-09T08:24:09Z","Processing. Please wait... We care about our visitors",
        "us",
        "en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main() 