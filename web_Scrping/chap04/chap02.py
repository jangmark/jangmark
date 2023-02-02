from selenium import webdriver


driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')
driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)

# find_element_by_class_name('클래스이름'): 하나의 클래스 이름 검색
name = driver.find_element_by_class_name('green')
print(name.text)
print('-' * 20)

# find_elements_by_class_name('클래스이름'): 해당 클래스 이름을 모두 검색
nameList = driver.find_elements_by_class_name('green')
for name in nameList:
    print(name.text)

driver.quit()