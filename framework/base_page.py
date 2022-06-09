# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os.path
from framework.logger import Logger


# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器并结束测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("在当前页面点击前进.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("点击返回当前页面.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒." % seconds)


    # 切换窗口的方法
    def switch_windows(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        logger.info("切换新的窗口")

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器.")
        except NameError as e:
            logger.error("无法退出浏览器 %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y年%m月%d日%H时%M分%S秒', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("已截取屏幕截图并保存到文件夹 : /screenshots")
        except NameError as e:
            logger.error("截屏失败! %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element(By.ID,selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element(By.ID,selector_value)
                logger.info("找到了元素 %s "
                            " %s 成功  元素为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没有这样的元素: %s" % e)
                self.get_windows_img()  # 截图
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element(By.NAME,selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by(By.CLASS_NAME,selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT,selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT,selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element(By.TAG_NAME,selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element(By.XPATH,selector_value)
                logger.info("找到了元素 %s "
                            " %s 成功  元素为: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没有这样的元素: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_elementr(By.CSS_SELECTOR,selector_value)
        else:
            raise NameError("请输入有效类型的定位元素.")

        return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info(" \' %s \' 类型在输入框中" % text)
        except NameError as e:
            logger.error("输入框输入失败 %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("输入前清除输入框中的文本.")
        except NameError as e:
            logger.error("无法在输入框中清除 %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("元素 \' %s \' 被点击." % el.text)
        except NameError as e:
            logger.error("无法单击元素 %s" % e)

    # 获取网页标题
    def get_page_title(self):
        logger.info("当前页面标题是 %s" % self.driver.title)
        return self.driver.title


    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("休眠 %d 秒" % seconds)
