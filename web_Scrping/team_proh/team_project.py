import requests
from bs4 import BeautifulSoup

url = "https://www.jobkorea.co.kr/recruit/joblist?ct=0300&cg=0300&pg=1"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

jobs = soup.find_all('div', {'class': 'recruitment-items'})
for job in jobs:
    title = job.find('a', {'class': 'job-title'}).text.strip()
    company = job.find('div', {'class': 'recruit-company'}).text.strip()
    location = job.find('div', {'class': 'recruit-location'}).text.strip()
    print(title, company, location)
