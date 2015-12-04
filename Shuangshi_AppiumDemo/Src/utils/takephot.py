# -*- encoding:utf8 -*-
__author__ = 'LHL'
from Src.driver.driver import Driver
from datetime import datetime


class photo:
    @classmethod
    def take_screeshot(self):
        '''
        给截图加上时间戳，防止重复命名的覆盖，保存到指定目录下
        :return:无
        '''
        Driver().get_driver().get_screenshot_as_file(u"D:/save_screenshot/%s.png" %
                                            datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3])