"""
Involves:
1. Web Scrapping : HTML, Xpath Expressions, Selenium (Scrapping tool for python), ChromeDriver (WebDriver for chrome)

   Notes:
       1. Don't download ChromeDriver manually:
       While it's possible to find ChromeDriver downloads online,
       it's not recommended.  Manually downloaded versions might become incompatible with Chrome updates.
       There's a better way.

       2. Use webdriver_manager:
       Webdriver_manager is a Python package that simplifies the process of downloading and managing the correct
       ChromeDriver version for your specific Chrome browser or other browsers like Fire Fox etc.
       Once you download the driver, no need to use webdriver_manager further. You can disable it.

       3. Selenium:
       Make sure you have installed selenium in the currently in-use venv. We need to import only the webdriver module
       from selenium. If you are using older versions of it, refer documentations for using service module or others
       according to your process steps.
       Newer versions of selenium close the driver automatically after the end of the process or task as a part of best
       practice.


2. Data Transferring: Pandas (Data frame tool), CSV

   Notes:
       1. Pandas:
       We will use pandas to create a data frame using list variables that we got via the web scrapping commands.






"""
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Download and configure ChromeDriver (no need to store the return value)
# ChromeDriverManager().install()
"----------------------------------------------Web Scrapping (Selenium)--------------------------------------"
# Assign the link to a variable
website = 'https://www.thesun.co.uk/sport/football/'

# Create a new Chrome session using the downloaded ChromeDriver
driver = webdriver.Chrome()
driver.get("https://www.thesun.co.uk/sport/football/")

# Assign the XPath value for containers
# //div[@class='teaser__copy-container']

"""The container var is a list of iterables. Notice we used find.elements"""
containers_xpath = "//div[contains(@class, 'teaser__copy-container')]"
containers = driver.find_elements(By.XPATH, containers_xpath)

# //div[@class='teaser__copy-container']/a/span  --- XPath value for Titles
# //div[@class='teaser__copy-container']/a/h3  ------ XPath value for Sub Titles



print('The type of the container is:',type(containers), sep=' ', end='\n')
#print(containers)
""" Loop through the container to get the single elements"""
""" Use .text to get only the texts from the elements"""
# We could have used driver.find_elements, but in this case, we gotta use the full XPath expression
titles = []
subtitles = []
links = []

# XPath values for Titles & Sub Titles (adjust if needed)
title_xpath = ".//a/span"  # Assuming title is within an anchor tag with a span child
subtitle_xpath = ".//a/h3"  # Assuming subtitle is within an anchor tag with an h3 child
link_xpath = "//div[@class='teaser__copy-container']/a"
link_attribute = "href"
wait_time = 10
for container in containers:
    try:
        title = WebDriverWait(container, wait_time).until(EC.visibility_of_element_located((By.XPATH, title_xpath))).text
        subtitle = WebDriverWait(container, wait_time).until(EC.visibility_of_element_located((By.XPATH, subtitle_xpath))).text
        link = WebDriverWait(container, wait_time).until(EC.visibility_of_element_located((By.TAG_NAME, "a"))).get_attribute(link_attribute)
        #print("It is inside Try")
    except(TimeoutException, NoSuchElementException):
        title = None  # Set title to None if not found
        subtitle = None  # Set subtitle to None if not found
        link = None  # Set subtitle to None if not found
        #print("It is inside except")
    #print(title)

    #subtitle = WebDriverWait(container,10.00).until(EC.visibility_of_element_located((By.XPATH,subtitle_xpath))).text

    #link = container.find_element(by='xpath', value="//div[@class='teaser__copy-container']/a").get_attribute("href")  # Get the link of each cards
    #link = WebDriverWait(container,10.00).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='teaser__copy-container']/a"))).get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)



print('The titles are:',titles,sep="\n",end='\n')
print('The subtitles are:',subtitles,sep="\n",end='\n')
print('The links:',links,sep="\n",end='\n')


"-------------------------------------------------Data Transfer (Pandas)-------------------------------------"

import pandas as pd

# Create a dictionary
# Then, use that to create a dataframe
# Export the dataframe to CSV at your desired location.

"Here you can go with different approaches. If you have to export it to excel,dictionary or JSON and etc "
"Then you need to create a data structure that the corresponding file type supports "
"As I have to export it to a csv, I made a DataFrame structure as csv supports it and also the NDFrame type"

my_dic = {'Titles': titles, 'Sub_Titles': subtitles, 'Links': links}
df_HeadLines = pd.DataFrame(my_dic)
path = "C:\\Users\\USER\Downloads\\Headings_News.csv"
df_HeadLines.to_csv(path)
