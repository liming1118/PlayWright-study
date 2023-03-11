"""
xpath 浏览器控制台调式  $x("//span[@id='s-usersetting-top' and @name='tj_settingicon']")
  尽量不使用绝对路径 /
  尽量减少路径级别
  尽量不使用下标

"""
from playwright.sync_api import sync_playwright

with sync_playwright()  as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto("http://www.baidu.com")
    # 单个属性定位：
    text1 = page.locator("//span[@id='s-usersetting-top']").text_content()
    print(text1)
    #   多个属性定位
    text2 = page.locator("//span[@id='s-usersetting-top' and @name='tj_settingicon']").text_content()
    print(text2)
    #   通过父节点定位
    text3 = page.locator("//div[@id='u1']/span").text_content()
    print(text3)
    #   通过下标
    text4 = page.locator("//div[@id='s-top-left']/a[1]").text_content()
    print(text4)
    #   通过 子节点 -> 找父节点  ../
    text5 = page.locator("//a[@name='tj_fanyi']/div/../../../../../a[1]").text_content()
    print(text5)
    #   通过文本
    text6 = page.locator("//a[text()='新闻']").text_content()
    print(text6)
    #   通过模糊文本
    text7 = page.locator("//a[contains(text(),'hao')]").text_content()
    print(text7)




