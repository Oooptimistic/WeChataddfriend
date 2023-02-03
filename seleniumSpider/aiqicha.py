from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://aiqicha.baidu.com/s?q=%E6%B7%B1%E5%9C%B3%E8%A3%85%E4%BF%AE&t=0")
pause = input('扫码登录:')
print(pause)

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/h3/a').click()
time.sleep(5)
# company = driver.find_element(By.CSS_SELECTOR, 'body > div.base.page-detail.has-search-tab > div.aqc-content-wrapper.has-footer > div > div.detail-header-container > div.detail-header > div.header-top > div.header-content > div.content-title > h1').text
# tel = driver.find_element(By.CSS_SELECTOR, 'body > div.base.page-detail.has-search-tab > div.aqc-content-wrapper.has-footer > div > div.detail-header-container > div.detail-header > div.header-top > div.header-content > div.content-info > div:nth-child(1) > div.telphone-lists-wrap.detail-header-item > div > span.first-data.text-icon-middle > span > span').text
a = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/h1')

print(a)
