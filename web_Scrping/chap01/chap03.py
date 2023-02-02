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
            <a class="external_link", href="www.google.com">google</a>

            <div id="class1">
                <p id="first">class1's first paragraph</p>
                <a class="exteranl_link", href="www.naver.com">naver</a>

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

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')
print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.text) # <title>태그의 텍스트만 리턴
print(soup.title.get_text()) # .text와 동일한 기능
print(soup.title.parent)

div_text2 = soup.find('div')
print(div_text2.text)

print ('----------------------------------------------------------')
div_text = soup.find('div',{'id':'text_id2'})
print(soup.find('div',{'id':'text_id2'}))
print(div_text.text)


print('-------<a> 태그 및 <a> 태그의 href 속성 추출 ------------')
href_link = soup.find('a', {'class':'internal_link'})
href_link = soup.find('a', class_='internal_link')

print(href_link.get('href'))
print(href_link['href'])

print('-----------------------------------------------------------')

print('href_link.attrs : ', href_link.attrs)
print('values()', href_link.attrs.values())
values = list(href_link.attrs.values())
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))

print('--------------span 태그 ----------------------')

tr = '''
<table>
<tr class="passed a b c" id="row1 example"><td>t1</td></tr>
<tr class="failed" id="row2"><td>t2</td></tr>
</table>
'''
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr'):

href_value = soup.find(attrs={'href' : 'www.google.com'})
print(href_value)
print(href_value['href'])
print(href_value.text)

span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs) # attribute 속성 추출
print('value:', span_tag.attrs['class']) # class 속성의 값 추출
print('text:', span_tag.text)