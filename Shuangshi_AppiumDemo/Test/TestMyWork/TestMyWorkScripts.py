# -*- encoding:utf8 -*-
__author__ = 'LHL'

import unittest
import string
import sys
import PIL.Image
from Src.driver.driver import Driver
from Test.TestLogin.TestLoginScript import RES as LRES
# from Test.TestDrawpanel.TestDrawpanelScripts import RES
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from Src.utils.pytesser import *
from Src.utils.element_scroll_old import E
from Src.utils.findsomething import RES as FRES

reload(sys)
sys.setdefaultencoding('utf8')


class RES():
    # 我的工作


    ID_WORK = 'com.xes.drawpanel:id/work'
    # 我的班级 和作业列表中班级名字ID一样，注意区分
    ID_CLASS = 'com.xes.drawpanel:id/class_tv'
    # 设置
    ID_SETTING = 'com.xes.drawpanel:id/setting'
    # 待批作业
    ID_READY_TO_PIGAI = 'com.xes.drawpanel:id/ready_to_pigai'
    # 全部任务/待批任务
    ID_ALL_CORRECT = 'com.xes.drawpanel:id/all_correct'
    # 试卷状态
    ID_PAPER_STATUS = 'com.xes.drawpanel:id/paperStatus'
    # 批改按钮/发布按钮
    ID_PIGAI_BUTTON = 'com.xes.drawpanel:id/pigai_btn'
    # 作业原题与答案按钮
    ID_QUESTION = 'com.xes.drawpanel:id/question'
    # 班级人数
    ID_CLASS_NUM = 'com.xes.drawpanel:id/class_num'
    # 提交人数
    ID_SUBMIT_NUM = 'com.xes.drawpanel:id/submit_num'
    # 已批改
    ID_WAIT_PIGAI = 'com.xes.drawpanel:id/wait_pigai'
    # 未提交
    ID_NO_SUBMIT = 'com.xes.drawpanel:id/no_submit'
    # 试卷名字
    ID_PAPER_TITLE = 'com.xes.drawpanel:id/main_title'
    # 主讲老师
    ID_TEACHER_NAME = 'com.xes.drawpanel:id/main_teachername'
    # 发布时间
    ID_PUB_TIME = 'com.xes.drawpanel:id/pub_time'

    # 作业原题的播放按钮
    ID_PLAY = 'com.xes.drawpanel:id/questionSay'

    # 批改页面
    # 批改页面学生姓名
    ID_STUDENT_NAME = 'com.xes.drawpanel:id/student_name'

    # 变量试卷名字
    paper_name = '11.2测试'
    # 变量老师名字
    teacher_name = '主讲老师：测试老师'
    # 变量班级名字
    class_name = '班级：初三化学'
    # 变量发布时间
    pub_time = '发布时间：2015-11-02'

    # 变量班级人数
    class_no = '6'

    list = [ID_PAPER_TITLE, ID_TEACHER_NAME,ID_CLASS,ID_PUB_TIME, ID_CLASS_NUM, ID_SUBMIT_NUM, ID_WAIT_PIGAI,ID_NO_SUBMIT]

    @classmethod
    def find_all_button(self):
        for i in list:
            try:
                Driver().get_driver().find_element_by_id(i).is_displayed()

            except Exception:
                return  False
        return True

    @classmethod
    def image_file_to_string(cls, filename, cleanup=cleanup_scratch_flag, graceful_errors=True):
        '''
         Applies tesseract to filename; or, if image is incompatible and graceful_errors=True,
         converts to compatible format and then applies tesseract.  Fetches resulting text.     :param filename:
         If cleanup=True, delete scratch files after operation.                                 :param cleanup:
        :param graceful_errors:
        :return:
        '''
        try:
            try:
                call_tesseract(filename, scratch_text_name_root)
                text = util.retrieve_text(scratch_text_name_root)
            except errors.Tesser_General_Exception:
                if graceful_errors:
                    im = Image.open(filename)
                    text = image_to_string(im, cleanup)
                else:
                    raise
        finally:
            if cleanup:
                util.perform_cleanup(scratch_image_name, scratch_text_name_root)
        return text

    @classmethod
    def read_imagetext(self):
        im = PIL.Image.open('E:\study\身份证\11.png')
        text = image_to_string(im)
        print "Using image_to_string(): "
        print text
        text = image_file_to_string('fonts_test.png', graceful_errors=True)
        print "Using image_file_to_string():"
        print text

    @classmethod
    def find_and_click_pub_button(self):
        '''
        找到并点击发布按钮
        找不到就往下滑动，滑到底还找不到就提示用户
        :return:无
        '''
        flag = True
        while flag:
            try:
                Driver().get_driver().find_element_by_name(u'发布').click()
                flag = False
            except Exception:
                Driver().get_driver().swipe(800, 1435, 800, 210)
                if RES.wait_toast_by_message(Driver().get_driver(), '2015暑假物理第二讲-课中', 4):
                # listpanel_id = 'com.xes.drawpanel:id/live_ListView'
                # item_classname = 'android.widget.LinearLayout'
                # # last_item_texts = [u'\u73ed\u7ea7\u4eba\u6570\uff1a6', u'\u63d0\u4ea4\u4eba\u6570\uff1a0',
                # #                    u'\u5df2\u6279\u6539\uff1a0', u'\u672a\u63d0\u4ea4\uff1a6']
                # print Element_scroll.element_scroll(Driver().get_driver(), listpanel_id, item_classname, 1, True,last_item_texts)
                    flag = False
                    print '滑动到最底部了，没有找到'
                    break

    @classmethod
    def find_and_click_draw_button(self):
        '''
        找到并点击批改（1）按钮
        找不到就往下滑动，滑到底还找不到就提示用户
        :return:无
        '''
        flag = True
        while flag:
            try:
                Driver().get_driver().find_element_by_name(u'批改（0）').click()
                flag = False
            except Exception:
                Driver().get_driver().swipe(800, 1435, 800, 210)
                if RES.wait_toast_by_message(Driver().get_driver(), '2015暑假物理第二讲-课中', 4):
                    flag = False
                    print '滑动到最底部了，没有找到'
                    break

    @classmethod
    def find_toast(cls, message, timeout, poll_frequency, driver):
        element = WebDriverWait(driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
        print element


    def wait_activity(self, toast_message, timeout, interval=1):
        try:
            WebDriverWait(self, timeout, interval).until(
                lambda d: d.find_element_by_text(toast_message).is_displayed())
            print toast_message
            return True
        except TimeoutException:
            return False


    @classmethod
    def wait_toast_by_message(cls, driver, toast_message, timeout, interval=1):
        '''
        根据toast消息内容，等待toast浮现
        :param driver: appium driver
        :param toast_message: toast消息内容
        :param timeout: 超时时间
        :param interval: 每次验证的时间间隔(s)
        :return:
        '''
        from selenium.webdriver.support.ui import WebDriverWait

        try:
            WebDriverWait(driver, timeout, interval).until(
                lambda d: d.find_element_by_android_uiautomator(
                    "new UiSelector().text(\"%s\")" % toast_message).is_displayed())
            print toast_message
            return True
        except Exception:
            return False


    @classmethod
    def find_all_work(self):
        '''
        找出所有作业列表
        :return:返回第一行作业
        '''
        # work_list = Driver().get_driver().find_elements_by_android_uiautomator(
        #     "new UiSelector().className(\"android.widget.ListView\")"
        #     ".childSelector(new UiSelector().className(\"android.widget.LinearLayout\"))")

        work_list = Driver().get_driver().find_element_by_id('com.xes.drawpanel:id/live_ListView').\
            find_elements_by_class_name('android.widget.LinearLayout')
        print len(work_list)
        return work_list[0]

    @classmethod
    def get_paper_status(self):
        '''
        根据批改按钮的内容确定试卷状态
        批改按钮为发布：试卷状态为待发布
        批改按钮为批改（0）：试卷状态为已完成
        批改按钮为批改（1）：试卷状态为待批改
        :return:无
        '''
        _pigai_text = self.find_all_work().find_element_by_id(RES.ID_PIGAI_BUTTON).text.encode('utf8')
        if _pigai_text == '批改（0）':
            _act_paper_status = self.find_all_work().find_element_by_id(RES.ID_PAPER_STATUS).text.encode('utf-8')
            print '实际试卷状态:' + _act_paper_status
            _exp_paper_status = '已完成'.encode('utf-8')
            assert _act_paper_status == _exp_paper_status, \
                '试卷状态与期待不符，exp=%s, act=%s' % (_exp_paper_status, _act_paper_status)
        elif _pigai_text == '批改（1）':
            _act_paper_status = self.find_all_work().find_element_by_id(RES.ID_PAPER_STATUS).text.encode('utf-8')
            print '实际试卷状态:' + _act_paper_status
            _exp_paper_status = '待批改'.encode('utf-8')
            assert _act_paper_status == _exp_paper_status, \
                '试卷状态与期待不符，exp=%s, act=%s' % (_exp_paper_status, _act_paper_status)
        elif _pigai_text == '发布':
            _act_paper_status = self.find_all_work().find_element_by_id(RES.ID_PAPER_STATUS).text.encode('utf-8')
            print '实际试卷状态:' + _act_paper_status
            _exp_paper_status = '待发布'.encode('utf-8')
            assert _act_paper_status == _exp_paper_status, \
                '试卷状态与期待不符，exp=%s, act=%s' % (_exp_paper_status, _act_paper_status)


class TestMyWork(unittest.TestCase):
    # SetUp测试环境
    def setUp(self):
        '''获取driver对象，进入被测页面'''
        self._driver = Driver().get_driver()
        self.__init_Login_activity()

    # TearDown测试环境
    def tearDown(self):
        # 重置driver，清空driver累积状态，供同时运行多条case使用
        # Driver().reset_driver()
        # 关闭当前session，仅供单条case测试使用，多条的时候注释掉此行
        Driver().close_driver()

    # 初始化方法,登录账户
    def __init_Login_activity(self):
        _driver = LRES.login_account()

    # C-11: 验证试卷名字
    def test_11_PaperName(self):
        _exp_paper_name = RES.paper_name
        _act_paper_name = RES.find_all_work().find_element_by_id(RES.ID_PAPER_TITLE).text.encode('utf8')
        print _act_paper_name
        assert _exp_paper_name == _act_paper_name, \
            '试卷名字与期望不符，exp=%s, act=%s' % (_exp_paper_name, _act_paper_name)

    # C-12: 验证老师名字
    def test_12_TeacherName(self):
        _exp_teacher_name = RES.teacher_name
        _act_teacher_name = RES.find_all_work().find_element_by_id(RES.ID_TEACHER_NAME).text.encode('utf8')
        print _act_teacher_name
        assert _exp_teacher_name == _act_teacher_name, \
            '主讲老师名字与期望不符，exp=%s, act=%s' % (_exp_teacher_name, _act_teacher_name)

    # C-13: 验证班级名字
    def test_13_ClassName(self):
        _exp_class_name = RES.class_name
        # _act_class_name = self.__find_All_Work().find_element_by_
        _act_class_name = RES.find_all_work().find_element_by_id(RES.ID_CLASS).text.encode('utf8')
        print _act_class_name
        assert _exp_class_name == _act_class_name, \
            '班级名字与期望不符，exp=%s, act=%s' % (_exp_class_name, _act_class_name)

    # C-14: 验证发布时间
    def test_14_PubTime(self):
        _exp_pub_time = RES.pub_time
        _act_pub_time = RES.find_all_work().find_element_by_id(RES.ID_PUB_TIME).text.encode('utf8')
        print _act_pub_time
        assert _exp_pub_time == _act_pub_time, \
            '发布时间与期望不符，exp=%s, act=%s' % (_exp_pub_time, _act_pub_time)

    # C-15: 验证班级人数
    def test_15_Class_No(self):
        _exp_class_no = RES.class_no
        _act_class_no = RES.find_all_work().find_element_by_id(RES.ID_CLASS_NUM).text.encode('utf8')
        print _act_class_no
        assert _exp_class_no == _act_class_no[-1], \
            '班级人数与期望不符，exp=%s, act=%s' % (_exp_class_no, _act_class_no[-1])

    # C-16: 验证提交人数和未提交人数之和是否为班级总人数
    def test_16_Class_No(self):
        _submit_no = RES.find_all_work().find_element_by_id(RES.ID_SUBMIT_NUM).text.encode('utf8')
        # _submit_no.subString(-1)
        _not_submit_no = RES.find_all_work().find_element_by_id(RES.ID_NO_SUBMIT).text.encode('utf8')
        # 分别截取最后一个字符
        assert string.atoi(_submit_no[-1]) + string.atoi(_not_submit_no[-1]) == string.atoi(RES.class_no), \
            '提交人数与未提交人数之和和班级总人数不符，exp=%d, act=%d' % (
                string.atoi(_submit_no[-1]) + string.atoi(_not_submit_no[-1]), RES.class_no)

    #C-17: 验证批改按钮为批改（1）的时候试卷状态应该为待批改，批改（0）的时候试卷状态应该为已完成
    def test_17_Paper_Status_Pigai(self):
        RES.get_paper_status()

    # C-18: 验证待批作业数目
    def test_18_Ready_To_Pigai(self):
        _exp_ready_pigai = '0'
        _act_ready_pigai = self._driver.find_element_by_id(RES.ID_READY_TO_PIGAI).text.encode('utf-8')
        print '待批数量：' + _act_ready_pigai
        assert _exp_ready_pigai == _act_ready_pigai, \
            '待批数目与期望不符，exp=%s, act=%s' % (_exp_ready_pigai, _act_ready_pigai)

    #C-19: 点击作业原题与答案按钮
    def test_19_Question_Check(self):
        question = RES.find_all_work().find_element_by_id(RES.ID_QUESTION)
        question.click()
        play_button = self._driver.find_element_by_id(RES.ID_PLAY)
        play_button.click()
        # message = '无语音解析'.encode('utf-8')
        __driver = self._driver
        # RES.find_toast(u"无语音解析",5, 1, self._driver)
        print RES.wait_toast_by_message(self._driver, "无语音解析", 5, 0.00001)
        # RES().wait_activity(u"无语音解析",5, 1)
        # Find_Toast.wait_toast_by_message(u"无语音解析",5, 1)
        # Find_Toast.find_toast(u"无语音解析",5, 0.5, self._driver)
        # WebDriverWait(driver, 5, 0.5).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
        self._driver.swipe(2106, 1209, 240, 1209)
        play_button.click()

    #C-20: 找到发布按钮并发布作业
    def test_20_Publish_Work(self):
        RES.find_and_click_pub_button()

    #C-21: 找到批改按钮并批改作业
    def test_21_Draw_Work(self):
        '''
        没作业的时候打印没有待批改作业
        有作业的时候开始批改作业
        :return:
        '''
        RES.find_and_click_draw_button()
        student_name = self._driver.find_element_by_id(RES.ID_STUDENT_NAME).text.encode('utf-8')
        if student_name == u'无学生':
            print '现在没有待批改作业'
        else:
            #批改作业在testmywork中
            pass
            # RES_DrawPanel.draw_work()

    #C-22: 获取作业列表数目
    def test_22_Get_Work_No(self):
        list_panel_id = 'com.xes.drawpanel:id/live_ListView'
        # item_className = 'android.widget.LinearLayout'
        item_className = 'com.xes.drawpanel:id/rll'
        # a = Driver().get_driver().find_element_by_id(list_panel_id).find_elements_by_class_name(item_className)
        # print len(a)
        # b = a[0].find_elements_by_class_name('android.widget.TextView')
        # for tst in b:
        #     print tst.text.encode('utf-8')
        # stu_info = E.element_scroll(Driver().get_driver(), list_panel_id, item_className)
        stu_info = E.element_scroll_by_id(Driver().get_driver(), list_panel_id, item_className)
        stu_no = len(stu_info)
        # stu_no = len(E.element_scroll(Driver().get_driver(), list_panel_id, item_className))
        print '作业列表数量：' + str(stu_no)

    #C-23: 获取作业列表数目
    def test_23_Get_Work_No(self):
        list_panel_id = 'com.xes.drawpanel:id/live_ListView'
        item_className = 'com.xes.drawpanel:id/rll'
        a = Driver().get_driver().find_element_by_id(list_panel_id).find_elements_by_id(item_className)
        # print FRES.find_all_button(a[3])
        all_text3 = a[3].find_elements_by_class_name('android.widget.TextView')
        # print len(all_text3)

        Driver().get_driver().swipe(435,1225,435,514)
        a = Driver().get_driver().find_elements_by_id(item_className)
        # print "page source = \r\n: " + Driver().get_driver().page_source
        # print "1st len = %s" % len(a)
        for i in range(len(a)):
            # all_text0 = a[i].find_elements_by_class_name('android.widget.TextView')
            # all_text0 = a[i].find_elements_by_android_uiautomator("new UISelector().className(\"android.widget.TextView\")")
            __all_text0_1 = a[i].find_elements_by_android_uiautomator("new UiSelector().className(\"android.widget.TextView\")")
            # print all_text0
            print len(__all_text0_1)
            # _all = []
            for t in __all_text0_1:
                # _all.append(t.text)
                print t.text.encode('utf-8')






