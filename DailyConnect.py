import time
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

    # 前提确保前面所有任务都已完成
    driver.get('https://zealy.io/c/wormhole/questboard')

    # Daily Connect
    element_click('//*[@id="c50f41c2-578c-413a-a528-76a4ed50b491"]')
    web_jump_next()
    time.sleep(2)
    # Claim Reward
    js = (
        "var elementsWithText = Array.from(document.querySelectorAll('*')).filter(function(element) {return element.innerText && element.innerText.includes('Claim Reward');});"
        "elementsWithText.forEach(function(element) {element.click();});")
    driver.execute_script(js)