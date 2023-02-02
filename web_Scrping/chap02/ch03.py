import re
m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple','I like apple!'))

p = re.compile('[a-z]+') # 알파벳 소문자
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

print('---------------------정규 표현식--------------------')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
# 정규식: ('img.*\.jpg'): img 다음에 임의의 한 문자가 0회 이상: img.jpg, img1.jpg, imga.jpg 등
img_tag = re.compile('/img/gifts/img.*.jpg')
# find_all()에서 img의 src 속성값에 정규식 사용
images = soup.find_all('img', {'src': img_tag})

for image in images:
    print(image, end=" -> ['src'] 속성: ")
    print(image['src'])