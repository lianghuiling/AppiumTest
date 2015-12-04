# -*- encoding:utf8-*-
# from Src.utils.abc import singleton
#
#
# @singleton


class Element_scroll():
    
    @classmethod
    def element_scroll(cls, driver, list_panel_id, item_className, scroll_step=1, scroll_bottom=True, last_item_texts=[], __all_item_text=[], __item_text_len=0):
        '''
        Appium滑动条滑动
        :param list_panel: 列表容器（父控件）
        :param item_className: 列表项容器的classname
        :param scroll_step: 滑动的间隔，如果=0，则滑动至最底部
        :return: list -> __all_item_text -> 滑动列表中所有列表项的文字
        '''
        #0 .定义内部类函数
        def __get_all_text_in_element(element):
            __all_text = []
            __all_text_ele = element.find_elements_by_class_name("android.widget.TextView")
            for __text_ele in __all_text_ele:
                __all_text.append(__text_ele.text)
            return __all_text
        # 1. 获取list容器
        __scroll_list_panel = driver.find_element_by_id(list_panel_id)
        # 2.获取列表容器中所有的子列表项容器
        __scroll_list_items = __scroll_list_panel.find_elements_by_class_name(item_className)
        # 3.获取当前展示的子列表项的数量
        __scroll_list_items_count = len(__scroll_list_items)
        # 4.获取当前列表的所有已加载文字信息
        #  已第一个列表项为基础，判断文字信息是否完全
        if __item_text_len == 0:
            __item_text_len = len(__get_all_text_in_element(__scroll_list_items[0]))
        for __list_item in __scroll_list_items:
            __current_item_texts = __get_all_text_in_element(__list_item)
            if (len(__current_item_texts) == __item_text_len) and (__all_item_text.count(__current_item_texts) == 0):
                __all_item_text.append(__current_item_texts)
        # 5.获取当前列表项最后一个列表中的文字信息
        __last_item_texts = __all_item_text[-1]
        # 5. 判断是否到达底部，如果达到则返回
        if __last_item_texts == last_item_texts:
            return __all_item_text
        # 6.判断滑动步数，如果等于0或大于当前列表数一半，则滑动数量等于当前列表项/2
        if (scroll_step == 0) or (scroll_step > __scroll_list_items_count / 2):
            scroll_step = (lambda x: x == 0 and 1 or x)(__scroll_list_items_count / 2)
        # 7.按指定步数滑动列表
        driver.scroll(__scroll_list_items[scroll_step], __scroll_list_items[0])
        # 8.判断是否滑动至底部，如果不是则返回，如果是递归调用滑动方法，直到滑动至底部
        if scroll_bottom:
            __all_item_text = cls.element_scroll(driver, list_panel_id, item_className, scroll_step, scroll_bottom, __last_item_texts, __all_item_text, __item_text_len)
        else:
            return __all_item_text
        return __all_item_text
