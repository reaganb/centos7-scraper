import unittest
import types
from scraper import Scraper


class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.scrape = Scraper()

    def test_scrape_file_url(self):
        rows = self.scrape.scrape_files_url('http://mirror.rise.ph/centos/7/atomic/x86_64/Packages/')
        self.assertIsInstance(rows, types.GeneratorType)

    def test_scrape_url(self):
        rows = self.scrape.scrape_url('http://mirror.rise.ph/centos/7/atomic/x86_64/Packages/')
        self.assertIsInstance(rows, types.GeneratorType)






