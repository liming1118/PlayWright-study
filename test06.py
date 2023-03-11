from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False,slow_mo=1000)
# 方便多页面管理
context = browser.new_context()
page = context.new_page()
page.goto('http://testingedu.com.cn:8000/index.php/Home/user/login.html')

page.fill('//input[@id="username"]','13800138006')
page.fill('//input[@id="password"]','123456')
page.fill('//input[@id="verify_code"]','111')
page.click('//a[@name="sbtbutton"]')

page.goto('http://testingedu.com.cn:8000/Home/User/info.html')
page.click('//img[@id="preview"]')

browser.close()