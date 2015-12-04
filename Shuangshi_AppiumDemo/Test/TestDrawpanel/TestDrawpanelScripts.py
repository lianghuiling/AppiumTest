# -*- encoding:utf8 -*-
__author__ = 'LHL'

import unittest
import random
import sys
from Src.driver.driver import Driver
from Test.TestLogin.TestLoginScript import RES as LRES
from Test.TestMyWork.TestMyWorkScripts import RES as WRES
from Src.utils.takephot import photo
from Src.utils.findsomething import findsomething
reload(sys)
sys.setdefaultencoding('utf8')


class RES():
    # 左上角后退按钮
    ID_BACK = 'com.xes.drawpanel:id/back'
    # 学生名字
    ID_STUDENT_NAME = 'com.xes.drawpanel:id/student_name'
    # 批改笔/橡皮檫
    ID_PEN = 'com.xes.drawpanel:id/panel'
    # 录音按钮
    ID_RECORD = 'com.xes.drawpanel:id/start_record'
    # 播放按钮
    ID_RECORD_PLAY = 'com.xes.drawpanel:id/recordtime'
    # 查看题目按钮
    ID_QUESTION_SEE = 'com.xes.drawpanel:id/questionSee'
    # 试卷名称
    ID_PAPER_NAME = 'com.xes.drawpanel:id/middle_title'
    # 题号
    ID_QUESTION_NO = 'com.xes.drawpanel:id/question_no'
    # 对号
    ID_RIGHT = 'com.xes.drawpanel:id/right'
    # 错号
    ID_WRONG = 'com.xes.drawpanel:id/wrong'
    # 半对
    ID_RIGHT_WRONG = 'com.xes.drawpanel:id/right_wrong'
    # 标记
    ID_IS_FEEDBACK = 'com.xes.drawpanel:id/isfeedback'
    # 提交
    ID_SUBMIT = 'com.xes.drawpanel:id/submit_btn'

    # 知识点出错
    ID_SHOW_SUBMIT1 = 'com.xes.drawpanel:id/showsubmit1'
    # 分析能力弱
    ID_SHOW_SUBMIT2 = 'com.xes.drawpanel:id/showsubmit2'
    # 基础概念模糊
    ID_SHOW_SUBMIT3 = 'com.xes.drawpanel:id/showsubmit3'
    # 计算失误
    ID_SHOW_SUBMIT4 = 'com.xes.drawpanel:id/showsubmit4'

    # 学习习惯较差
    ID_SHOW_SUBMIT5 = 'com.xes.drawpanel:id/showsubmit5'

    # 马虎粗心
    ID_SHOW_SUBMIT6 = 'com.xes.drawpanel:id/showsubmit6'

    # 态度不端正
    ID_SHOW_SUBMIT7 = 'com.xes.drawpanel:id/showsubmit7'

    # 其它
    ID_SHOW_SUBMIT8 = 'com.xes.drawpanel:id/showsubmit8'

    # 1分
    ID_SHOW_SCORE1 = 'com.xes.drawpanel:id/showscore1'

    # 2分
    ID_SHOW_SCORE2 = 'com.xes.drawpanel:id/showscore2'

    # 3分
    ID_SHOW_SCORE3 = 'com.xes.drawpanel:id/showscore3'

    # 4分
    ID_SHOW_SCORE4 = 'com.xes.drawpanel:id/showscore4'

    # 5分
    ID_SHOW_SCORE5 = 'com.xes.drawpanel:id/showscore5'

    # 6分
    ID_SHOW_SCORE6 = 'com.xes.drawpanel:id/showscore6'

    # 7分
    ID_SHOW_SCORE7 = 'com.xes.drawpanel:id/showscore7'

    # 8分
    ID_SHOW_SCORE8 = 'com.xes.drawpanel:id/showscore8'

    # 9分
    ID_SHOW_SCORE9 = 'com.xes.drawpanel:id/showscore9'

    # 10分
    ID_SHOW_SCORE10 = 'com.xes.drawpanel:id/showscore10'

    # 取消
    ID_CANCEl = 'com.xes.drawpanel:id/showdiss'

    # 确认
    ID_YES = 'com.xes.drawpanel:id/showyes'

    # 定义出错原因list
    wrong_list = [u'知识点错误', u'分析能力弱', u'基础概念模糊', u'计算失误', \
                  u'学习习惯较差', u'马虎粗心', u'态度不端正', u'其它']

    # 定义分数列表
    score_list = [u'1分', u'2分', u'3分', u'4分', u'5分', \
                  u'6分', u'7分', u'8分', u'9分', u'10分']

    # 定义按钮list
    button_list = [u'取消', u'确认']


    def click_submit_button(self):
        # 定义对号
        right_button = Driver().get_driver().find_element_by_id(RES.ID_RIGHT)
        # 定义提交按钮并点击
        submit_button = Driver().get_driver().find_element_by_id(RES.ID_SUBMIT)
        # 点击对号
        right_button.click()
        # 点击提交按钮
        submit_button.click()

    @classmethod
    def draw_work(self):
        '''
        画几笔，用用橡皮擦
        录音，播放播音
        选择对错
        提交
        :return:
        '''
        # 定义driver
        res_driver = Driver().get_driver()
        # 定义对号
        right_button = res_driver.find_element_by_id(RES.ID_RIGHT)
        # 定义错号
        wrong_button = res_driver.find_element_by_id(RES.ID_WRONG)
        # 定义半对
        right_wrong_button = res_driver.find_element_by_id(RES.ID_RIGHT_WRONG)
        # 结果列表
        result = [right_button, wrong_button, right_wrong_button]

        # 定义提交按钮并点击
        submit_button = res_driver.find_element_by_id(RES.ID_SUBMIT)
        # 定义铅笔/橡皮按钮
        pen_erase_button = res_driver.find_element_by_id(RES.ID_PEN)
        # 定义录音/停止按钮
        record_button = res_driver.find_element_by_id(RES.ID_RECORD)
        # 定义播放按钮
        record_play_button = res_driver.find_element_by_id(RES.ID_RECORD_PLAY)
        # 定义查看题目按钮
        question_see_button = res_driver.find_element_by_id(RES.ID_QUESTION_SEE)

        # 定义标记按钮
        feedback_button = res_driver.find_element_by_id(RES.ID_IS_FEEDBACK)



        # 用笔画3笔
        res_driver.swipe(661, 473, 1821, 473)
        res_driver.swipe(661, 1358, 1821, 1358)
        res_driver.swipe(996, 318, 996, 1323)
        res_driver.swipe(1530, 318, 1530, 1323)
        # 点击铅笔按钮变为橡皮擦
        pen_erase_button.click()
        # 擦除一条线
        res_driver.swipe(1530, 318, 1530, 1323)
        # 录音按钮
        record_button.click()
        # 设置录音时间5s
        res_driver.implicitly_wait(5)
        # 再次点击停止录音
        record_button.click()
        # 点击录音播放按钮
        record_play_button.click()
        # 设置播放录音时间5s
        res_driver.implicitly_wait(5)
        # 点击查看题目
        question_see_button.click()
        if findsomething().find_by_message(res_driver, u'原题', 2, 1):
            print u'查看题目功能正常'
        else:
            print u'查看题目功能不正常'
        # 定义关闭查看题目按钮
        question_close_button = res_driver.find_element_by_id('com.xes.drawpanel:id/diss_window')
        # 关闭查看题目
        question_close_button.click()
        # 随机选择一个答题结果
        result[random.randint(0, 2)].click()
        # 点击标记按钮
        feedback_button.click()
        # 点击提交按钮
        submit_button.click()
                # 知识点出错
        show_submit1 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT1)
        # 分析能力弱
        show_submit2 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT2)
        # 基础概念模糊
        show_submit3 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT3)
        # 计算失误
        show_submit4 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT4)
        # 学习习惯较差
        show_submit5 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT5)
        # 马虎粗心
        show_submit6 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT6)
        # 态度不端正
        show_submit7 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT7)
        # 其它
        show_submit8 = res_driver.find_element_by_id(RES.ID_SHOW_SUBMIT8)
        # 1分
        show_score1 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE1)
        # 2分
        show_score2 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE2)
        # 3分
        show_score3 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE3)
        # 4分
        show_score4 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE4)
        # 5分
        show_score5 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE5)
        # 6分
        show_score6 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE6)
        # 7分
        show_score7 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE7)
        # 8分
        show_score8 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE8)
        # 9分
        show_score9 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE9)
        # 10分
        show_score10 = res_driver.find_element_by_id(RES.ID_SHOW_SCORE10)
        # 取消
        cancel_button = res_driver.find_element_by_id(RES.ID_CANCEl)
        # 确认
        yes_button = res_driver.find_element_by_id(RES.ID_YES)

        # 定义出错原因list
        wrong_button_list = [show_submit1, show_submit2, show_submit3, show_submit4, \
                             show_submit5, show_submit6, show_submit7, show_submit8]

        # 定义分数列表
        score_button_list = [show_score1, show_score2, show_score3, show_score4, show_score5, \
                             show_score6, show_score7, show_score8, show_score9, show_score10]
        # 随机选择一个错题原因
        wrong_button_list[random.randint(0, 7)].click()
        # 随机选择一个分数
        score_button_list[random.randint(0, 9)].click()
        # 取消关闭对话框
        cancel_button.click()
        # 再次点击提交按钮
        submit_button.click()
        # 随机选择一个错题原因
        wrong_button_list[random.randint(0, 7)].click()
        # 随机选择一个分数
        score_button_list[random.randint(0, 9)].click()
        # 点击确认提交作业
        yes_button.click()


