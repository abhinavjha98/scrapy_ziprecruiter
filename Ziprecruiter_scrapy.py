import pandas as pd
import re
import requests
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()
import urllib.request
from warnings import warn
import math


url = "https://www.ziprecruiter.com/candidate/search?search=&location=Vista%2C+CA"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)


import secrets 
import string 
  
N = 7  
res = ''.join(secrets.choice(string.ascii_lowercase + string.digits) 
                                                  for i in range(N)) 

username = browser.find_element_by_id("email_address")
username.send_keys(str(res)+"@gmail.com")
browser.find_element_by_xpath("//input[@type='submit' and @value='Continue']").click()


sleep(10)
elems = browser.find_element_by_xpath("//button[contains(@class, 'load_more_jobs')]").click()

sleep(10)
aa = 0
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
while True:
    dataa = browser.current_url
    a = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
    datac = browser.current_url
    if dataa == datac:
        aa = aa +1
        if aa == 5:
            print(dataa,datac)
            break
    print(datac)
links = datac

sleep(5)
parse_link = links.split("&page=")
i = 1
pp=[]
for i in range(int(parse_link[1])+1):
    if i == 0:
        continue
    else:
        pp.append(parse_link[0]+"&page="+str(i))
print(pp)
sleep(5)
browser.get("https://www.ziprecruiter.com/candidate/search?search=&location=Vista%2C+CA")
browser.refresh()
sleep(5)
job_title = []
company = []
location = []
salary = []
emp_type = []
description = []
imgs = []
link_view = []
for k in pp:
    sleep(25)
    browser.get(k)
    try:
        job_tit=browser.find_elements_by_class_name("just_job_title")
        for j in job_tit:
            job_title.append(j.text)
    except NoSuchElementException:
        job_title.append("")
        
    try:
        descript=browser.find_elements_by_class_name("job_snippet")
        for i in descript:
            description.append(i.text)
    except NoSuchElementException:
        description.append("")
    
    try:
        cpm=browser.find_elements_by_class_name("t_org_link")
        for i in cpm:
            company.append(i.text)
    except NoSuchElementException:
        company.append("")
    
    try:
        emp_typ=browser.find_elements_by_class_name("data_item")
        for i in emp_typ:
            if "$" in i.text:
                pass
            else:
                emp_type.append(i.text)
    except NoSuchElementException:
        emp_typ.append("")
    try:
        loca = browser.find_elements_by_class_name("t_location_link")
        for i in loca:
            location.append(i.text)
    except NoSuchElementException:
        location.append("")   
    try:
        img_logo = browser.find_elements_by_xpath("//p/img")
        for i in img_logo:
            imgs.append(i.get_attribute("src"))
    except NoSuchElementException:
        imgs.append("")     
        
len(location)

link_view = []
for j in pp:
    browser.get(j)
    try:
        elems = browser.find_elements_by_xpath("//a[contains(@class, 't_job_link')]")
        for elem in elems:
            try:
                r = requests.get(elem.get_attribute("href")) 
                link_view.append(r.url)
            except AttributeError:
                link_view.append("")
            except requests.exceptions.ConnectionError:
                r.status_code = "Connection refused"
    except NoSuchElementException:
        link_view.append("")

len(link_view)

import pandas as pd 
   
lst = [job_title,company,location,salary,emp_type,description] 
 
df = pd.DataFrame(list(zip(imgs,job_title,location,company,description,link_view,emp_type)), columns =['Logo','Title','Location','Company','Description','ApplyLink','Job_type']) 
df
df.to_csv('ZipRecruiter.csv',index=False)