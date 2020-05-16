"""
https://en.wikipedia.org/wiki/List_of_countries_by_tea_consumption_per_capita
"""

from selenium import webdriver
import pandas as pd
from time import sleep

url = "https://en.wikipedia.org/wiki/List_of_countries_by_tea_consumption_per_capita"
browser = webdriver.Chrome("C:\chromedriver.exe")



browser.get(url)


Rank=[]
Tea=[]
Country=[]
for i in range(1,55):
    r = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[1]").text
    Rank.append(r)
    c = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[2]").text
    Country.append(c)
    t = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[3]").text.replace("\n","")
    Tea.append(t)
    


sleep(5)
browser.quit()

df = pd.DataFrame()
df["Rank"]=Rank
df["Country\Region"]= Country
df["Tea Consumption"]= Tea
print(df)

df.to_csv("teaconsumptionpercapital.csv")
