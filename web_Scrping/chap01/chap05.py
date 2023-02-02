from bs4 import BeautifulSoup

html_example = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BeautifulSoup 활용</title>
    </head>
    <body>
        <h1 id="heading">Heading 1</h1>
        <p>Paragraph</p>
        <div id="link">
            <a class="external_link" href="www.google.com">google</a>

            <div id="class1">
                <p id="first">class1's first paragraph</p>
                <a class="exteranl_link" href="www.naver.com">naver</a>

                <p id="second">class1's second paragraph</p>
                <a class="internal_link" href="/pages/page1.html">Page1</a>
                <p id="third">class1's third paragraph</p>
            </div>
        </div>
        <div id="text_id2">
            Example page
            <p>g</p>
        </div>
        <h1 id="footer">Footer</h1>
    </body>
    </html>
'''

soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head.text)
print(head.text.strip())

footer = soup.select_one('h1#footer')
print(footer)

class_link = soup.select_one('a.internal_link')
print(class_link)

external_link = soup.find('a',{'class': 'external_link'})
print(external_link)
print(external_link.text)

print('-------------select 모든함수 ------------')

h1_all = soup.select('a')
print(h1_all)

url_links = soup.select('a')
for x in url_links:
    print(x['href'])

print('---------내부의 모든 url 검색------------------')
div_urls = soup.select('div#class1 > a')
print(div_urls)
print(div_urls[0]['href'])

print('---------------id, heading, footing ---------')
h1 = soup.select('#heading, #footing')

print('• <a>태그의 class이름이 “external_link”와 ”internal_link” 모두 검색')
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)

