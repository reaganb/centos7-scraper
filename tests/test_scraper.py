import unittest
import types
from scraper.scraper import Scraper
from scraper.scraper import config_parser
from urllib.parse import urljoin


class TestScraper(unittest.TestCase):

    def setUp(self):
        """
        The unittest setUP method where instance attributes can be initialized
        """

        self.scrape = Scraper()
        config = config_parser(file='../data/config_tests.ini')
        self.base_url = config['args']['url']

    def test_create_csv(self):
        """
        Testing the create_csv method from the Scraper class
        """

        self.assertTrue(self.scrape.create_csv())

    def test_get_url(self):
        """
        Testing the get_url method from the Scraper class
        """

        url = urljoin(self.base_url,'centos/7/atomic/x86_64/Packages/')
        self.assertIsNotNone(self.scrape.get_url(url))
        url2 = urljoin(self.base_url, 'centos/7/atomic/x86_644/Packages/')
        self.assertIsNot(int,self.scrape.get_url(url2))

    def test_scrape_files_url(self):
        """
        Testing the scrape_files_url method from the Scraper class
        """

        url = urljoin(self.base_url, 'centos/7/atomic/x86_64/Packages/')
        rows = self.scrape.scrape_files_url(url)

        self.assertIsNotNone(rows)
        self.assertIsInstance(rows, types.GeneratorType)

    def test_scrape_url(self):
        """
        Testing the scrape_url method from the Scraper class
        """

        url = urljoin(self.base_url, 'centos/7/atomic/x86_64/Packages/')
        rows = self.scrape.scrape_url(url)

        self.assertIsNotNone(rows)
        self.assertIsInstance(rows, types.GeneratorType)

    def test_scrape_all_url(self):
        """
        Testing the scrape_all_url method from the Scraper class
        """

        url = urljoin(self.base_url, 'centos/7/configmanagement/')
        self.assertIsNone(self.scrape.scrape_all_url(url))
        wrong_url = 'https://wrong.web.site/centos/7/configmanagement/'
        self.assertIsNotNone(self.scrape.scrape_all_url(wrong_url))

    def test_config_files(self):
        """
        Testing the config_files function from the scraper module
        """

        self.assertIsNotNone(config_parser('../data/config.ini'))
        self.assertIsNotNone(config_parser('../data/config_tests.ini'))

        self.assertIsNone(config_parser('../data/config_tests.iniii'))

    def test_db(self):
        """
        Testing the database methods and functions
        """

        db_cred = {
            'host': 'localhost',
            'user': 'postgres',
            'password': 'wrongpassword'
        }

        scrape = Scraper(db=True, db_cred=db_cred)
        # def __init__(self, csv_file="file.csv", db=False, db_cred=None):
        url = 'http://mirror.rise.ph/centos/7/atomic/x86_64/Packages/'

        with self.assertRaises(AttributeError):
            scrape.write_to_db(url=url)

    def test_run_scrapper(self):
        """
        Testing the run_scraper method from the Scraper class
        """

        url = urljoin(self.base_url, 'centos/7/configmanagement/')
        self.assertIsNone(self.scrape.run_scraper(url))
        wrong_url = 'https://wrong.web.site/centos/7/configmanagement/'
        self.assertIsNotNone(self.scrape.run_scraper(wrong_url))



if __name__ == '__main__':
    # The main runner of the unittest
    unittest.main()





