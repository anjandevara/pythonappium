import subprocess


def get_device_name():
    p = subprocess.Popen("appium", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()

get_device_name()