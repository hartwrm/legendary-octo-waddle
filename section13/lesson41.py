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
actions = ActionChains(browser)
zipcode = "02169"

## open weather.com and click on the "today" header
elem = browser.find_element(By.CSS_SELECTOR, "a.styles--listItem--3b2Ko:nth-child(1)")
elem.click()

## find search bar and populate zip code
WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="LocationSearch_input"]'))).send_keys(zipcode)
## click on first matching result
WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR,  "#LocationSearch_listbox-0"))).click()



##tried to play a video on weather.com
##browser.swtich_to.frame(browser.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/section/div/div[2]/div/div[2]/div[8]/div[1]/div/iframe"))
##WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[1]/div/div/section/div/div[2]/div/div[2]/div[12]/div[1]/div/div/div[2]/div"))).click()

## part of the lesson but there is an issue with a lot of links being obstructed and unable to click, havnet been able to solve
##myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "Chapter  6 – Manipulating Strings")))
##elem = ActionChains(browser).move_to_element(myElem).click().perform()
##li_elem = elem.find_element(By.XPATH, "/html/body/div/main/div/ul[2]/li[7]/a")
##li_elem.click()
