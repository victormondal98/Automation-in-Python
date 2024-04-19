# Automation-in-Python
## Involves:
1. Web Scrapping: HTML, Xpath Expressions, Selenium (Scrapping tool for python), ChromeDriver (WebDriver for chrome)

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


3. Data Transferring: Pandas (Data frame tool), CSV

   Notes:
       1. Pandas:
       We will use pandas to create a data frame using list variables that we got via the web scrapping commands.
