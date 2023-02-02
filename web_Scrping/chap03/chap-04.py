'''
3.3 인터넷 크롤링

예제 6
'''

from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import random

pages = set
random.seed(None)
# 웹 페이지에서 발견된 내부 링크를 모두 목록으로 만듬
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # "/"로 시작하는 링크를 모두 찾음
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# 웹 페이지에서 발견된 외부 링크를 모두 목록으로 만듬
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 
    # 링크를 모두 찾음
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
        bs = BeautifulSoup(html, 'html.parser')
        externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    
        if len(externalLinks) == 0: # 외부 링크가 없으면 내부 링크 검색
            print('No external links, looking around the site for one')
            domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
            print('domain: ', domain)
            internalLinks = getInternalLinks(bs, domain)
            return getRandomExternalLink(internalLinks[random.randint(0,
                                                                  len(internalLinks) - 1)])
        else: # 랜덤하게 외부 링크 선택                
            return externalLinks[random.randint(0, len(externalLinks) - 1)]
    except Exception as e:
        print('Exception 발생: ', e) 

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    # quote(externalLink): 한글이 포함된 url인 경우, UnicodeEncodeError 발생
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')