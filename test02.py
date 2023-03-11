from playwright.sync_api import sync_playwright
"""
浏览器操作 窗口大小 前进 后退  重刷
"""
with sync_playwright() as p:
    # 浏览器谷歌参数（官方文档） 使窗口最大化  设置每一步操作都延时3s
    browser = p.chromium.launch(headless=False, args=["--start-maximized"], slow_mo=3000)
    # 使得playwright默认窗口失效  windows电脑
    page = browser.new_page(no_viewport=True)
    # mac 只能设置屏幕像素大小
    # page = browser.new_page(no_viewport={"width": 1920, "height": 1080})
    page.goto("http://www.zhihu.com")
    # 打印 标题
    print(page.title())
    page.get_by_text("开通机构号").click()
    page.go_back()
    page.go_forward()
    page.reload()
    browser.close()
