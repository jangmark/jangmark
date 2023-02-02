from selenium import webdriver
driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(3)
# id, 비밀번호 전달
# <input>의 이름이 id를 검색
driver.find_element_by_name('id').send_keys('jangmark1995')
driver.find_element_by_name('pw').send_keys('536536ab')

driver.find_element_by_xpath('//*[@id="log.login"]').click()
