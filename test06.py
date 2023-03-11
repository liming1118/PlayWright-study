from playwright.sync_api import sync_playwright
import re

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False,slow_mo=1000)
# playwrigth context 方便多页面管理 上下文
context = browser.new_context()
page = context.new_page()
page.goto('http://testingedu.com.cn:8000/index.php/Home/user/login.html')

"""
登录
"""
print("--登录开始--")
page.fill('//input[@id="username"]','13800138006')
page.fill('//input[@id="password"]','123456')
page.fill('//input[@id="verify_code"]','111')  # 验证码随意输入
page.click('//a[@name="sbtbutton"]')
print("--登录结束--")
"""
上传头像
"""
print("--上传头像开始--")
page.goto('http://testingedu.com.cn:8000/Home/User/info.html')
page.click('//img[@id="preview"]')  # 点击头像就会出现让上传的iframe 弹窗

# playwright 先定位到（***）iframe(***)元素，再操作其他元素（上传按钮）和（保存按钮）
# 区别于selenium，要先进入iframe再退出 ，playwright不需要退出
page.frame_locator('//*[@id="layui-layer-iframe1"]').\
    locator('//*[@id="filePicker"]/div[2]/input').\
    set_input_files(r'C://Users//86130//Pictures//test.png') # iframe元素再定位上传按钮再上传图片

page.frame_locator('//*[@id="layui-layer-iframe1"]').locator('//*[@class="saveBtn"]').click()
page.click('//input[@class="save"]') # iframe元素再点击保存
print("--上传头像结束--")
"""
新增收件信息  
"""
print("--新增收件信息开始--")
page.goto("http://testingedu.com.cn:8000/Home/User/address_list.html")
page.click('//span[text()="增加新地址"]')
page.fill('//input[@name="consignee"]','深圳市宝安区')
page.fill('//input[@name="mobile"]','13988881111')
page.fill('//input[@name="mobile"]','13988881111')

# （***）下拉框 select（***） : 和selenium 类似  有label文本值 和value的两种定位
page.select_option('//select[@name="province"]',label="湖南省")
page.select_option('//select[@name="city"]',label="长沙市")
page.select_option('//select[@name="district"]',value="25582")
page.select_option('//select[@name="twon"]',value='25585')
page.fill('//input[@name="address"]','测试添加地址')
page.fill('//input[@name="zipcode"]','3373330976@qq.com')
page.click("//a[@id='address_submit']")
# 删除收件人为"深圳市宝安区" 对应的一条收件信息  子节点 -> 父节点
page.click('//span[text()="深圳市宝安区"]/../..//a[text()="删除"]')
print("--新增收件信息结束--")

"""
搜索商品，加入购物车，提交订单
"""
print("--搜索商品，加入购物车，提交订单 开始--")
# 输入框搜索“手机” 的商品
page.fill('//*[@id="q"]','手机')
page.click('//*[@id="sourch_form"]/a')
# 打印所有“手机”的商品名称
# goods = page.query_selector_all('//div[@class="shop-list-splb p"]//div[@class="shop_name2"]/a')
# for good in goods:
#     print(good.text_content().strip())  # 名称去空格
# 点进“中国移动198号段” 这个商品 ，并加入购物车、提交订单
page.click('//a[contains(text(),"中国移动198号段")]')
page.click('//*[@id="join_cart"]')
page.click('//*[@id="layui-layer1"]/span/a')
page.hover('//span[text()="我的购物车"]')
page.click('//a[@class="c-btn"]')
page.click('//a[text()="去结算"]')
page.click('//button[@class="checkout-submit"]')
# 订单号元素定位的文本值
text = page.locator('//p[@class="succ-p"]').text_content()
# print(text)
# 获取订单号 正则提取18位数字
billNo = re.findall(r'\d{18}',text)[0]
print(billNo)
print("--搜索商品，加入购物车，提交订单 结束--")
"""
打开新标签页
"""
print("--打开新标签页 开始--")
# playwrigth 用 context 多页面管理上下文  ,不同于selenium 获取(***)多窗口handle句柄切换(***)
with context.expect_page() as new_page_info:
    # 点击顶部我的订单 ，会打开新标签页
    page.click('a[target="_blank"]')
# 获取新页面“我的订单页”
new_page = new_page_info.value
new_page.wait_for_load_state() # 用于等待页面加载到指定状态
print("新标签页标题,"+new_page.title()) # 新标签页标题

# 根据{订单号} 找到取消并点击取消  子节点 -> 父节点
new_page.click('//em[text()="{}"]/../..//a[text()="取消订单"]'.format(billNo))
# 父节点-> 子节点点击取消
new_page.click('//div[@class="layui-layer-btn layui-layer-btn-"]//a[text()="确定"]')
# 刷新页面
new_page.reload()
print("--打开新标签页 结束--")

browser.close()

