import re

import pytest
from playwright.async_api import Page


class AdminLoginTest:

    @pytest.fixture(scope="class", autouse=True)
    def before(self, page: Page):
        page.goto('http://testingedu.com.cn:8000/index.php/Home/user/login.html')

    @staticmethod
    def test_admin_login(page: Page):
        """
        登录
        """
        print("--登录开始--")
        page.fill('//input[@id="username"]', '13800138006')
        page.fill('//input[@id="password"]', '123456')
        page.fill('//input[@id="verify_code"]', '111')  # 验证码随意输入
        page.click('//a[@name="sbtbutton"]')
        print("--登录结束--")

    @staticmethod
    def test_admin_upload(page: Page):
        """
        上传头像
        """
        print("--上传头像开始--")
        page.wait_for_timeout(3000)
        page.goto('http://testingedu.com.cn:8000/Home/User/info.html')
        page.wait_for_timeout(3000)
        page.click('//img[@id="preview"]')  # 点击头像就会出现让上传的iframe 弹窗
        page.wait_for_timeout(3000)
        # playwright 先定位到（***）iframe(***)元素，紧接着再操作其他元素（上传按钮）和（保存按钮）
        # 区别于selenium，要先进入iframe再退出 ，playwright不需要退出
        page.frame_locator('//*[@id="layui-layer-iframe1"]'). \
            locator('//*[@id="filePicker"]/div[2]/input'). \
            set_input_files(r'C://Users//86130//Pictures//test.png')  # iframe元素再定位上传按钮再上传图片

        page.frame_locator('//*[@id="layui-layer-iframe1"]').locator('//*[@class="saveBtn"]').click()
        page.click('//input[@class="save"]')  # iframe元素再点击保存
        page.wait_for_timeout(3000)
        print("--上传头像结束--")

    @staticmethod
    def test_admin_add_consign(page: Page):
        """
        新增收件信息
        """
        print("--新增收件信息开始--")
        page.wait_for_timeout(3000)
        page.goto("http://testingedu.com.cn:8000/Home/User/address_list.html")
        page.wait_for_timeout(3000)
        page.click('//span[text()="增加新地址"]')
        page.fill('//input[@name="consignee"]', '深圳市宝安区')
        page.fill('//input[@name="mobile"]', '13988881111')
        page.fill('//input[@name="mobile"]', '13988881111')

        # （***）下拉框 select（***） : 和selenium 类似  有label文本值 和value的两种定位
        page.select_option('//select[@name="province"]', label="湖南省")
        page.select_option('//select[@name="city"]', label="长沙市")
        page.select_option('//select[@name="district"]', value="25582")
        page.select_option('//select[@name="twon"]', value='25585')
        page.fill('//input[@name="address"]', '测试添加地址')
        page.fill('//input[@name="zipcode"]', '3373330976@qq.com')
        page.click("//a[@id='address_submit']")
        # 删除收件人为"深圳市宝安区" 对应的一条收件信息  子节点 -> 父节点
        page.click('//span[text()="深圳市宝安区"]/../..//a[text()="删除"]')
        print("--新增收件信息结束--")

    @staticmethod
    def test_admin_searchGoods_addBuy(page: Page):
        """
        搜索商品，加入购物车，提交订单
        """
        page.wait_for_timeout(3000)
        print("--搜索商品，加入购物车，提交订单 开始--")
        # 输入框搜索“手机” 的商品
        page.fill('//*[@id="q"]', '手机')
        page.click('//*[@id="sourch_form"]/a')
        # 点进“中国移动198号段” 这个商品 ，并加入购物车、提交订单
        page.wait_for_timeout(2000)
        page.click('//a[contains(text(),"中国移动198号段")]')
        page.wait_for_timeout(3000)
        page.click('//*[@id="join_cart"]')
        page.wait_for_timeout(3000)
        page.click('//*[@id="layui-layer1"]/span/a')
        page.wait_for_timeout(3000)
        page.hover('//span[text()="我的购物车"]')
        page.wait_for_timeout(3000)
        page.click('//a[@class="c-btn"]')
        page.wait_for_timeout(3000)
        page.click('//a[text()="去结算"]')
        page.wait_for_timeout(3000)
        page.click('//button[@class="checkout-submit"]')
        page.wait_for_timeout(3000)
        # 订单号元素定位的文本值
        text = page.locator('//p[@class="succ-p"]').text_content()
        # print(text)
        # 获取订单号 正则提取18位数字
        billNo = re.findall(r'\d{18}', text)[0]
        print("获取订单号", billNo)
        print("--搜索商品，加入购物车，提交订单 结束--")


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
