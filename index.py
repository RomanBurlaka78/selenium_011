from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()


browser.get("https://eplatforma.nowoczesnaszkola.edu.pl/login/index.php")

browser.implicitly_wait(5)
# sleep(10)
usernameInput = browser.find_element(By.ID, "username")
usernamePass = browser.find_element(By.ID, "password")

rememberUsername = browser.find_element(By.ID, "rememberusername")

submitButn = browser.find_element(By.ID, "loginbtn")


usernameInput.send_keys('username')
sleep(3)
usernamePass.send_keys('7777777')
sleep(3)
rememberUsername.click()
sleep(3)
submitButn.click()

sleep(7)
  
browser.close()