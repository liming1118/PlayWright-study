
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 有头模式 打开谷歌浏览器
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.bilibili.com")
    # 打印 标题
    print(page.title())
    browser.close()

"""
例子中使用了 with as 语句，with 用于上下文对象的管理，
无论运行期间是否抛出异常，它能够帮助我们自动分配并且释放 Playwright 的资源。
"""