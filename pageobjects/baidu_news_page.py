# coding=utf-8
from framework.base_page import BasePage

class NewsHomePage(BasePage):
    news_search_frame = 'name=>word'
    news_highlights = 'xpath=>//*[@id="pane-news"]/div/ul/li[1]/strong/a'

    def type_news_search_frame(self,text):
        self.type(self.news_search_frame, text)
        self.sleep(2)

    def clear_news_search_frame(self):
        self.clear(self.news_search_frame)
        self.sleep(2)

    def click_newspage_link(self):
        self.click(self.news_highlights)
        self.sleep(2)

