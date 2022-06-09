# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import locale
from common.SendEmail import SendEmail

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
locale.setlocale(locale.LC_CTYPE, 'Chinese')
# 获取系统当前时间
now = time.strftime("%Y年-%m月-%d日-%H时_%M分_%S秒", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + ".html"

# 构建suite
suite = unittest.TestLoader().discover("testsuits")

if __name__ == '__main__':
    # 测试报告存放位置
    test_reports_address = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    print('test_reports_address:', test_reports_address)
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    with open(HtmlFile, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"项目测试报告", description=u"用例测试情况")
        # 开始执行测试套件
        runner.run(suite)
    time.sleep(6)
    # 查找最新生成的测试报告地址
    new_report_address = SendEmail().acquire_report_address(test_reports_address)
    # 自动发送邮件
    SendEmail().send_email(new_report_address)

