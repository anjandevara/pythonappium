import subprocess

def readoutput():
    # process = subprocess.Popen(["adb", "shell", "getprop", "ro.build.version.release"], stdout=subprocess.PIPE)
    # stdout = process.communicate()[0]
    # print("stdout{} :: ".format(stdout))
    #
    # output = process.stdout.readline()
    # print(output)
    # process.poll()

    # p = subprocess.Popen("adb shell getprop ro.build.version.release", stdout=subprocess.PIPE, shell = True)
    p = subprocess.Popen("adb shell getprop ro.product.model", stdout=subprocess.PIPE, shell=True)
    (output,err) = p.communicate()

    pwait = p.wait()

    print(output.decode('ascii'))
readoutput()