# -*- encoding:utf8-*-
# from Src.utils.abc import singleton
#
import time
from Src.utils.findsomething import RES
# @singleton
class E():
    
    # @classmethod
    # def element_scroll(cls, driver, list_panel_id, item_className, scroll_step=1, scroll_bottom=True, last_item_texts=[], __all_item_text=[], __item_text_len=0):
    #     '''
    #     Appium滑动条滑动
    #     :param list_panel: 列表容器（父控件）
    #     :param item_className: 列表项容器的classname
    #     :param scroll_step: 滑动的间隔，如果=0，则滑动至最底部
    #     :return:
    #     '''
    #     #0 .定义内部类函数
    #     def __get_all_text_in_element(element):
    #         __all_text = []
    #         __all_text_ele = element.find_elements_by_class_name("android.widget.TextView")
    #         print 'chandu' + str(len(__all_text_ele))
    #         for __text_ele in __all_text_ele:
    #             # print __text_ele.text.encode('utf-8')
    #                 __all_text.append(__text_ele.text)
    #         return __all_text
    #     # 1. 获取list容器
    #     print '1进入方法：'
    #     __scroll_list_panel = driver.find_element_by_id(list_panel_id)
    #     # 2.获取列表容器中所有的子列表项容器
    #     print '2开始找子列表'
    #     __scroll_list_items = __scroll_list_panel.find_elements_by_id(item_className)
    #     # __scroll_list_items = __scroll_list_panel.find_elements_by_class_name(item_className)
    #     # 3.获取当前展示的子列表项的数量
    #     print '3获取数量：'
    #     # for i in [0, len(__scroll_list_items)]:
    #     #     b = __scroll_list_items[i].find_elements_by_class_name('android.widget.TextView')
    #     #     for tst in b:
    #     #         print tst.text.encode('utf-8')
    #
    #     # print __scroll_list_items
    #     __scroll_list_items_count = len(__scroll_list_items)
    #     # for i in [0, 3]:
    #     #     b = __scroll_list_items[i].find_elements_by_class_name('android.widget.TextView')
    #     #     for tst in b:
    #     #         print tst.text.encode('utf-8')
    #
    #     # 4.获取当前列表项最后一个列表中的文字信息
    #     print '4数量多少' + str(__scroll_list_items_count)
    #     if __item_text_len == 0:
    #         __item_text_len = len(__get_all_text_in_element(__scroll_list_items[0]))
    #     for __list_item in __scroll_list_items:
    #         __current_item_texts = __get_all_text_in_element(__list_item)
    #         if (len(__current_item_texts) == __item_text_len) and (__all_item_text.count(__current_item_texts) == 0):
    #             __all_item_text.append(__current_item_texts)
    #     # 5.获取当前列表项最后一个列表中的文字信息
    #     print '5获取列表最后一个文字信息：'
    #     __last_item_texts = __all_item_text[-1]
    #     # 5. 判断是否到达底部，如果达到则返回
    #     print '6判断是否到底部：'
    #     if __last_item_texts == last_item_texts:
    #         # for i in [0, len(__all_item_text)]:
    #         #     b = __all_item_text[i].find_elements_by_class_name('android.widget.TextView')
    #         #     for tst in b:
    #         #         print tst.text.encode('utf-8')
    #         # for i in [0, len(__all_item_text)]:
    #         print __all_item_text
    #         return __all_item_text
    #     print '7判断滑动步数'
    #     # 6.判断滑动步数，如果等于0或大于当前列表数，则滑动数量等于当前列表项
    #     # if (scroll_step == 0) or (scroll_step > __scroll_list_items_count / 2):
    #     #     scroll_step = (lambda x: x == 0 and 1 or x)(__scroll_list_items_count / 2)
    #     print '8滑动步数多少' + str(scroll_step)
    #     # 7.按指定步数滑动列表
    #     print '9滚动'
    #     driver.scroll(__scroll_list_items[scroll_step], __scroll_list_items[0])
    #     # 8.判断是否滑动至底部，如果不是则返回，如果是递归调用滑动方法，直到滑动至底部
    #     print '10判断是否到底部2：'
    #     if scroll_bottom:
    #        __all_item_text = cls.element_scroll(driver, list_panel_id, item_className, scroll_step, scroll_bottom, __last_item_texts, __all_item_text, __item_text_len)
    #     else:
    #         # for i in [0, len(__all_item_text)]:
    #         #     b = __all_item_text[i].find_elements_by_class_name('android.widget.TextView')
    #         #     for tst in b:
    #         #         print tst.text.encode('utf-8')
    #         # print __all_item_text
    #         return __all_item_text
    #
    #     # for i in [0, len(__all_item_text)]:
    #     #         b = __all_item_text[i].find_elements_by_class_name('android.widget.TextView')
    #     #         for tst in b:
    #     #             print tst.text.encode('utf-8')
    #     # print __all_item_text
    #     return __all_item_text
    #     print '11结束'


    @classmethod
    def element_scroll_to_find_button(cls, driver, list_panel_id, item_className, scroll_step=1, scroll_bottom=False, last_item_texts=[], __all_item_text=[], __item_text_len=0):
        '''
        Appium滑动条滑动
        :param list_panel: 列表容器（父控件）
        :param item_className: 列表项容器的classname
        :param scroll_step: 滑动的间隔，如果=0，则滑动至最底部
        :return:
        '''
        #0 .定义内部类函数
        def __get_all_text_in_element(element):
            __all_text = []
            __all_text_ele = element.find_elements_by_class_name("android.widget.TextView")
            for __text_ele in __all_text_ele:
                if RES.find_all_button(element):
                     print __text_ele.text.encode('utf-8')
                     __all_text.append(__text_ele.text)
            return __all_text


        print '初始化返回值为空'
        __all_item_text = []
        __item_text_len = 8
        # 1. 获取list容器
        print '1进入方法：'
        __scroll_list_panel = driver.find_element_by_id(list_panel_id)
        # 2.获取列表容器中所有的子列表项容器
        print '2开始找子列表'
        __scroll_list_items = __scroll_list_panel.find_elements_by_id(item_className)
        print len(__scroll_list_items)
        __item_text_len = 8
        # __item_text_len = len(__get_all_text_in_element(__scroll_list_items[0]))
        print '单个list长度' + str(__item_text_len)
        print '3开始循环滚动'
        while not scroll_bottom:
            print '获得当前所有list'
            old_list_panel = __scroll_list_panel.find_elements_by_id(item_className)
            # 添加当前text到list
            for __old_list_item in old_list_panel:
                __old_item_texts = __get_all_text_in_element(__old_list_item)
                # print __old_item_texts
                print RES.find_all_button(__old_list_item)
                print __all_item_text.count(__old_item_texts)
                print len(__old_item_texts)
                a = RES.find_all_button(__old_list_item) and len(__old_item_texts) == __item_text_len and __all_item_text.count(__old_item_texts) == 0
                print a
                if a:
                    __all_item_text.append(__old_item_texts)
            # 获取当前的最后一条
            old_last_item = __all_item_text[-1]
            # print old_last_item
            # 开始滚动
            driver.swipe(435,1432,435,549)
            # driver.scroll(old_list_panel[1], old_list_panel[0])
            print '获取现在所有list'
            current_list_panel = __scroll_list_panel.find_elements_by_id(item_className)
            for __list_current_item in current_list_panel:
                __current_item_texts = __get_all_text_in_element(__list_current_item)
                # print __current_item_texts
                print RES.find_all_button(__list_current_item)
                print __all_item_text.count(__current_item_texts)
                print len(__current_item_texts)
                # if (len(__current_item_texts) == __item_text_len) and (__all_item_text.count(__current_item_texts) == 0):
                if RES.find_all_button(__list_current_item) and len(__current_item_texts) == __item_text_len and __all_item_text.count(__current_item_texts) == 0:
                    __all_item_text.append(__current_item_texts)
            # 获取现在的最后一条
            new_last_item = __all_item_text[-1]
            # print new_last_item
            print '判断最后一个list内容是否相等'
            # print scroll_bottom
            if new_last_item == old_last_item:
                scroll_bottom = True
                # print scroll_bottom
                print __all_item_text
                return __all_item_text
            # time.sleep(2)
            # else:
            #    __all_item_text =  cls.element_scroll_to_find_button(driver, list_panel_id, item_className, scroll_step, scroll_bottom, new_last_item, __all_item_text, __item_text_len)
            #    return __all_item_text

