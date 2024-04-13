from telnetlib import EC

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from bit_api import *


# 网页元素基本操作
def element_input(path, content):  # 填入您需要操作的元素的路径以及内容
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, path))).send_keys(content)


def element_click(path):  # 填入您需要操作的元素的路径
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, path))).click()


def element_is_displayed(path):
    demo = driver.find_element(By.XPATH, path).is_displayed()
    print(demo)
    time.sleep(1)


# 页面基本操作
def web_jump_next():
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


def web_jump_new():
    attempt = 5
    new_window_handle = None
    former_web = driver.current_window_handle
    while not new_window_handle and attempt > 0:
        for handle in driver.window_handles:
            if handle != former_web:
                new_window_handle = handle
        attempt -= 1
        time.sleep(1)
    driver.switch_to.window(new_window_handle)
    print(driver.title)


def web_scroll(path):  # 滚动到某个元素的位置
    element = driver.find_element(By.XPATH, path)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(2)


if __name__ == '__main__':
    # 初始化
    res = openBrowser('5690df353bf1404db1fd30a52f42aa62')
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", res['data']['http'])
    service = Service(executable_path=res['data']['driver'])
    driver = webdriver.Chrome(service=service, options=chrome_options)
    main_web = driver.current_window_handle
    former_web = None

    # 前提确保DC已经登录完成
    driver.get('https://zealy.io/c/wormhole/questboard')

    # # Follow Wormhole on Twitter
    # element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    # web_jump_next()
    # time.sleep(2)
    # # Claim Reward
    # js = (
    #     "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
    #     "elementsWithText.forEach(function(element) {element.click();});")
    # driver.execute_script(js)
    # time.sleep(10)
    #
    # # Join the Wormhole Discord
    # element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    # web_jump_next()
    # time.sleep(2)
    # # Join Discord
    # js = (
    #     "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Join Discord');});"
    #     "elementsWithText.forEach(function(element) {element.click();});")
    # driver.execute_script(js)
    # # 跳转页面，手动Verify，60秒验证后不用管，页面自动关闭
    # web1 = driver.current_window_handle
    # web_jump_new()
    # time.sleep(10)
    # driver.close()
    # driver.switch_to.window(web1)
    # # Claim Reward
    # js = (
    #     "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
    #     "elementsWithText.forEach(function(element) {element.click();});")
    # driver.execute_script(js)
    # time.sleep(5)

    # Follow Wormhole on LinkedIn
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # Visit this page
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Visit this page');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    web1 = driver.current_window_handle
    web_jump_new()
    driver.close()
    driver.switch_to.window(web1)
    time.sleep(12)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(5)

    # Subscribe to Wormhole Ytb
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # Visit this page
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Visit this page');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    web1 = driver.current_window_handle
    web_jump_new()
    driver.close()
    driver.switch_to.window(web1)
    time.sleep(12)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(3)

    # Visit the Wormhole Blog
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # Visit this page
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Visit this page');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    web1 = driver.current_window_handle
    web_jump_new()
    driver.close()
    driver.switch_to.window(web1)
    time.sleep(12)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(5)

    # Visit the Wormhole Website
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # Visit this page
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Visit this page');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    web1 = driver.current_window_handle
    web_jump_new()
    driver.close()
    driver.switch_to.window(web1)
    time.sleep(12)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(5)

    # Follow Wormhole labs on Twitter
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(10)

    # Follow Xlab on Twitter
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(10)

    # Follow WF on Twitter
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(10)

    # Follow Wormhole China on Twitter
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(10)

    # Question 1
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # A
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('A set of distributed nodes which monitor state on several blockchains');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 2
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # D
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('All of the above');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 3
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # C
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Arbitrary data and assets that exist in their own layer independent of any blockchain, which makes xData accessible by all blockchains');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 4 (不确定)
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # A
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Cross-chain decentralized applications that can utilise xData and xAssets');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 5
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # C
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('book.wormhole.com');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 6
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # C
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Both of the above');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 7
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # B
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('https://docs.wormhole.com/');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 8
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # B
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('The Wormhole Discord');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(5)

    # Question 9
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # D
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('All of the above');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)

    # Question 10
    element_click('//*[@id="scroll-wrapper"]/div/div/div/div/div/div/div[4]/div[1]/div[3]/div[1]')
    web_jump_next()
    time.sleep(2)
    # D
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('All of the above');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)

    # Daily Connect
    web_scroll('//*[@id="c50f41c2-578c-413a-a528-76a4ed50b491"]')
    element_click('//*[@id="c50f41c2-578c-413a-a528-76a4ed50b491"]')
    web_jump_next()
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)


