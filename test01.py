
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 有头模式 打开谷歌浏览器
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.bilibili.com")
    # 打印 标题
    print(page.title())
    browser.close()