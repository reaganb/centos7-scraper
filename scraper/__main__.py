from .scraper import Scraper


if __name__ == "__main__":
    # The start of the script.

    # Instantiating the scraper object from the Scaper class. Indicating a explicit csv file name.
    scraper = Scraper(csv_file='subdir.csv')

    # Running the method of the object for recursive scraping. It needs a valid url from the CentOS 7 repository
    # from the http://mirror.rise.ph website.
    scraper.scrape_all_url(
        # url='http://mirror.rise.ph/centos/7/'
        url='http://mirror.rise.ph/centos/7/configmanagement/'
        # url='http://mirror.rise.ph/centos/7/atomic/x86_64/adb/'
    )