from urllib.parse import urljoin
import configparser
import argparse
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
import os.path as op
import csv
import re
from sqlalchemy.orm import sessionmaker
import sys

# print(sys.path)
from models.models import File, init_database


# from models import models

class Scraper:

    def __init__(self, csv_file="file.csv", write_to_db=False):
        """
        The __init__ or the constructor method. Everything under here will be run every time
        another object is instantiated from this class. The csv file will be created immediately
        for every object creation.
        Argument:
             csv_file -- This is the filename of the csv file. By default, its name is "file.csv"
                        when there is no explicit assignment upon object creation.
        """

        self.csv_file = op.abspath(csv_file)
        self.urls_set_global = set()



        self.session = None

        if write_to_db:
            engine = init_database()
            self.session = sessionmaker(bind=engine)
            pass

        self.create_csv()

    def create_csv(self):
        with open(self.csv_file, 'w') as file:
            file.write("file_name,download_link,file_size\n")
        return op.isfile(self.csv_file)

    def get_url(self, url):
        """
        The class method that implements the requests get() method with additional error
        handling.

        Argument:
            url -- the url to get() request for

        return -- The response object or None
        """
        try:
            response = get(url)
            if response.status_code == 200:
                return response
            else:
                raise RequestException('There is an error in the exception!')
        except RequestException as e:
            return None

    def write_to_csv(self, url):
        """
        Once called, this method will call the scrape_files_url() method to harvest all the downloadable file links
        based from the url argument. It will then write those links together with its information to the csv file
        indicated upon object instantiation.
        Argument:
            url -- the url where there are downloadable files url
        """
        rows = self.scrape_files_url(url)

        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
            for line in rows:
                row = File(line[0], line[1], line[2])
                self.session.add(row)
                self.session.commit()
                self.session.close()
                writer.writerow(line)

        return op.isfile(self.csv_file)

    def scrape_all_url(self, url):
        """
        A method to recursively look for url that consist of downloadable files.
        It will first check if the url is from the CentOS 7 repository then uses that url as the root node.
        It uses a special algorithm for traversing n-ary trees called pre-order traversal.
        Argument:
            url -- the url for recursively scraping
        """
        rise_website = 'http://mirror.rise.ph/'
        try:
            if rise_website in url:
                for url_ in self.scrape_url(url.strip()):
                    self.scrape_all_url(url_.strip())
            else:
                raise ValueError("Not the Rise website!")
        except ValueError as e:
            print(e)
            return e

    def scrape_url(self, url):
        """
        This is the method for scraping a url and look for another url that points to another page where
        there are downloadable files. It will yield a set containing the harvested collection
        of url.
        Argument:
            url -- the url for scraping
        yield -- set of url
        """

        response = self.get_url(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')

        urls_set = set()

        for attr in soup.find('table').find_all('a'):
            link = attr.get('href')
            match = re.match(r'[^\/]+[\/]$', link)
            if match and not match.group().startswith('/'):
                if urljoin(url, link) not in self.urls_set_global:
                    self.write_to_csv(urljoin(url, link))
                self.urls_set_global.add(urljoin(url, link))
                urls_set.add(urljoin(url, link))

        yield from urls_set

    def scrape_files_url(self, url):
        """
        The method to call for scraping all the files from a url

        Argument:
            url - the downloadable file url

        return -- the return data of the scrape_page method
        """

        response = self.get_url(url)
        data = response.text

        rows = self.scrape_page(url, data)

        return rows

    def scrape_page(self, url, data):
        """
        Accepting a single argument data which is a get response text, this method consist of inner methods to help format the text line
        to be written to the csv file. It also has a get request method that needs the url for downloadable files.
        Argument:
            url - the downloadable file url
        return -- A tuple of lists. Each list contain the file information
        """

        soup = BeautifulSoup(data, 'html.parser')
        trow = (x for x in soup.find('table').findAll('tr'))

        def row(tr):
            """
            The inner function to find all the table data from the soup object
            Argument:
                tr -- the table row that consist of a list of table data
            return -- a list of table data
            """
            return tr.findAll('td')

        def row_condition(row_args):
            """
            Another inner function for condition for each table rows if it has the table data
            containing the downloadable file link.
            Argument:
                row_args -- The list of table data
            return -- True or None
            """
            if len(row_args) == 4:
                if "-" not in row_args[-1].text:
                    return True

        def row_metadata(row_):
            """
            The last innner function that will format the file information into a list. The sequence of order
            is as follows: file_name, download_link, and file_size.
            Argument:
                row_ - The list of table data
            return -- line (the ordered list)
            """
            file_name = row_[1].text
            download_link = urljoin(url, row_[1].find('a').get('href'))
            file_size = row_[-1].text.strip()
            line = [file_name, download_link, file_size]

            return line

        rows = (row_metadata(row(tr))
                for tr in trow if row_condition(row(tr)))

        return rows


def main():
    """
    The start of the script.
    """
    parser = argparse.ArgumentParser()
    config = config_parser(file='../data/config.ini')
    csv_config = config['args']['csv']
    url_config = config['args']['url']

    parser.add_argument('-db', dest='write_to_db', action='store_true')

    args = parser.parse_args()

    # Instantiating the scraper object from the Scaper class. Indicating a explicit csv file name.
    scraper = Scraper(csv_file=csv_config, write_to_db=args.write_to_db)

    # Running the method of the object for recursive scraping. It needs a valid url from the CentOS 7 repository
    # from the http://mirror.rise.ph website.

    scraper.scrape_all_url(
        # url='http://mirror.rise.ph/centos/7/'
        url=url_config
        # url='http://mirror.rise.ph/centos/7/atomic/x86_64/adb/'
    )


def config_parser(file):
    config_file = op.join(op.dirname(op.abspath(__file__)), file)
    if op.isfile(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    else:
        return None


if __name__ == "__main__":
    main()
