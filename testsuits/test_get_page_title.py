# coding = utf-8
import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_frontpage import FrontPage


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = FrontPage(self.driver)
        print(homepage.get_page_title())
        time.sleep(2)
