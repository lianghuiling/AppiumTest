# -*- encoding:utf8-*-

import os
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

#测试目标基础信息

PLATFORM_NAME = 'Android'
PLATFORM_VER = '4.4.2'
DEVICES_NAME = '430072fe4758a07f'
APP_PACKAGE = 'com.xes.drawpanel'
APP_ACTIVITY = '.activity.LoginActivity'
SERVER_IP = '127.0.0.1:4723'
APP_PATH = PATH('E:\Users\Administrator\PycharmProjects\Shuangshi_AppiumDemo\DrawPanel1117test.apk')