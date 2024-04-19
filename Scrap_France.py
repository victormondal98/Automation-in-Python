import selenium.webdriver
import selenium.common
import selenium.types
import selenium.webdriver.common.by as x
import pandas as pd
import selenium.webdriver.support.ui as t
import selenium.webdriver.support.expected_conditions as C
website = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=France'

driver = selenium.webdriver.Chrome()
driver.get(website)

# Assign the variable for the containers
containers_XPath = '//div/table[@class="data_wide_table new_bar_table"]/tbody/tr'
containers = driver.find_elements(x.By.XPATH, containers_XPath)
print(len(containers))

# Create empty lists to store elements from the containers
Normal_Conetents = []
Price_Normal = []
#Price_Hihjlighted = []

# Assign the XPaths of the single element

Normal_Conetents_Xpath = '//div/table[@class="data_wide_table new_bar_table"]/tbody/tr/td'
Price_Normal_Xpath = '//div[@class="innerWidth"][2]/table[1]/tbody/tr/td[2]/span'
wait_time = 10

for container in containers:
    try:
        #content = t.WebDriverWait(container,wait_time).until(C.visibility_of_element_located((x.By.XPATH,Normal_Conetents_Xpath))).text
        content = container.find_element(x.By.TAG_NAME, 'td').text
        #content2 = container.find_element(x.By.XPATH, Price_Normal_Xpath).text 'This did repetation of the first node'
        content2 = container.find_element(x.By.TAG_NAME, 'span').text
        content2 = content2[:-3]

    except(selenium.common.TimeoutException,selenium.common.NoSuchElementException):
        content = None
        content2 = None
    Normal_Conetents.append(content)
    Price_Normal.append(content2)


print('Normal Contents length :',len(Normal_Conetents))
print('Normal Prize length :',len(Normal_Conetents))


print('Contents by Tag Name :',Normal_Conetents,sep='\n',end='\n')
print('Contents by X Path price :',Price_Normal,sep='\n',end='\n')



my_dic = {'Titles': Normal_Conetents,'Price': Price_Normal}
df_HeadLines = pd.DataFrame(my_dic)
path = "C:\\Users\\USER\Downloads\\Headings.csv"
df_HeadLines.to_csv(path)
