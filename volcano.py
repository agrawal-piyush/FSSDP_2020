'''
https://en.wikipedia.org/wiki/List_of_large_volcanic_eruptions_in_the_21st_century
''''

from selenium import webdriver
import pandas as pd
from time import sleep

url="https://en.wikipedia.org/wiki/List_of_large_volcanic_eruptions_in_the_21st_century"

browser =  webdriver.Chrome("C:\chromedriver.exe")


browser.get(url)
Ve=[]
V=[]
C=[]
Y=[]
Ca=[]
N=[]

for i in range(1,30):
    ve = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/th").text
    Ve.append(ve)  
    v = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[1]").text
    V.append(v) 
    c = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[2]").text
    C.append(c)
    y = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[3]").text
    Y.append(y) 
    ca = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[4]").text
    Ca.append(ca)
    n = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[5]").text
    N.append(n)
browser.quit()

df = pd.DataFrame()
df["VEI"] =Ve
df["Volcano eruption"]=V
df["Country"]=C
df["Year"]=Y
df["Casualities"] = Ca
df["Notes"] = N

print(df)   
df.to_csv("volcano.csv") 