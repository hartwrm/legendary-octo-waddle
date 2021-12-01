from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
delay = 3
browser = webdriver.Firefox()
browser.get('https://weather.com/')
browser.maximize_window()

elem = browser.find_element(By.CSS_SELECTOR, "div.undefined > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)").click()
browser.swtich_to.frame(browser.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/section/div/div[2]/div/div[2]/div[8]/div[1]/div/iframe"))
WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[1]/div/div/section/div/div[2]/div/div[2]/div[12]/div[1]/div/div/div[2]/div"))).click()


##myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "Chapter  6 – Manipulating Strings")))
##elem = ActionChains(browser).move_to_element(myElem).click().perform()
##li_elem = elem.find_element(By.XPATH, "/html/body/div/main/div/ul[2]/li[7]/a")
##li_elem.click()
