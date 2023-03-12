import  re
from playwright.sync_api import sync_playwright

"""
playwright 的特有的定位方式
"""
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto("http://www.baidu.com")

    # page.get_by_alt_text()  # img的 alt文本
    # page.get_by_label()  # 输入框
    # page.get_by_placeholder() # 输入框
    # page.get_by_role() # 自定义组件上 如：element-ui ,html没有这个属性 ，可以用这个
    # page.get_by_text() # 文本定位
    # page.get_by_title()  # 标题定位
