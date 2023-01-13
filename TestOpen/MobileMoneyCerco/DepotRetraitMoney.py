from selenium import webdriver
from selenium.webdriver.common.keys import Keys
passwrd = ''
login =''
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()  

ServicesMoney = [
    "//span[normalize-space()='2- Recharge Mobile Money']",    
    "//span[normalize-space()='4- Retrait Cash']",    
   ]

driver.get('https://openmoise.ci/pos/ui?config_id=33#cids=1')
    
driver.find_element(By.XPATH, "//input[@id='login']").send_keys(login)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwrd)

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/main/div/form/div[3]/button').click()
time.sleep(80)

        
for i in range(len(ServicesMoney)):
    
    driver.find_element(By.XPATH, ServicesMoney[i]).click()

    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//img[@alt='[Recharge Money] 200 Fcfa']").click()
    except:
        driver.find_element(By.XPATH, "//img[@alt='[Retrait Cash] 200 Fcfa']").click()
               
    
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='button set-customer']").click()

    time.sleep(2)
    client = driver.find_element(By.XPATH, "//input[@placeholder='Rechercher un client']").send_keys("Kouassi Yao Anderson")

    time.sleep(2)
    driver.find_element(By.XPATH, "//td[@id='bal']").click() 


    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='button next highlight']").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//i[@title='Payer']").click()

    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//div[contains(text(),'Mobile Money (Orange-MTN-Moov)')]").click()
    except:
        driver.find_element(By.XPATH, "//div[contains(text(),'Espèces')]").click()
        
    time.sleep(2)
    try:        
        driver.find_element(By.XPATH, "//span[@class='next_text']").click()
    except:
        print("Element non trouvé")
        
   
    time.sleep(30) 
    try:
        driver.find_element(By.XPATH, "//div[contains(text(),'Commandes')]").click()
    except:
        print("Nouvelle cmd non trouvé")
    
    try:    
       driver.find_element(By.XPATH, "//button[@class='highlight']").click()
    except:
        print("bouton non trouvé")
        
    time.sleep(5)
    try:        
        driver.find_element(By.XPATH, "//i[@title='Home']").click()
    except:
        print("Home non trouvé")
time.sleep(30)
driver.quit()