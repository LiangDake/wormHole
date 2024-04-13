import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from bit_api import *


class BaseActions:
    # 网页初始化
    def __init__(self, id, url, password):  # 比特浏览器的窗口ID，页面的URL，小狐狸的登录密码
        self.id = id
        self.url = url
        self.password = password
        res = openBrowser(id)
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", res['data']['http'])
        service = Service(executable_path=res['data']['driver'])
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.main_web = self.driver.current_window_handle
        self.former_web = None
        self.driver.get(url)
        time.sleep(3)

    # 网页元素基本操作
    def element_input(self, path, content):  # 填入您需要操作的元素的路径以及内容
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path))).send_keys(content)

    def element_click(self, path):  # 填入您需要操作的元素的路径
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path))).click()

    def checkbox_click(self, path):
        mycheckbox = self.driver.find_element(By.XPATH, path)
        # Select checkbox if not already selected
        if not mycheckbox.is_selected():
            mycheckbox.click()
            print(f"{mycheckbox.get_attribute('value')} checkbox is selected.")
        else:
            print(f"{mycheckbox.get_attribute('value')} checkbox is already selected.")

    def element_is_displayed(self, path):
        demo = self.driver.find_element(By.XPATH, path).is_displayed()
        print(demo)
        time.sleep(1)

    # 网页单页基本操作
    def web_size(self, width, height):
        self.driver.set_window_size(width, height)

    def web_maxsize(self):
        self.driver.maximize_window()

    def web_scroll(self, path):  # 滚动到某个元素的位置
        element = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

    def web_scroll_top(self):  # 滚动到页面顶部
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def web_scroll_end(self, x=0):  # 滚动到页面底部
        js = 'window.scrollTo(%s,document.body.scrollHeight)' % x
        self.driver.execute_script(js)

    def mouse_move(self, path):
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH, path))

    # 网页跳转基本操作
    def web_open_new(self, url):  # 填入您需要网页的url地址
        self.main_web = self.driver.current_window_handle
        self.driver.get(url)
        time.sleep(3)

    def web_jump_remain(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def web_jump_next(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def web_jump_new(self):
        attempt = 5
        new_window_handle = None
        self.former_web = self.driver.current_window_handle
        while not new_window_handle and attempt > 0:
            for handle in self.driver.window_handles:
                if handle != self.former_web:
                    new_window_handle = handle
            attempt -= 1
            time.sleep(1)
        self.driver.switch_to.window(new_window_handle)
        print(self.driver.title)

    def web_jump_to(self, handle):
        self.driver.switch_to.window(handle)

    def web_jump_main(self):
        self.driver.switch_to.window(self.main_web)
        time.sleep(3)

    def web_jump_former(self):
        self.driver.switch_to.window(self.former_web)

    # 小狐狸基本操作
    def metamask_initialize(self):  # 网页MetaMask初次登录
        words = ['angry', 'elite', 'chair', 'laundry', 'fox', 'plate', 'desert', 'creek', 'essence', 'envelope',
                 'unfair', 'uniform']
        next_btn = self.driver.find_element(By.XPATH, "//*[@id='onboarding__terms-checkbox']")
        self.driver.execute_script("arguments[0].click();", next_btn)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button')
        self.driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(3)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

        time.sleep(3)
        next_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]")
        self.driver.execute_script("arguments[0].click();", next_btn)

        time.sleep(3)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        # 依次填入助记词登陆
        for index in range(len(words)):
            self.driver.find_element(By.ID, 'import-srp__srp-word-' + str(index)).send_keys(words[index])

        next_btn = self.driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[4]/div/button")
        self.driver.execute_script("arguments[0].click();", next_btn)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

        self.driver.find_element(By.XPATH,
                                 '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(
            self.password)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(
            self.password)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click()

        next_btn = self.driver.find_element(By.XPATH,
                                            "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/button")
        self.driver.execute_script("arguments[0].click();", next_btn)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

        next_btn = self.driver.find_element(By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button")
        self.driver.execute_script("arguments[0].click();", next_btn)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

        next_btn = self.driver.find_element(By.XPATH,
                                            "//*[@id='app-content']/div/div[2]/div/div/div/div[1]/div/ul/li[2]")
        self.driver.execute_script("arguments[0].click();", next_btn)

        next_btn = self.driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button')
        self.driver.execute_script("arguments[0].click();", next_btn)

    def metamask_login(self):  # MetaMask钱包弹窗登录
        main_window = self.driver.current_window_handle
        self.web_jump_new()
        # 输入密码
        self.element_input('/html/body/div[1]/div/div/div/div/form/div/div/input', self.password)
        # 点击<登录>按钮
        self.element_click('//*[@id="app-content"]/div/div/div/div/button')
        # 点击<下一步>按钮
        self.element_click('//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]')
        # 点击<连接>按钮
        self.element_click('//*[@id="app-content"]/div/div/div/div[2]/div[2]/div[2]/footer/button[2]')
        # 点击签名按钮
        self.element_click('//*[@id="app-content"]/div/div/div/div[4]/footer/button[2]')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def metamask_connect(self):  # MetaMask钱包弹窗登录
        main_window = self.driver.current_window_handle
        self.web_jump_new()
        # 输入密码
        self.element_input('/html/body/div[1]/div/div/div/div/form/div/div/input', self.password)
        # 点击<登录>按钮
        self.element_click('//*[@id="app-content"]/div/div/div/div/button')
        # 点击签名按钮
        self.element_click('//*[@id="app-content"]/div/div/div/div[4]/footer/button[2]')
        # 返回主页面
        self.driver.switch_to.window(main_window)
        time.sleep(3)

    # Venom基本操作
    def venom_login(self, password):
        phrase1 = ['usual', 'business', 'author', 'road', 'setup', 'urge', 'cricket', 'embrace', 'scorpion', 'inquiry']
        phrase2 = ['behind', 'border']
        # Signin with seed phrase
        self.element_click('//*[@id="root"]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/button')
        for index in range(len(phrase1)):
            self.element_input('//*[@id="headlessui-combobox-input-:r' + str(index) + ':"]', phrase1[index])
        self.element_input('// *[ @ id = "headlessui-combobox-input-:ra:"]', phrase2[0])
        self.element_input('// *[ @ id = "headlessui-combobox-input-:rb:"]', phrase2[1])
        self.element_click('//*[@id="confirm"]')
        self.web_jump_next()
        time.sleep(3)
        self.element_input('//*[@id="password"]/div[1]/input', password)
        self.element_input('//*[@id="password"]/div[2]/input', password)
        self.element_click('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/button[1]')
        self.web_jump_main()

    def venom_connect(self):
        self.web_jump_new()
        time.sleep(2)
        # Connect
        self.element_click('//*[@id="root"]/div/div/footer/div[2]/button')
        # 返回主页面
        self.web_jump_former()

    def venom_confirm_transcation(self, keyword):
        self.web_jump_new()
        time.sleep(2)
        self.element_input('//*[@id="root"]/div/div/div[2]/div/div[2]/input', keyword)
        self.element_click('//*[@id="root"]/div/div/div[2]/footer/div/button[2]')
        self.web_jump_former()

    def venom_mint(self, key):
        self.web_jump_new()
        self.element_input('//*[@id="root"]/div/div/div[2]/div/div[2]/input', key)
        self.element_click('//*[@id="root"]/div/div/div[2]/footer/div/button[2]/div')
        time.sleep(15)
        # Back to progects 按钮
        self.element_click('//*[@id="nft-9"]/button')
        # 返回主页面
        self.web_jump_main()

    # 推特基本操作
    def twitter_login(self, username, code):  # 推特登录
        # 跳转至推特页面
        self.web_jump_new()
        self.element_input('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label',
                           username)
        self.element_click('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
        self.element_input(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input',
            code)
        self.element_click(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div')
        self.web_jump_next()

    def twitter_authorize(self, username, code):  # 推特授权
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至推特页面
        self.web_jump_new()
        self.element_input('//*[@id="username_or_email"]', username)
        self.element_input('//*[@id="password"]', code)
        self.element_click('//*[@id="allow"]')
        time.sleep(5)
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_retweet(self):  # 推特转发
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至推特页面
        self.web_jump_new()
        # 点击retweet按钮
        self.element_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_post(self):  # 推特发帖
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至推特页面
        self.web_jump_new()
        # 点击post按钮
        self.element_click(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_post_button(self):  # 推特发帖(按钮形式)
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至推特页面
        self.web_jump_new()
        # 点击post按钮
        self.element_click('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div')

        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_follow(self):  # 推特关注
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至推特页面
        self.web_jump_new()
        # 点击follow按钮
        self.element_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
        # 返回主页面
        time.sleep(1)
        self.driver.switch_to.window(main_window)

    def twitter_like(self):  # 推特关注
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至推特页面
        self.web_jump_new()
        # 点击like按钮
        self.element_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    # 推特基本操作(包含登录)
    def twitter_login_and_retweet(self, username, code):  # 推特登录并转发
        # 标记主页面
        main_window = self.driver.current_window_handle
        time.sleep(2)
        # 跳转至推特页面
        self.web_jump_new()
        self.element_input('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label',
                           username)
        self.element_click('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
        self.element_input(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input',
            code)
        self.element_click(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div')
        self.web_jump_next()
        # 点击retweet按钮
        self.element_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_login_and_post(self, username, code):  # 推特登录并发帖
        # 标记主页面
        main_window = self.driver.current_window_handle
        time.sleep(2)
        # 跳转至推特页面
        self.web_jump_new()
        self.element_input('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label',
                           username)
        self.element_click('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
        self.element_input(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div['
            '3]/div/label/div/div[2]/div[1]/input',
            code)
        self.element_click(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div')
        self.web_jump_next()
        # 点击Post按钮
        self.element_click('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_login_and_follow(self, username, code):  # 推特登录并关注
        # 标记主页面
        main_window = self.driver.current_window_handle
        time.sleep(2)
        # 跳转至推特页面
        self.web_jump_new()
        self.element_input('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label',
                           username)
        self.element_click('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
        self.element_input(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input',
            code)
        self.element_click(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div')
        self.web_jump_next()
        # 点击Follow按钮
        self.element_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    def twitter_login_and_like(self, username, code):  # 推特登录并转发
        # 标记主页面
        main_window = self.driver.current_window_handle
        time.sleep(2)
        # 跳转至推特页面
        self.web_jump_new()
        self.element_input('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label',
                           username)
        self.element_click('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
        self.element_input(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input',
            code)
        self.element_click(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div')
        self.web_jump_next()
        # 点击like按钮
        self.element_click('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
        # 返回主页面
        self.driver.switch_to.window(main_window)

    # discord基本操作(大部分需要人工介入)
    def discord_login(self, username, code):  # discord登录
        # 跳转至discord页面
        self.web_jump_new()
        # 点击<已经拥有账号>按钮
        self.element_click('//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/button')
        # 跳转至login页面
        self.web_jump_next()
        self.element_input('//*[@id="uid_8"]', username)
        self.element_input('//*[@id="uid_10"]', code)
        self.element_click(
            '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]')
        self.web_jump_next()
        # 后续验证操作需要人工

    def discord_invite(self):  # discord登录后接受邀请
        # 标记主页面
        main_window = self.driver.current_window_handle
        # 跳转至discord页面
        self.web_jump_new()
        # 点击<接受邀请>按钮
        self.element_click('//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/section/div[2]/button/div')
        self.web_jump_next()
        # 点击<Complete>按钮
        self.element_click(
            '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div[2]/button')
        self.web_jump_remain()
        self.web_scroll(
            '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[3]/label/div[1]')
        self.element_click(
            '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[3]/label/div[1]')
        self.element_click('//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/button')

        # 返回主页面
        self.driver.switch_to.window(main_window)

    def close(self):  # 关闭网页
        self.driver.quit()
