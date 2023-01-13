from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
passwrd = ''
login =''
import time
driver = webdriver.Firefox()

# https://openmoise.ci/web#action=115&active_id=mail.box_inbox&cids=1&menu_id=91

driver.get('https://openmoise.ci/pos/ui?config_id=33#cids=1')

time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='login']").send_keys(login)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwrd)

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/main/div/form/div[3]/button').click()

time.sleep(80)
driver.find_element(By.XPATH, "//span[normalize-space()='1- Transfert Crédits Téléphonique']").click()

time.sleep(5)
driver.find_element(By.XPATH, "//img[@alt='[Achat de Crédit] 100 Fcfa']").click()


time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='button set-customer']").click()

time.sleep(5)
client = driver.find_element(By.XPATH, "//input[@placeholder='Rechercher un client']").send_keys("Kouassi Yao Anderson")

time.sleep(5)
driver.find_element(By.XPATH, "//td[@id='bal']").click() 


time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='button next highlight']").click()

time.sleep(5)
driver.find_element(By.XPATH, "//i[@title='Payer']").click()

time.sleep(5)
driver.find_element(By.XPATH, "//div[contains(text(),'Espèces')]").click()

time.sleep(5)
driver.find_element(By.XPATH, "//span[@class='next_text']").click()


time.sleep(10)
driver.quit()