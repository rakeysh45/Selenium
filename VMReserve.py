import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=edge_options)
driver.get("https://webtools.mp.ics.com/index.php?")

details_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "details-button"))
)
details_button.click()

proceed_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "proceed-link"))
)
proceed_link.click()

username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "wlUsr"))
)
username_field.send_keys("rakeshs")

password_field = driver.find_element(By.NAME, "wlPwd")
password_field.send_keys("Vc34@e1Ws*^x")

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "wlLogin"))
)
login_button.click()

ah_cap_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "4ba3cd475de12"))
)
ah_cap_link.click()

mpvm15_link = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[3]/table/tbody/tr[15]/td[1]/a'))
)
mpvm15_link.click()

reserve_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[3]/form/table/tbody/tr[24]/td[2]/input'))
)
reserve_button.click()

alert = driver.switch_to.alert
alert.accept()

time.sleep(500)

driver.quit()
