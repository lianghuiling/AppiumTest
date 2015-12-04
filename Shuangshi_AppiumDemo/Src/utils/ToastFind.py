# -*- encoding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
# from Src.utils.pytesser import *
import PIL.Image
import pytesser
import util
import errors

class Find_Toast():
    @classmethod
    def find_toast(cls, message, timeout, poll_frequency, driver):
        element = WebDriverWait(driver,timeout,poll_frequency).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,message)))
        # print element

    @classmethod
    def wait_toast_by_message(self, toast_message, timeout, interval=1):
        try:
            WebDriverWait(self, timeout, interval).until(
                lambda d: d.find_element_by_text(toast_message).is_displayed())
            return True
        except TimeoutException:
            return False


    def read_imagetext(self):
        im = PIL.Image.open('E:\study\oooo.png')
        # text = pytesser.image_to_string(im)
        # print "Using image_to_string(): "
        # print text
        text = pytesser.image_file_to_string('E:\study\oooo.png', graceful_errors=True)
        print "Using image_file_to_string():"
        print text

Find_Toast().read_imagetext()