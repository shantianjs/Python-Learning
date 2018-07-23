from selenium import webdriver
import time
import threading
import multiprocessing
import os

def baidu_search():
	browser = webdriver.Chrome('E://tem/chromedriver.exe')
	url = r'http://www.baidu.com'
	browser.get(url=url)
	browser.maximize_window()
	browser.find_element_by_id('kw').send_keys('python')
	browser.find_element_by_id('su').submit()
	time.sleep(5)
	browser.find_element_by_id('kw').clear()
	browser.find_element_by_id('kw').send_keys('京东')
	browser.find_element_by_tag_name('submit').click()
	time.sleep(5)
	browser.quit()

def get_screenshot(url):
	browser = webdriver.Chrome('E://tem/chromedriver.exe')
	print(f"get {url}")
	browser.get('http://' + url)
	browser.save_screenshot(f'webpage-{url[4:-4]}.png')
	browser.quit()

def multi_thread(urls):

	browser = webdriver.Chrome("E://tem/chromedriver.exe")
	browser.set_window_size(800,600)
	browser.set_window_position(100,0)
	ths = []
	for i,url in enumerate(urls,1):
		th = threading.Thread(target=get_screenshot,args=(url,))
		th.start()
		ths.append(th)
	for th in ths:
		th.join()

	time.sleep(5)
	browser.quit()

def multi_process(urls):
	browser = webdriver.Chrome('E://tem/chromedriver.exe')
	pool = multiprocessing.Pool(processes=4)
	pool.starmap_async(get_screenshot,urls)

def login_jd():
	browser = webdriver.Chrome('E://tem/chromedriver.exe')
	browser.get('http://www.jd.com')
	browser.maximize_window()
	browser.find_element_by_id('ttbar-login').click()
	time.sleep(1)
	browser.find_element_by_class_name('login-tab-r').click()
	time.sleep(3)
	browser.find_element_by_id('loginname').send_keys(f'{os.environ.get(jd-user)}')
	browser.find_element_by_id('nloginpwd').send_keys(f'{os.environ.get(jd-pw)}')
	browser.find_element_by_class_name('login-btn').click()
	time.sleep(10)
	browser.quit()



urls = ['www.sina.com',
	        'www.sohu.com',
	        'www.eastmoney.com',
	        'www.newone.com.cn',
	        'www.baidu.com',]

for i in os.walk('e://tools'):
	print(i)