
from appium import webdriver

import subprocess
import os
from builtins import print
import time


class appTest1:
    #
    # def start_appium_server(self):
    #     p = subprocess.Popen("appium", stdout=subprocess.PIPE, shell=True)
    #     (output, err) = p.communicate()
    #     p.wait()

    def get_device_name(self):
        p = subprocess.Popen("adb shell getprop ro.product.name", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        return  str(output.decode('ascii'))

    def get_device_version(self):
        p = subprocess.Popen("adb shell getprop ro.build.version.release", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        return  float(output.decode('ascii'))

    def launch_installed_application(self, package, activity):
        # Arranging the capabilities in the form of a DICTIONARY
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = self.get_device_version()
        desired_caps['deviceName'] = self.get_device_name()
        desired_caps['appPackage'] = package
        desired_caps['appActivity'] = activity
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240

        # Connecting to APPIUM SERVER with default port
        # http://localhost:4723/wd/hub
        self.driver =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        time.sleep(5)
        # self.vertical_scrollUp_little()
        #
        # self.driver.find_element_by_id("com.one20.maps.qa:id/marketing_splash_login").click()
        #
        # time.sleep(2)
        # username = self.driver.find_element_by_id("com.one20.maps.qa:id/login_email_field")
        # username.click()
        # self.insert_username("adevara@innominds.com")
        #
        # self.driver.hide_keyboard()
        #
        # continue_as_email_button = self.driver.find_element_by_id("com.one20.maps.qa:id/login_email_button")
        # continue_as_email_button.click()
        #
        # login_password_field = self.driver.find_element_by_id("com.one20.maps.qa:id/login_password_field")
        # login_password_field.click()
        #
        # time.sleep(3)
        # self.insert_password("pass@123")
        #
        # self.driver.hide_keyboard()
        #
        # login_password_submit_button = self.driver.find_element_by_id("com.one20.maps.qa:id/login_password_submit_button")
        # login_password_submit_button.click()

        time.sleep(5)
        self.device_back_key()

        search_button = self.driver.find_element_by_xpath("//android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[contains(@index,'1')]")
        search_button.click()

        self.insert_word("Judwaa 2")

        time.sleep(3)
        judwaa = self.driver.find_element_by_id("com.bt.bms:id/search_result_title")
        judwaa.click()

        book_ticket_button = self.driver.find_element_by_id("com.bt.bms:id/movie_details_activity_lin_bookticket")
        book_ticket_button.click()

        time.sleep(3)

        # book_date = self.driver.find_element_by_id("com.bt.bms:id/show_time_tab_date")
        # book_date.click()

        print("Available contexts are :: :: " + str(self.driver.current_context))

        time.sleep(5)

        print("Available contexts are :: :: " + str(self.driver.current_context))

        # timing = self.driver.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout/android.widget.TextView[contains(@index,'0')]")
        # timing.click()
        #
        # print("Available contexts are :: :: " + str(self.driver.current_context))
        #
        # search_field = self.driver.find_element_by_xpath("//android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[contains(@index,'1')]")
        # search_field.click()
        #




        # search_poi = self.insert_text_with_spaces("minerva%sgrand")
        # poi = self.driver.find_element_by_xpath("//android.view.View[contains(@index='0')]")
        # poi.click()


    def setUp(self, appname):
        # Providing APK name to the desired capabilities function

        # Forming the APK FILE PATH
        directory = "/Documents/pycharmworkspace/apkfolder/"
        user = str(os.path.expanduser('~'))
        full = user + directory


        # Arranging the capabilities in the form of a DICTIONARY
        desired_caps = {}
        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = self.get_device_version()
        desired_caps['deviceName'] = self.get_device_name()
        desired_caps['app'] = full + appname
        # desired_caps['noReset'] = True
        # desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240

        # Connecting to APPIUM SERVER with default port
        # http://localhost:4723/wd/hub
        self.driver =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    def uninstalling_application(self, packageName):
        p = subprocess.Popen("adb uninstall " + packageName, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        print(str(output.decode('ascii')))

# Scroll a little from bottom
    def vertical_scrollUp_little(self):
        p = subprocess.Popen("adb shell input swipe 520 1750 520 1300", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Swipe from bottom to top
    def vertical_scrollUp_fullscreen(self):
        p = subprocess.Popen("adb shell input swipe 520 1500 520 200", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Swipe from top to bottom (Excluding Notification Bar)
    def vertical_scrollDown_fullscreen(self):
        p = subprocess.Popen("adb shell input swipe 520 200 520 1500", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Scroll Horizontally from Left to Right
    def vertical_swipe_right(self):
        p = subprocess.Popen("adb shell input swipe 300 1000 2000 1000", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Scroll Horizontally from Right to Left
    def vertical_swipe_left(self):
        p = subprocess.Popen("adb shell input swipe 1000 800 -50 800", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Insert Username as a single word
    def insert_username(self, username):
        p = subprocess.Popen("adb shell input text " + username, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Insert Password as a single word
    def insert_password(self, password):
        p = subprocess.Popen("adb shell input text " + password, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Insert word as a single word
    def insert_word(self, password):
        p = subprocess.Popen("adb shell input text " + password, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

# Insert TEXT with SPACES. To insert text with spaces, use %s instead of spaces
    def insert_text_with_spaces(self, textWithSpaces):
        p = subprocess.Popen("adb shell input text " + textWithSpaces, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

    def tearDown(self):
        self.driver.quit()

# Tap on device back key
    def device_back_key(self):
        p = subprocess.Popen("adb shell input keyevent KEYCODE_BACK", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

apptest = appTest1()
# apptest.installing_application('Maps25961.apk')
apptest.launch_installed_application('com.bt.bms', 'com.movie.bms.splash.views.activities.SplashScreenActivity')
# apptest.uninstalling_application('com.one20.maps.qa')

