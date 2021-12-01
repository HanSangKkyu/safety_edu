from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

ser = Service("/Users/han/Downloads/jj/chromedriver") # chromedriver가 있는 디렉터리 경로
op = webdriver.ChromeOptions()
chrome = webdriver.Chrome(service=ser, options=op)
chrome.get('https://safety.konkuk.ac.kr/ushm/edu/online.do') # 안전교육 URL
idinput = chrome.find_element_by_xpath('//*[@id="userId"]')
idinput.send_keys('input your ID') # ID 입력하기
pwinput = chrome.find_element_by_xpath('//*[@id="userName"]')
pwinput.send_keys('input your PW') # PW 입력하기
chrome.find_element_by_xpath('//*[@id="btnUser"]').click()
chrome.get('https://safety.konkuk.ac.kr/ushm/edu/online.do')
chrome.implicitly_wait(3)

for a in range(2,9):
    while(True):
        btn = chrome.find_element_by_xpath('//*[@id="tblProgressList"]/tbody/tr['+str(a)+']/td[7]/input')
        print('("******************'+str(a)+'btn.text', btn.get_attribute('value'))
        if(btn.get_attribute('value') == '다시보기'):
            break
        btn.click()
        chrome.implicitly_wait(3)
        chrome.switch_to.window(chrome.window_handles[-1])
        now = int(chrome.find_element_by_css_selector('#footer > div > div.pageNumDiv > div.pageNum.cPageNum').text)
        num = int(chrome.find_element_by_css_selector('#footer > div > div.pageNumDiv > div.pageNum.tPageNum').text)
        print("******************now",now)
        print("******************num",num)
        dtime = chrome.find_element_by_css_selector('#footer > div > div.timeDiv > div.dTime').text.split(':')
        playTime = int(dtime[0])*60 + int(dtime[1]) + 3
        sleep(playTime)
        print("******************playTime",playTime)
        chrome.close()
        chrome.switch_to.window(chrome.window_handles[-1])
        if(now == num):
            break
    