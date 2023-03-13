import pytest
from playwright.async_api import Page
from page.baidu.baidu_search_page import BaiduSearchPage

from common.tools import Tools

# 利用 global 简化 page 使用
baiduSearchPage: BaiduSearchPage

class BaiduSearchTest:

    @pytest.fixture(scope="class", autouse=True)
    def before(self, page: Page):
        global baiduSearchPage
        baiduSearchPage = BaiduSearchPage(page)


    @pytest.fixture()
    def fixtures(self):
        yield Tools.get_fixtures("baidu_search")

    @staticmethod
    def test_baidu_search(page: Page, env: dict, fixtures):

        baiduSearchPage.open()
        baiduSearchPage.search_keywords(fixtures['kerwords'])
        baiduSearchPage.page.wait_for_timeout(2000)
        assert baiduSearchPage.page.title() == f'{fixtures["kerwords"]}_百度搜索'

if __name__ == '__main__':
    pytest.main(["-v", "-s"])