class TestDrawpanel(unittest.TestCase):
    # SetUp测试环境
    def setUp(self):
        '''获取driver对象，进入被测页面'''
        self._driver = Driver().get_driver()
        self.__init_drawpanel_activity()

    # TearDown测试环境
    def tearDown(self):
        # 重置driver，清空driver累积状态，供同时运行多条case使用
        Driver().reset_driver()
        # 关闭当前session，仅供单条case测试使用，多条的时候注释掉此行
        # Driver().close_driver()

    # 初始化方法,登录账户
    # 点击批改进入批改页面
    def __init_drawpanel_activity(self):
        _driver = LRES.login_account()
        WRES.find_and_click_draw_button()

    # C-11: 验证没有批改作业的时候学生名字显示
    # 期望是无学生
    def test_11_NoWork(self):
        _exp_student_name = u'无学生'
        _act_student_name = self._driver.find_element_by_id(RES.ID_STUDENT_NAME).text.encode('utf-8')
        print u'请查看没有待批改作业的批改截图：'
        # 给截图加上时间戳，防止重复命名的覆盖
        photo().take_screeshot()
        assert _exp_student_name == _act_student_name, \
            '期望的没作业时候的学生名字与设计不符，exp=%s, act=%s' % (_exp_student_name, _act_student_name)


    # C-12: 获取提交作业的学生情况，试卷情况并打印
    def test_12_ClickFeedBack(self):
        feed_back_button = self._driver.find_element_by_id(RES.ID_IS_FEEDBACK)
        print u'标记按钮初始内容为：' + feed_back_button.text.encode('utf-8')
        feed_back_button.click()
        _exp_feed_back_content = u'已标记'
        _act_feed_back_content = feed_back_button.text.encode('utf-8')
        print u'标记按钮初始内容为：' + _act_feed_back_content
        assert _exp_feed_back_content == _act_feed_back_content, \
            '期望的标记按钮名字与设计不符，exp=%s, act=%s' % (_exp_feed_back_content, _act_feed_back_content)

    # C-13: 获取提交作业的学生情况，试卷情况并打印
    def test_13_GetStudentInfoandPaperInfo(self):
        # 获取提交作业的学生姓名
        _act_student_name = self._driver.find_element_by_id(RES.ID_STUDENT_NAME).text.encode('utf-8')
        print u'提交作业的学生名字：' + _act_student_name
        # 获取提交作业的试卷名字
        _act_paper_name = self._driver.find_element_by_id(RES.ID_PAPER_NAME).text.encode('utf-8')
        print u'提交作业的试卷名字：' + _act_paper_name
        # 获取提交作业的试卷题号
        _act_question_no = self._driver.find_element_by_id(RES.ID_QUESTION_NO).text.encode('utf-8')
        print U'提交作业的试卷题号：' + _act_question_no
        # 截图
        photo().take_screeshot()

    # C-14: 点击提交按钮弹出分数选择框
    def test_14_ClickSubmitDialog(self):
        RES().click_submit_button()
        if findsomething().find_by_message(self._driver, u'1分', 2, 1):
            print u'点击提交后弹出框正确！'
        else:
            print u'点击提交后弹出框错误！'

    # C-15: 查看错题原因是否显示完全
    def test_15_CheckWrongReason(self):
        RES().click_submit_button()
        photo().take_screeshot()
        for reason in RES().wrong_list:
            if findsomething().find_by_message(self._driver, reason, 2, 1):
                print '错题原因' + reason + '存在'
            else:
                print '错题原因' + reason + '不存在'

    # C-16: 查看分数是否显示完全
    def test_16_CheckScoreList(self):
        RES().click_submit_button()
        for score in RES().score_list:
            if findsomething().find_by_message(self._driver, score, 2, 1):
                print '分数' + score + '存在'
            else:
                print '分数' + score + '不存在'

    # C-17: 查看确认取消是否显示完全
    def test_17_CheckButtonList(self):
        RES().click_submit_button()
        for button in RES().button_list:
            if findsomething().find_by_message(self._driver, button, 2, 1):
                print '按钮' + button + '存在'
            else:
                print '按钮' + button + '不存在'

    # C-18: 点击弹出框的取消按钮
    def test_18_ClickCancelButton(self):
        RES().click_submit_button()
        photo().take_screeshot()
        cancel_button = self._driver.find_element_by_id(RES.ID_CANCEl)
        cancel_button.click()
        if findsomething().find_by_message(self._driver, u'提交', 2, 1):
            print u'取消功能正常，弹出框关闭'
        else:
            print u'取消功能不正常，弹出框没有关闭'

    # C-19: 批改作业
    def test_19_DrawWork(self):
        RES.draw_work()









