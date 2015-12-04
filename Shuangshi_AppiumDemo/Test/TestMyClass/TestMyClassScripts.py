# -*- encoding:utf8 -*-
__author__ = 'LHL'

import unittest
import sys
from Src.driver.driver import Driver
from Test.TestLogin.TestLoginScript import RES as LRES
# from Test.TestDrawpanel.TestDrawpanelScripts import RES
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from Src.utils.pytesser import *
from Src.utils.element_scroll import Element_Scroll

reload(sys)
sys.setdefaultencoding('utf8')


class RES():
    # 我的班级
    ID_CLASS = 'com.xes.drawpanel:id/class_tv'
    # 主讲老师
    ID_TEACHER = 'com.xes.drawpanel:id/masterTeaName'
    teacher_name = u'主讲老师 :测试老师'
    # 班级名字
    ID_CLASS_NAME = 'com.xes.drawpanel:id/className'
    class_name = u'初三化学'
    # 学生人数
    ID_STU_NO = 'com.xes.drawpanel:id/stuCount'
    stu_no = u'班级人数:6'
    # 我的班级页面RelativeLayout
    ID_CLASS_ALL = 'android.widget.RelativeLayout'

    @classmethod
    # 点击进入班级详情页面
    def gotoclassitempage(self):
        Driver().get_driver().find_element_by_id(self.ID_CLASS_ALL).click()


class TestMyClass(unittest.TestCase):
    # SetUp测试环境
    def setUp(self):
        '''获取driver对象，进入被测页面'''
        self._driver = Driver().get_driver()
        self.__init_Login_activity()

    # TearDown测试环境
    def tearDown(self):
        # 重置driver，清空driver累积状态，供同时运行多条case使用
        Driver().reset_driver()
        # 关闭当前session，仅供单条case测试使用，多条的时候注释掉此行
        # Driver().close_driver()

    # 初始化方法,登录账户
    def __init_Login_activity(self):
        _driver = LRES.login_account()
        # 点击我的班级
        Driver().get_driver().find_element_by_id(RES.ID_CLASS).click()

    # C-11: 验证老师名字
    def test_11_TeacherName(self):
        _exp_teacher_name = RES.teacher_name
        _act_teacher_name = self._driver.find_element_by_id(RES.ID_TEACHER).text.encode('utf8')
        print _act_teacher_name
        assert _exp_teacher_name == _act_teacher_name, \
            '老师名字与期望不符，exp=%s, act=%s' % (_exp_teacher_name, _act_teacher_name)

    # C-12: 验证班级名字
    def test_12_ClassName(self):
        _exp_class_name = RES.class_name
        _act_class_name = self._driver.find_element_by_id(RES.ID_CLASS_NAME).text.encode('utf8')
        print _act_class_name
        assert _exp_class_name == _act_class_name, \
            '班级名字与期望不符，exp=%s, act=%s' % (_exp_class_name, _act_class_name)

    # C-13: 验证班级人数
    def test_13_StuNo(self):
        _exp_stu_no = RES.stu_no
        _act_stu_no = self._driver.find_element_by_id(RES.ID_STU_NO).text.encode('utf8')
        print _act_stu_no
        assert _exp_stu_no == _act_stu_no, \
            '班级人数与期望不符，exp=%s, act=%s' % (_exp_stu_no, _act_stu_no)




