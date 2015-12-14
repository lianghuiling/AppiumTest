# -*- encoding:utf8 -*-
__author__ = 'LHL'

import unittest
import sys
import string
from Src.driver.driver import Driver
from Test.TestLogin.TestLoginScript import RES as LRES
from Src.utils.element_scroll_old import E
from Src.utils.element_scroll import Element_scroll
from Src.utils.takephot import photo

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

    # 学生名字
    ID_STU_NAME = 'com.xes.drawpanel:id/student_name'
    # 反馈按钮
    ID_FEEDBACK = 'com.xes.drawpanel:id/isfeedback'
    # 本周作业提交数
    ID_WORK_NUM = 'com.xes.drawpanel:id/weekHomeworkNum'

    @classmethod
    # 点击点击我的班级,然后进入学生列表页面
    def gotoclassitempage(self):
        Driver().get_driver().find_element_by_id(RES.ID_CLASS).click()
        # 点击进入学生列表页面
        class_list = Driver().get_driver().find_elements_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.GridView\")"
            ".childSelector(new UiSelector().className(\"android.widget.RelativeLayout\"))")[0].click()

    @classmethod
    def find_all_student_list(self):
        '''
        找出所有学生列表
        :return:返回第一行学生信息
        '''
        work_list = Driver().get_driver().find_element_by_id('com.xes.drawpanel:id/student_ListView')
        work_list1 = work_list.find_elements_by_class_name('android.widget.LinearLayout')
        print len(work_list1)

        # work_list = Driver().get_driver().find_elements_by_android_uiautomator(
        #     "new UiSelector().className(\"android.widget.ListView\")"
        #     ".childSelector(new UiSelector().className(\"android.widget.LinearLayout\"))")
        return work_list1[0]

    @classmethod
    def get_all_student_no(self):
        list_panel_id = 'com.xes.drawpanel:id/student_ListView'
        item_className = 'android.widget.LinearLayout'
        stu_info = E().element_scroll_by_clickable(Driver().get_driver(), list_panel_id, item_className)
        stu_no = len(stu_info)

        return stu_no


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
        # 点击我的班级,然后进入学生列表
        RES.gotoclassitempage()

    # C-11: 验证老师名字
    def test_11_GetStudentList(self):
        _exp_student_list_length = string.atoi(RES.stu_no[-1])
        _act_student_list_length = RES.get_all_student_no()
        # list_panel_id = 'com.xes.drawpanel:id/student_ListView'
        # item_className = 'android.widget.LinearLayout'
        # _act_student_list_length = len(E.element_scroll(Driver().get_driver(), list_panel_id, item_className))
        print _act_student_list_length
        assert _exp_student_list_length == _act_student_list_length, \
            '学生列表长度与期望不符，exp=%d, act=%d' % (_exp_student_list_length, _act_student_list_length)

    # C-12: 获取学生名字
    def test_12_GetStudentName(self):
        _exp_stu_name = u'刘鹏鹏'
        _act_stu_name = RES.find_all_student_list().find_element_by_id(RES.ID_STU_NAME).text.encode('utf8')
        print _act_stu_name
        assert _exp_stu_name == _act_stu_name, \
            '学生名字与期望不符，exp=%d, act=%d' % (_exp_stu_name, _act_stu_name)

    # C-13: 查看反馈状态
    def test_13_GetFeedStatus(self):
        # _exp_stu_name = u'刘鹏鹏'
        _feed_button1 = RES.find_all_student_list().find_element_by_id(RES.ID_FEEDBACK)
        print _feed_button1.text.encode('utf8')
        _feed_button1.click()
        print _feed_button1.text.encode('utf8')

    # C-14: 获取本周提交作业数
    def test_14_GetWorkNo(self):
        _work_no = RES.find_all_student_list().find_element_by_id(RES.ID_WORK_NUM).text.encode('utf-8')
        photo.take_screeshot()
        print _work_no




