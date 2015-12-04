# -*- encoding:utf8 -*-
__author__ = 'LHL'

import unittest

from Src.driver.driver import Driver


class RES():
    # 登录页面用户名输入框
    ID_LOGIN_USERNAME = 'com.xes.drawpanel:id/login_username_et'
    # 登录页面密码输入框
    ID_LOGIN_PASSED = 'com.xes.drawpanel:id/login_passwd_et'
    # 登录页面登录按钮
    ID_LOGIN_BUTTON = 'com.xes.drawpanel:id/login_login_tv1'
    # 批改端版本号
    ID_VERSION_NO = 'com.xes.drawpanel:id/versions_tv'
    # 版本号
    VERSION = 'V3.0'
    # 用户名
    USERNAME = '13522319357'
    # USERNAME = '18211155659'
    # 密码
    PWD = '123456'

    # driver = Driver().get_driver()

    @classmethod
    def edittextclear(cls, text):
        '''
       请除EditText文本框里的内容
        @param:text 要清除的内容
        '''
        # 光标移到末尾
        cls.login_account().driver.keyevent(123)
        # 循环删除
        for i in range(0, len(text)):
            Driver().get_driver().keyevent(67)

    @classmethod
    def login_account(cls):
        driver = Driver().get_driver()
        __username = driver.find_element_by_id(RES.ID_LOGIN_USERNAME)
        # print 'username' + __username.text
        __pwd = driver.find_element_by_id(RES.ID_LOGIN_PASSED)
        # print 'pwd' + __pwd.text
        if __username.text == '输入账号. 正在编辑。':
            __username.send_keys(RES.USERNAME)
        if __pwd.text == 'Enter password.. 轻敲两次以编辑。':
            __pwd.send_keys(RES.PWD)
        driver.find_element_by_id(RES.ID_LOGIN_BUTTON).click()
        try:
            _ele_mywork = driver.find_element_by_name('我的工作')
            # print '登录成功'
        except:
            assert False, \
                '登录失败'


class TestLogin(unittest.TestCase):
    # SetUp测试环境
    def setUp(self):
        '''获取driver对象，进入被测页面'''
        self._driver = Driver().get_driver()

    # TearDown测试环境
    def tearDown(self):
        '''重置driver'''
        Driver().reset_driver()

    # C-11: 验证登录用户名输入框中的文字
    def test_11_defaultTextOfLoginNameInput(self):
        _exp_username_text = '输入账号. 正在编辑。'
        _act_username_text = self._driver.find_element_by_id(RES.ID_LOGIN_USERNAME).text.encode('utf8')
        print _act_username_text
        assert _exp_username_text == _act_username_text, \
            '登录用户名输入框中的文字与设计不符，exp=%s, act=%s' % (_exp_username_text, _act_username_text)

    # C-12: 验证登录密码输入框中的文字
    def test_12_defaultTextOfLoginPwdInput(self):
        _exp_pwd_text = 'Enter password.. 轻敲两次以编辑。'
        _act_pwd_text = self._driver.find_element_by_id(RES.ID_LOGIN_PASSED).text.encode('utf8')
        print _act_pwd_text
        assert _exp_pwd_text == _act_pwd_text, \
            '登录密码输入框中的文字与设计不符，exp=%s, act=%s' % (_exp_pwd_text, _act_pwd_text)

    #C-13: 验证登录按钮上的文字
    def test_13_defaultTextOfLoginButtonText(self):
        _exp_Login_text = '登陆'
        _act_login_text = self._driver.find_element_by_id(RES.ID_LOGIN_BUTTON).text.encode('utf8')
        print _act_login_text
        assert _exp_Login_text == _act_login_text, \
            '登录按钮上的文字与设计不符，exp=%s, act=%s' % (_exp_Login_text, _act_login_text)

    #C-14: 验证版本号
    def test_14_defaultTextOfVersionText(self):
        _exp_version_text = RES.VERSION
        _act_version_text = self._driver.find_element_by_id(RES.ID_VERSION_NO).text.encode('utf8')
        print _act_version_text
        assert _exp_version_text == _act_version_text, \
            '版本号与期望不符，exp=%s, act=%s' % (_exp_version_text, _act_version_text)

    #C-15: 验证登录，输入用户名密码点登录
    def test_15_Login(self):
        self._driver.find_element_by_id(RES.ID_LOGIN_USERNAME).send_keys(RES.USERNAME)
        self._driver.find_element_by_id(RES.ID_LOGIN_PASSED).send_keys(RES.PWD)
        self._driver.find_element_by_id(RES.ID_LOGIN_BUTTON).click()
        try:
            _ele_mywork = self._driver.find_element_by_name("我的工作")
            print '登录成功'
        except:
            assert False, \
                '登录失败'


