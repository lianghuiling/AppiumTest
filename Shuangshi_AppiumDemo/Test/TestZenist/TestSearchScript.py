# -*- encoding:utf8 -*-
__author__ = 'zenist'

import unittest

from Src.driver.driver import Driver

import settings

class RES():
    #首页， 搜索图片ID
    ID_SEARCH_ENTRY_IMG = 'com.esbook.reader:id/iv_title_search_main'
    #搜索页, 搜索框ID
    ID_SEARCH_INPUT = 'com.esbook.reader:id/et_search'
    #搜索页，搜索框确定按钮
    ID_SEARCH_SUBMIT = 'com.esbook.reader:id/btn_search_result_more'
    #搜索页，搜索结果文字
    ID_SEARCH_RST_TEXT = 'com.esbook.reader:id/tv_search_result_word'
    #搜索页，搜索结果数量
    ID_SEARCH_RST_COUNT = 'com.esbook.reader:id/tv_search_result_counter'
    #搜索页，搜索历史框标题
    ID_SEARCH_HISTORY = 'com.esbook.reader:id/tv_title_history_search_view'
    #搜索页，清空历史文字
    ID_CLEAN_HISTORY = 'com.esbook.reader:id/tv_clear_history_search_view'
    #搜索页，清空历史记录弹窗确认
    ID_CLEAN_CONFIRM = 'com.esbook.reader:id/publish_stay'


class TestSearch(unittest.TestCase):

    #SetUp测试环境
    def setUp(self):
        '''获取driver对象，进入被测页面'''
        self._driver = Driver().get_driver()
        self.__init_serch_activity()

    #TearDown测试环境
    def tearDown(self):
        '''重置driver'''
        Driver().reset_driver()

    #初始化方法,启动搜索页面
    def __init_serch_activity(self):
        '''获取并点击位于首页的搜索入口图标'''
        _ele_search_img = self._driver.find_element_by_id(RES.ID_SEARCH_ENTRY_IMG)
        _ele_search_img.click()
        #页面常用组建
        self._ele_search_input = self._driver.find_element_by_id(RES.ID_SEARCH_INPUT)

    #C-11: 验证搜索输入框中的文字
    def test_11_defaultTextOfSearchInput(self):
        _exp_text = '搜索书名或作者'
        _act_text = self._ele_search_input.text.encode('utf8')
        assert _exp_text == _act_text, \
            '搜索输入框中的文字与设计不符，exp=%s, act=%s' %(_exp_text, _act_text)

    #C-12: 验证搜索,搜索：烦人修仙传
    def test_12_searchTargetBook(self):
        _exp_bookName = u'凡人修仙传'
        self._ele_search_input.send_keys(_exp_bookName)
        self._driver.find_element_by_id(RES.ID_SEARCH_SUBMIT).click()
        _act_rstText = self._driver.find_element_by_id(RES.ID_SEARCH_RST_TEXT).text
        assert _act_rstText == _exp_bookName, \
            '搜索跳转后的输入框文字与所输入的书名不一致, exp=%s, axt=%s' % (_exp_bookName, _act_rstText)

        _act_rstCount = self._driver.find_element_by_id(RES.ID_SEARCH_RST_COUNT).text
        assert _act_rstCount != u'0本', \
             '搜索跳转后的输入框数量显示小于1'

    #C-13: 验证搜索历史，前置case:C-12
    def test_13_searchHistoryTitle(self):
        try:
            _ele_searchHistory = self._driver.find_element_by_id(RES.ID_SEARCH_HISTORY)
            print _ele_searchHistory.text
        except:
            assert False, \
                '未发现搜索历史栏目'

    #C-14: 清空搜索记录， 前置case：C-12
    def test_13_cleanHistoryList(self):
        _ele_cleanHistory = self._driver.find_element_by_id(RES.ID_CLEAN_HISTORY)
        _ele_cleanHistory.click()
        self._driver.find_element_by_id(RES.ID_CLEAN_CONFIRM).click()

        try:
            _ele_cleanHistory = self._driver.find_element_by_id(RES.ID_SEARCH_HISTORY)
            print _ele_cleanHistory.text
        except:
            return

        assert True, \
                '发现清空搜索记录按钮'

    #C-13: 验证每次进入获取的热搜词贴都是随机不同的
    def test_21_hotWordsTag(self):
        _hot_words_id = 'com.esbook.reader:id/tv_hot_word_search_item'
        _hot_words_tags = self._driver.find_elements_by_id(_hot_words_id)
        for _hot_wods in _hot_words_tags:
            print _hot_wods.text

        self._driver.back()
        self._driver.back()
        _ele_search_img = self._driver.find_element_by_id(RES.ID_SEARCH_IMG_MAIN)
        _ele_search_img.click()

        _hot_words_tags = self._driver.find_elements_by_id(_hot_words_id)
        for _hot_wods in _hot_words_tags:
            print _hot_wods.text


