__author__ = 'Administrator'

from Src.driver.driver import Driver
import key_events

def edittextclear(cls, text):
        '''
       请除EditText文本框里的内容
        @param:text 要清除的内容
        '''
        # 光标移到末尾
        Driver().get_driver().keyevent(key_events.KEYCODE_MOVE_END)
        # 循环删除
        for i in range(0, len(text)):
            Driver().get_driver().keyevent(key_events.KEYCODE_DEL)
