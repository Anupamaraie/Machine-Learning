from bs4 import BeautifulSoup
import requests
import pandas as pd


response = requests.get('https://negja.org.np/index.php?page=rates')
soup = BeautifulSoup(response.text,'html.parser')

rates = soup.find('table').find_all('tr')[1:100]
    
data=[]

for rate in rates:
    item = {}
    item['Gold'] = str(rate.find_all('td'))[31:36]
    item['Silver'] = str(rate.find_all('td'))[77:81].replace('.','')

    data.append(item)

df = pd.DataFrame(data)
df.to_excel('GSrates.xlsx',index=False)
df.to_csv('GSrates.csv',index=False)