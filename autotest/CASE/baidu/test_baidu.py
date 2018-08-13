#encoding=utf-8
from selenium import webdriver
import time,unittest, re,sys
from HTMLTestRunner import HTMLTestRunner
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
'''
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

class Test(unittest.TestCase):
	'''百度登录'''
	@classmethod
	def setUpClass(self):
		self.driver=webdriver.Firefox()
		#driver=webdriver.Chrome()
		self.driver.get("http://www.baidu.com")
	def test_login(self):
		self.driver.add_cookie({u'name':u'BDUSS', u'value':u'自己的'})
		time.sleep(3)
		self.driver.refresh()
	
	def test_login_successful(self):
		text=self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/a[7]/span").text#xpath必须双引号
		#text=self.driver.find_element_by_id('s_username_top').text
		target='Dysania_GGG'
		str(text)
		#print text
		self.assertEqual(text,target)
	
	@classmethod
	def tearDownClass(self):
		self.driver.quit()
if __name__=='__main__':
	#unittest.main()
	#构造测试套件
    testsuit = unittest.TestSuite()
    testsuit.addTest(Test("test_login"))
    testsuit.addTest(Test("test_login_successful"))
    testsuit.addTest(Test("test_youdao_ide"))
    #按照一定格式获取当前时间
    now = time.strftime("%Y%m%d_%H%M%S")
    #将当前时间加入到报告文件名称中
    filename = './'+now+'result.html'
    #定义测试报告存放路径
    fp = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='自动化测试报告',
                            description='用例执行情况：')
    runner.run(testsuit)
    #关闭测试报告
    fp.close()
