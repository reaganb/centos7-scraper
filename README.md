## The Web Scraper project

The Scraper class of the scraper module have methods to recursively scrape for downloadable files from the http://mirror.rise.ph/ website. To be specific, this project can harvest all file information from the CentOS 7 repository in the website. 

### Usage
#### Requirements check
Check if Python 3 is installed in the system.
```
$ python --version
```
Also, make sure that **pipenv** is installed as the main virtual environment manager for python projects.
```
$ pipenv --version
```
#### Clone the repository and checkout to this branch
```
$ git clone -b write-to-db https://github.com/rgbtrend/centos7-scraper.git
```

#### Create the environment
```
$ pipenv shell
```

#### Install dependencies
```
$ pipenv update
```

#### Run the scraper
On the top level directory, run the following to test the script. It has two options: database or csv writing

```
$ python -m scraper
$ ls *.csv
files.csv
```

#### Run the unit tests
```
$ pytest --cov=scraper tests/
```
The ```--cov``` option pertains to the target project and second argument for the module of the tests files.
It uses the pytest library to run these tests.

### Editing arguments
```
data
    -- config.ini
    --- config_tests.ini
    ---
```
```
[args]
url = http://mirror.rise.ph/centos/7/configmanagement/
csv = file.csv
```
At the data directory, you can change the input data for the script or test cases


