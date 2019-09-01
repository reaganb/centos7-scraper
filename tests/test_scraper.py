import unittest
import types
from requests.exceptions import RequestException
from scraper.scraper import Scraper
from scraper.scraper import config_parser
from urllib.parse import urljoin

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scrape = Scraper()
        config = config_parser(file='../data/config_tests.ini')
        self.base_url = config['args']['url']

    def tearDown(self):
        pass

    def test_create_csv(self):
        self.assertTrue(self.scrape.create_csv())

    def test_get_url(self):
        url = urljoin(self.base_url,'centos/7/atomic/x86_64/Packages/')
        self.assertIsNotNone(self.scrape.get_url(url))

    def test_scrape_files_url(self):
        url = urljoin(self.base_url, 'centos/7/atomic/x86_64/Packages/')
        rows = self.scrape.scrape_files_url(url)

        self.assertIsNotNone(rows)
        self.assertIsInstance(rows, types.GeneratorType)

    def test_scrape_url(self):
        url = urljoin(self.base_url, 'centos/7/atomic/x86_64/Packages/')
        rows = self.scrape.scrape_url(url)

        self.assertIsNotNone(rows)
        self.assertIsInstance(rows, types.GeneratorType)

    def test_config_files(self):
        self.assertIsNotNone(config_parser('../data/config.ini'))
        self.assertIsNotNone(config_parser('../data/config_tests.ini'))

    def test_scrape_all_url(self):
        url = urljoin(self.base_url, 'centos/7/configmanagement/')
        self.assertIsNone(self.scrape.scrape_all_url(url))


if __name__ == '__main__':
    unittest.main()





