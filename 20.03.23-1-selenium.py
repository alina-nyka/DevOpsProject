from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# driver for Windows:
# driver=webdriver.Chrome(executable_path="C:/Users/nykak/Desktop/tip_calc/index.exe")'
# -----------------------------------------
# to check if it works you need to run it!:
# driver.get("https://github.com")
# -----------------------------------------
# for Windows
driver.get("file://c:/Users/nykak/Desktop/DevOps/less4/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
# suppose to send a value into a field with id billamt
billamt.send_keys("100")
sleep(10)
# for copy xpath go to browser->inspect->elements->find elements that you
# need->right click on it->copy->copy xpath=>//*[@id="serviceQual"]/option[5]
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]option[5]")
s.click()
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys(5)
driver.find_element(by="id", value="calculate").click()
expected = "2.00"
actual = driver.find_element(by="id", value="tip").text
# if expected == actual:
#    print("tip calculation is ok")
# instead of if we can write:
assert expected == actual
sleep(5)
driver.close()
