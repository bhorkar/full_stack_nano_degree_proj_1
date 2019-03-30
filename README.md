
# Log summary  
This project is a part of the Udacity's Full Stack Web Developer Nanodegree.
The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


 The reporting answer the 3 following questions from :
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?


## Prerequisites
* ```Python 3``` (https://www.python.org/) 
* ```Vagrant``` (https://www.vagrantup.com/downloads.html)
* ```VirtualBox``` (https://www.virtualbox.org/wiki/Downloads)
* ```Vagrantfile``` (https://github.com/udacity/fullstack-nanodegree-vm)

## Installation instructions  
Start the Ubuntu Linux installation with ```vagrant up```.
Log into the Linux VM with ```vagrant ssh```. Load the data into the PostgreSQL database. Use the command ```psql -d news -f newsdata.sql```.



There are three tablesin the database:
* The ```authors``` table includes information about the authors of articles.
* The ```articles``` table includes the articles themselves.
* The ```log table``` includes one entry for each time a user has accessed the site.


## Running the program 
The sql query can be run as 

```python3 analysis.py```
