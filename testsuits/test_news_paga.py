# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_news_page import NewsHomePage
from pageobjects.baidu_frontpage import FrontPage



class ViewNews(unittest.TestCase):
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    # 测试新闻页面
    def test_view_news_views(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        # 百度首页点击新闻
        baidupage = FrontPage(self.driver)
        baidupage.click_news()
        baidupage.switch_windows()# 调用切换窗口方法
        # 新闻页
        newspage = NewsHomePage(self.driver)
        newspage.get_windows_img()# 调用截图方法
        newspage.type_news_search_frame('selenium')
        newspage.clear_news_search_frame()
        newspage.click_newspage_link()
        newspage.sleep(2)
        newspage.switch_windows()
        newspage.get_windows_img()


if __name__ == '__main__':
    unittest.main()
