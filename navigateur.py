from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_cookie3 import firefox
from browser_cookie3 import chrome

class Navigator_local_chrome:
	def __init__(self):
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument("--headless")
		self.chrome_options.add_argument("--mute-audio")
		self.chrome_options.add_argument('--log-level=3')
		# self.chrome_options.add_argument("--remote-debugging-port=12345") # select a port
		# self.chrome_options.add_argument('--incognito')
		# self.chrome_options.add_argument("start-maximized")
		self.chrome_options.add_argument("window-size=1920,1080")
		self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
		self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
		self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.chrome_options.add_experimental_option("useAutomationExtension", False)
		# find the path to the extension in the chrome store https://crxextractor.com/
		path_to_extension = r"ublock/uBlock-Origin.crx"
		self.chrome_options.add_extension(path_to_extension)
		self.service = webdriver.ChromeService(executable_path="chromedriver-win64/chromedriver.exe")
		# A telecharger ici : https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
		self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options) # add service=self.service, if you want to use a specific version of chrome in local mode, else it will use the default chrome installed on your computer
		self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		self.wait = WebDriverWait(self.driver, 30)

	def get_url(self, url):
		self.driver.get(url)
		self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

	def refresh(self):
		self.driver.refresh()

	def close(self):
		self.driver.quit()

	def open_newtab(self, url):
		self.driver.switch_to.new_window('tab')
		self.get_url(url)

	def import_cookies(self, cookies):
		if cookies == "chrome":
			self.cookies = chrome()
		elif cookies == "firefox":
			self.cookies = firefox()
		else:
			print("Merci de renseigner le bon navigateur (chrome ou firefox) pour importer les cookies")
			exit()

	def test(self):
		self.get_url("https://adblock-tester.com/")
		time.sleep(5)
		self.driver.save_screenshot("addtest1.png")
		self.get_url("https://adblock-tester.com/")
		time.sleep(5)
		self.driver.save_screenshot("addtest2.png")
	

class Navigator_vps_docker:
	def __init__(self):
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument("--mute-audio")
		self.chrome_options.add_argument('--log-level=3')
		# self.chrome_options.add_argument('--incognito')
		self.chrome_options.add_argument("start-maximized")
		self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
		self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")
		self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
		self.chrome_options.add_experimental_option("useAutomationExtension", False)
		self.driver = webdriver.Remote("http://172.25.0.5:4444", options=self.chrome_options)
		self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		self.wait = WebDriverWait(self.driver, 20)

	def get_url(self, url):
		self.driver.get(url)
		self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

	def refresh(self):
		self.driver.refresh()

	def close(self):
		self.driver.quit()

	def open_newtab(self, url):
		self.driver.switch_to.new_window('tab')
		self.get_url(url)

	def import_cookies(self, cookies):
		if cookies == "chrome":
			self.cookies = chrome()
		elif cookies == "firefox":
			self.cookies = firefox()
		else:
			print("Merci de renseigner le bon navigateur (chrome ou firefox) pour importer les cookies")
			exit()

	def test(self):
		self.get_url("https://adblock-tester.com/")
		time.sleep(5)
		self.driver.save_screenshot("addtest1.png")
		self.get_url("https://adblock-tester.com/")
		time.sleep(5)
		self.driver.save_screenshot("addtest2.png")


if __name__ == "__main__":

	navigator = Navigator_local_chrome()
	navigator.test()



