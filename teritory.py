'''
https://en.wikipedia.org/wiki/List_of_state_and_territorial_capitols_in_the_United_States
'''


from selenium import webdriver
import pandas as pd
from time import sleep

url="https://en.wikipedia.org/wiki/List_of_state_and_territorial_capitols_in_the_United_States"

browser =  webdriver.Chrome("C:\chromedriver.exe")
browser.get(url)
#P=[]
C=[]
L=[]
Y=[]
H=[]
N=[]

for i in range(1,30):
    #p = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[1]").text
    #P.append(p)  
    c = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[2]").text
    C.append(c) 
    l = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[3]").text
    L.append(l)
    y = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[4]").text
    Y.append(y) 
    h = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[5]").text
    H.append(h)
    n = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[4]/div/table/tbody/tr["+str(i)+"]/td[6]").text
    N.append(n)
browser.quit()

df = pd.DataFrame()
#df["Picture"] =P
df["Capital"]=C
df["Location"]=L
df["Years of current capitol consytuction"]=Y
df["Heights"] = H
df["Notes"] = N

print(df)   
df.to_csv("teritory.csv") 