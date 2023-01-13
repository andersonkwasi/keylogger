from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
passwrd = 'passwordMoise'
login ='yaoanderson.kouassi@groupecerco.com'
driver = webdriver.Firefox()  

ServicesMoney = [
    "//span[normalize-space()='3- Recharge Wave']",    
    "//span[normalize-space()='4- Retrait Cash']",    
   ]

ModePaiement = [
    "//div[contains(text(),'Espèces')]",
    "//div[contains(text(),'Wave')]"    
]

driver.get('https://openmoise.ci/pos/ui?config_id=33#cids=1')
    
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='login']").send_keys(login)

time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(passwrd)

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/main/div/form/div[3]/button').click()
time.sleep(90)

        
for i in range(len(ServicesMoney)):
    
    driver.find_element(By.XPATH, ServicesMoney[i]).click()

    time.sleep(5)
    try:
        driver.find_element(By.XPATH, "//img[@alt='[Recharge Wave] 200 Fcfa']").click()
    except:
        driver.find_element(By.XPATH, "//img[@alt='[Retrait Cash] 200 Fcfa']").click()
               
    
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@class='button set-customer']").click()

    time.sleep(5)
    client = driver.find_element(By.XPATH, "//input[@placeholder='Rechercher un client']").send_keys("0748874989")

    time.sleep(10)
    driver.find_element(By.XPATH, "//td[@id='bal']").click() 


    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='button next highlight']").click()

    time.sleep(5)
    driver.find_element(By.XPATH, "//i[@title='Payer']").click()

    time.sleep(5)
    try:
        driver.find_element(By.XPATH, "//div[contains(text(),'Wave')]").click()
    except:
        driver.find_element(By.XPATH, "//div[contains(text(),'Espèces')]").click()
        
    time.sleep(5)
    try:        
        driver.find_element(By.XPATH, "//span[@class='next_text']").click()
    except:
        print("operation effectuée avec succes")
        
    time.sleep(20)      
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div/div/div/div[1]/div[2]").click()
    
    time.sleep(5)
    driver.find_element(By.XPATH, "//i[@title='Home']").click()

driver.quit()