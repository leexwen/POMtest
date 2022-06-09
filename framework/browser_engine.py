# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger
from webdriver_manager.chrome import ChromeDriverManager




logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    def __init__(self, driver):
        self.driver = driver

    # 从 config.ini 文件中读取浏览器类型，返回驱动
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # print(file_path)
        config.read(file_path,encoding='UTF-8'), # 如果代码有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        logger.info("选择的 %s 浏览器." % browser)
        url = config.get("testServer", "URL")
        logger.info("测试服务器地址 url 是: %s" % url)

        # 判断config.ini 文件的浏览器类型
        if browser == "Firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            logger.info("启动 Firefox 浏览器.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            logger.info("启动 Chrome 浏览器.")
        elif browser == "IE":
            driver = webdriver.Ie(IEDriverManager().install())
            logger.info("启动 IE 浏览器.")

        driver.get(url)
        logger.info("打开 url: %s" % url)
        driver.maximize_window()
        logger.info("最大化当前窗口.")
        driver.implicitly_wait(10)
        logger.info("设置隐式等待 10 秒.")
        return driver

    def quit_browser(self):
        logger.info("关闭并退出浏览器.")
        self.driver.quit()
