# -*- encoding:utf-8 -*-
__author__ = 'Sophia'

import unittest
from Src.driver.driver import Driver
# from Test.tt import res


class RES():
    # 登录账号
    ID_ASSIST_LOGIN_ACCOUNT = 'com.xes.drawpanel:id/login_username_et'
    #登录密码
    ID_ASSIST_LOGIN_PASSWORD = 'com.xes.drawpanel:id/login_passwd_et'
    #登录按钮
    ID_ASSIST_LOGIN_DENGLU = 'com.xes.drawpanel:id/login_login_tv1'

class TestLogin(unittest.TestCase):
    # SetUp测试环境
    def setUp(self):
        '''获取driver对象，登录应用'''
        self._driver = Driver().get_driver
        self.__init_login_activity()


    #TearDown测试环境
    def tearDown(self):
        '''重置driver'''
        Driver().reset_driver()
         # 关闭当前session，仅供单条case测试使用，多条的时候注释掉此行
        Driver().close_driver()

    #初始化方法，进入我的班级页面
    def __init_login_activity(self):
        # 登录双师应用
        self._driver = Driver().get_driver()
        _ele_login_account = self._driver.find_element_by_id(RES.ID_ASSIST_LOGIN_ACCOUNT)
        _ele_login_password = self._driver.find_element_by_id(RES.ID_ASSIST_LOGIN_PASSWORD)
        _ele_login_denglu = self._driver.find_element_by_id(RES.ID_ASSIST_LOGIN_DENGLU)

        if _ele_login_account.text == "18211155659":
            _ele_login_denglu.click()
        else:
            _ele_login_account.send_keys("18211155659")
            _ele_login_password.send_keys("123456")
            _ele_login_denglu.click()

    def test_01(self):
        print "test11111111111111111111"



