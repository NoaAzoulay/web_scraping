# web_scraping

I was challenged to do this web scraping assignment , by using Selenium library
There are 3 parts :
1.	BBC news link : scrap this web, and download all articles in the main page
Since the main page have links to all articles, first I saved all links and then with the webdriver I opened each article and saved its content to file.

2.	Airport website : scrap the table of arrivals flights . 
First, when opening the website, only 12 rows of flights details are shown in table,
there is a button to click which open more 12 rows, and so on until all table is shown. I wrote a function to demo button click until the table is fully opened.
Then I saved all data by columns in lists , and then iterated all lists to create objects of flight-data. Then wrote in JSON format to files.

3.	Search model : given a string, search if it appears in files. If it does, the file name and the line of first instance of the string is printed to console




#python #selenium #web_driver #web_scraping
