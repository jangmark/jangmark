from selenium import webdriver
from time import sleep
#driver = webdriver.Chrome('C:/workspace/chromedriver.exe’) # Windows 사용자
driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')

driver.get('https://www.google.com')
print(driver.current_url)
print(driver.title)
print(driver.page_source) # HTML 소스 가져오기
driver.implicitly_wait(time_to_wait=5)
find_element_by_name()
# driver.close() # 하나의 탭만 종료
# driver.quit() # webdriver 전체 종료

