from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

jobDescription = []
company = []
experience = []
salaryPosted = []
locationPosted = []
jobDetails = []
skillsRequired = []
#url = "https://www.naukri.com/data-scientist-jobs-"
#driver.get(url)
#url = "https://www.naukri.com/data-scientist-jobs-"
driver = webdriver.Chrome("C:/Users/Tejan/Documents/web_scraping/chromedriver")

for i in range(2,31):
    url = "https://www.naukri.com/data-scientist-jobs-"
    url = url + str(i)
    print(url)
    driver.get(url)
    
    
    job_desc = driver.find_elements_by_xpath('.//a[@class = "title fw500 ellipsis"]')
    com_name = driver.find_elements_by_xpath('.//a[@class = "subTitle ellipsis fleft"]')
    exp = driver.find_elements_by_xpath('.//li[@class = "fleft grey-text br2 placeHolderLi experience"]')
    salary = driver.find_elements_by_xpath('.//li[@class = "fleft grey-text br2 placeHolderLi salary"]')
    location = driver.find_elements_by_xpath('.//li[@class = "fleft grey-text br2 placeHolderLi location"]')
    job_details = driver.find_elements_by_xpath('.//div[@class = "job-description fs12 grey-text"]')
    skills = driver.find_elements_by_xpath('.//ul[@class = "tags has-description"]')
    len_jobs = len(job_desc)
    for i in range(len_jobs):
        jobDescription.append(job_desc[i].text)
        company.append(com_name[i].text)
        experience.append(exp[i].text)
        salaryPosted.append(salary[i].text)
        locationPosted.append(location[i].text)
        jobDetails.append(job_details[i].text)
        skillsRequired.append(skills[i].text)

    time.sleep(5)

dict = {'JobDescription': jobDescription, 'Company': company, 'Experience': experience, 'Salary':salaryPosted, 'Location':
    locationPosted, 'JobDetails':jobDetails, 'Skills':skillsRequired}
df = pd.DataFrame(dict)
df.to_csv('gatheredData.csv', index = False)