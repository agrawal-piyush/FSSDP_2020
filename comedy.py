
#https://en.wikipedia.org/wiki/List_of_comedy_films_of_the_1990s

from selenium import webdriver
from time import sleep
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_comedy_films_of_the_1990s"
browser = webdriver.Chrome("C:\chromedriver.exe")



browser.get(url)
T=D=C=P=G =[]

for i in range(1,69):
    t = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[1]").text
    T.append(t)
    d =browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[2]").text
    D.append(d)
    c =browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[3]").text
    C.append(c)
    p=browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[4]").text
    P.append(p)
    g = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[5]").text
    G.append(g)
browser.quit()

df = pd.DataFrame() 
df["Title"] = T
df["Director"] = D
df["Cast"] = C
df["Production Countrty"]=P
df["Genre"] = G
print(df)
df.to_csv("Comedy.csv") 
