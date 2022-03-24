from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://pypi.org/project/selenium/")
driver.quit()