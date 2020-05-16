from selenium import webdriver


url = "https://bidplus.gem.gov.in/servicelists"


Bid_No=[]
Items=[]
Quantity=[]
Dept_name_addr=[]
Start=[]
End=[]


browser = webdriver.Chrome("C:\chromedriver.exe")

browser.get(url)

for j in range(1,5):
    for i in range(1,10):    
        bid_num = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text.replace("\n"," ")
        bid_num_list.append(bid_num)
    
        items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text.replace("\n"," ")
        items_list.append(items)
    
        quantity_req = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text.replace("\n"," ")
        quantity_req_list.append(quantity_req)
        
        dept_details = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text.replace("\n"," ")
        dept_details_list.append(dept_details)
        
        start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:10]
        start_date_list.append(start_date)
        
        start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
        start_time_list.append(start_time)
        
        end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:10]
        end_date_list.append(end_date)
        
        end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
        end_time_list.append(end_time)
    
    next_button=browser.find_element_by_xpath("//*[contains(text(), '»')]")
    next_button.click()
        

browser.quit()

df = pd.DataFrame()
df["Bid Number"]=bid_num_list
df["Items"]=items_list
df["Quantity Required"]=quantity_req_list
df["Department Name and Address"]=dept_details_list
df["Start Date"]=start_date_list
df["Start Time"]=start_time_list
df["End Date"]=end_date_list
df["End Time"]=end_time_list
print(df)

df.to_csv("servicelist.csv")


