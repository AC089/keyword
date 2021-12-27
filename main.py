from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def count(dt, driver, xpath):
    if isElementExist(driver, xpath):
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        str = element.text
        if str in dt:
            dt[str] += 1
        else:
            dt[str] = 1
    else:
        print('没有关键字')

def isElementExist(driver, element):
    flag = True
    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, element)))
        return flag
    except:
        flag = False
        return flag

options = webdriver.ChromeOptions()

#手机模式
mobile_emulation = {"deviceName": "iPhone X"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
c_service = Service('./chromedriver')
# c_service = Service("chromedriver.exe")
c_service.command_line_args()
c_service.start()

driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
# driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
try:
    while True:
        keyword = input('\n\n输入关键字:')
        if keyword == "":
            break
        dt = {}
        driver.get("https://baidu.com")
        driver.find_element_by_id("index-kw").send_keys(keyword)
        driver.find_element_by_id("index-bn").click()
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[2]/div[1]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[2]/div[2]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[3]/div[1]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[3]/div[2]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[4]/div[1]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[4]/div[2]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[5]/div[1]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../div[5]/div[2]/a/span")

        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[1]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[2]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[3]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[4]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[5]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[6]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[7]/a/span")
        count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[8]/a/span")

        flag = isElementExist(driver, "//span[contains(text(), '已了解安全风险，查看更多')]/../../a")
        if flag:
            sel = driver.find_element_by_xpath("//span[contains(text(), '已了解安全风险，查看更多')]/../../a")
            driver.execute_script("arguments[0].click();", sel)


        flag = isElementExist(driver, "//*[@id='page-controller']/div/a")
        if flag:
            sel = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-controller']/div/a")))
            driver.execute_script("arguments[0].click();", sel)
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[1]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[2]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[3]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[4]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[5]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[6]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[7]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[8]/a/span")
    
        flag = isElementExist(driver, "//*[@id='page-controller']/div/div[3]/a")
        if flag:
            sel = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-controller']/div/div[3]/a")))
            driver.execute_script("arguments[0].click();", sel)
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[1]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[2]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[3]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[4]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[5]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[6]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[7]/a/span")
            count(dt, driver, "//div[contains(text(),'大家还在搜')]/../../../div[2]/div[8]/a/span")

        for i in dt:
            print("%s  %d" %(i, dt[i]))
    driver.close()
finally:
    driver.quit()
    c_service.stop()



    