import os
from subprocess import call
from  subprocess import check_output

def get_device_name():
    adb_device_name = call(["adb", "shell", "getprop", "ro.product.model" ])
    out = check_output(adb_device_name)
    device_name = str(out)
    return device_name

def get_device_version():
    adb_device_version = call(["adb", "shell", "getprop", "ro.build.version.release"])
    out = check_output(adb_device_version)
    device_version = str(out)
    return device_version

def get_desired_capabilities(apk_name):
        # Forming the APK FILE PATH
        current_user = os.path.expanduser('~')
        directory = "/Documents/pycharmworkspace/apkfolder/"

        desired_caps = {
            'platformName': 'Android',
            # 'platformVersion': '7.0',
            'platformVersion': get_device_version(),
            # 'deviceName': 'potter_n',
            'deviceName': get_device_name(),
            'app': os.path.expanduser('~') + os.path.join(directory, apk_name),
            'newCommandTimeout': 240
        }

        # print(desired_caps)
        return desired_caps

