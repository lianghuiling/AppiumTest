# -*- encoding:utf8 -*-
__author__ = 'LHL'
from selenium.webdriver.support.ui import WebDriverWait
from Src.driver.driver import Driver


class findsomething:
    def find_by_message(cls, driver, toast_message, timeout, interval=1):
        '''
        根据toast消息内容，等待toast浮现
        :param driver: appium driver
        :param toast_message: toast消息内容
        :param timeout: 超时时间
        :param interval: 每次验证的时间间隔(s)
        :return:
        '''

        try:
            WebDriverWait(driver, timeout, interval).until(
                lambda d: d.find_element_by_android_uiautomator(
                    "new UiSelector().text(\"%s\")" % toast_message).is_displayed())
            # print toast_message
            return True
        except Exception:
            return False


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
    def find_all_button(self, e):
        for i in RES.list:
            # print i
            try:
                e.find_element_by_id(i).is_displayed()

            except Exception:
                return False
        return True
