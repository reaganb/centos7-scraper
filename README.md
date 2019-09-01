## The Web scraper project

The Scraper class of the scraper module have methods to recursively scrape for downloadable files from the http://mirror.rise.ph/ website. To be specific, this project can harvest all file information from the CentOS 7 repository in the website. 

### Usage
Check if Python 3 is installed in the system.
```
$ python --version
```
Also, make sure that **pipenv** is installed as the main virtual environment manager for python projects.

#### Clone the repository and checkout to this branch
```
$ git clone -b project-structure https://github.com/rgbtrend/centos7-scraper.git
```

### Run as One-Off script
#### Create the environment
```
$ pipenv shell
```

#### Install dependencies
```
$ pipenv update
```

#### Run
```
$ python scraper/scraper.py
$ ls *.csv
files.csv
```

### Run as Installable Single Package
#### Create the environment
```
$ pipenv shell
```

#### Install the package and its dependencies
```
$ pipenv install -e .
```

#### Run
```
$ python -m scraper
$ ls *.csv
files.csv
```

### Run the script and check the csv file:
```
$ python scraper.py
$ ls *.csv
file.csv
```

### Editing arguments
```
data
    -- config.ini
    --- config_tests.ini
```
```
[args]
url = http://mirror.rise.ph/centos/7/configmanagement/
csv = file.csv
```
At the data directory, you can change the input data for the script or test cases


