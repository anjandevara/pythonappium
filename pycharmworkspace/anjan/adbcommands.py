from subprocess import call
import os
user = os.path.expanduser('~')
usr = str(user)
directory = os.path.dirname('/Documents/pycharmworkspace/adbtool/adb')
dir = str(directory)

adb_command = os.path.abspath(os.path.join(os.path.expanduser('~'),os.path.dirname('/Documents/pycharmworkspace/adbtool/adb')))
print(user)
print(adb_command)
adb = user + directory
call(['adb', "shell", "getprop", "ro.product.model"])
