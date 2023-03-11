from playwright.sync_api import Page,expect
import re
# 无头模式运行 不会打开浏览器，控制台输出执行结果日志
def test_baidu(page:Page):
    page.goto("http://www.baidu.com")
    # 断言页面是否有“百度一下” 文本
    expect(page).to_have_title(re.compile("百度一下"))
    input_text = page.locator("#kw")
    input_text.fill("搜索关键字")
    get_search = page.locator("text=百度一下")
    get_search.click()