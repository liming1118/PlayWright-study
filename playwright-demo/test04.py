"""css 元素定位：  控制台调试：如：$('#kw')

id选择器
class选择器
标签选择器（纯标签容易太多，一般配合使用）
层级选择器（适用于难以定位）

"""
from playwright.sync_api import sync_playwright

with sync_playwright()  as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=2000)
    page = browser.new_page(no_viewport=True)
    page.goto("http://www.baidu.com")

    page.locator('#kw').fill("id选择")
    page.locator('.s_ipt').fill('class选择器')
    page.locator('input.s_ipt').fill('标签选择器+class选择')
    page.locator('input#kw').fill('标签选择器+id选择')
    page.locator('div > form > span > input.s_ipt').fill('层级选择')
