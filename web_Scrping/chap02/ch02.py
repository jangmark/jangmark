from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')

soup = BeautifulSoup(html, 'html.parser')
# table_tag = soup.find('table', {'id':'giftList'})
# for child in table_tag.children:
#     print(child)

desc = soup.find('table', {'id':'giftList'}).descendants
print('descendants 개수: ', len(list(desc)))

# for child in soup.find('table', {'id':'giftList'}).descendants:
#     print(child)
#     print('---------------')

for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print(ord(sibling))
sibling1