import unittest
from selenium import webdriver
import subprocess
from appTest1 import appTest1
import os
import signal

class SearchText(unittest.TestCase):



    @classmethod
    def setUp(self):
        # p = subprocess.Popen("appium", stdout=subprocess.PIPE, shell=True)
        # (output, err) = p.communicate()
        # p.wait()
        appTest1.get_device_name()

    @classmethod
    def tearDown(self):
        appTest1.get_device_version()

    # pid = p.pid
    # os.kill(pid,signal.SIGINT)
    # if not p.poll():
    #     print("Appium server exit successfull")

if __name__ == '__main__':
    unittest.main()