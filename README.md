# Machine Problem: Web Scraping

### Requirements:

1. Your program needs to scrape all of the filenames, download links and filesizes in all of the inside pages of this page: http://mirror.rise.ph/centos/7/

2. Save the results in a CSV file with the following columns: filename,download_link,filesize

3. Create a new repository for this project named "centos7-scraper" and paste the link here for checking

### Prerequisites
1. Windows/Linux OS
2. Python 3

## The scraper.py script

The script consists of the Scraper class. Its method can be used to scrape the http://mirror.rise.ph/centos/7/ url recursively. The underlying url behind this url consist of files for the CentOS 7 repository.

### Usage
The script will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
```
$ python --version
```
Also, make sure that **pipenv** is installed as the main virtual environment manager for python projects.

#### Clone the repository
```
$ git clone https://github.com/rgbtrend/centos7-scraper.git
```

#### Create the environment
```
$ pipenv shell
```
#### Install dependencies
```
$ pipenv install
```

### Run the script and check the csv file:
```
$ python scraper.py
$ ls *.csv
file.csv
```
Note: The default csv file would be file.csv, but  on the script, it can be changed to anything.


