# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time,sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

class YoudaoIdeTest(unittest.TestCase):
    '''有道翻译测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com/"

    
    def test_youdao_ide(self):
        '''中英翻译测试'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"自动化测试报告")
        driver.find_element_by_css_selector("button").click()
        time.sleep(5)
        self.assertEqual(u"【自动化测试报告】", driver.title)

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()