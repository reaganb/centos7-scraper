## The Web scraper project

The Scraper class of the scraper module have methods to recursively scrape for downloadable files from the http://mirror.rise.ph/ website. To be specific, this project can harvest all file information from the CentOS 7 repository in the website. 

### Usage
The script will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
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
$ python scraper/__main__.py
$ ls *.csv
files.csv
```

### Run as Installable Single Package
#### Create the environment
```
$ pipenv shell
```
#### Install dependencies
```
$ pipenv install -e .
```
#### Run
```
$ python -m 

```


### Run the script and check the csv file:
```
$ python scraper.py
$ ls *.csv
file.csv
```
Note: The default csv file would be file.csv, but  on the script, it can be changed to anything.


