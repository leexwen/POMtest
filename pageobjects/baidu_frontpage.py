# coding=utf-8
from framework.base_page import BasePage


class FrontPage(BasePage):
    input_box = "id=>kw"
    search_submit = "xpath=>//*[@id='su']"
    # 百度新闻入口
    news = 'xpath=>//*[@id="s-top-left"]/a[1]'



    def type_search(self, text):
        self.type(self.input_box, text)
        self.sleep(2)

    def send_submit_btn(self):
        self.click(self.search_submit)
        self.sleep(2)

    def click_news(self):
        self.click(self.news)
        self.sleep(2)

    def clear_seaech(self):
        self.clear(self.input_box)
        self.sleep(2)




