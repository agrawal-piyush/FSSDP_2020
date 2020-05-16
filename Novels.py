"""
https://en.wikipedia.org/wiki/Time%27s_List_of_the_100_Best_Novels
"""

from selenium import webdriver
import pandas as pd
from time import sleep

url = "https://en.wikipedia.org/wiki/Time%27s_List_of_the_100_Best_Novels"
browser = webdriver.Chrome("C:\chromedriver.exe")



browser.get(url)


Title=[]
Author=[]
Year=[]
for i in range(1,100):
    t = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[1]").text
    Title.append(t)
    a = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[2]").text
    Author.append(a)
    Y = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table[2]/tbody/tr["+str(i)+"]/td[3]").text.replace("\n","")
    Year.append(Y)
    


sleep(5)
browser.quit()

df = pd.DataFrame()
df["Title"]=Title
df["Author"]= Author
df["Year"]= Year
print(df)

df.to_csv("Novels.csv")

