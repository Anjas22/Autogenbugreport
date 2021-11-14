import sys
import os
import glob
import time
import subprocess
import shutil

qualcomm = "1"
mediatek = "2"

x = (input(' Select Function 1.Qualcomm 2.Mediatek = '))

if x == "1":
    print ('judul Bug ?')
    nameFolder = input()

    os.chdir ('C:\AutoGen')
    os.mkdir (nameFolder)
    os.chdir (nameFolder)
    subprocess.call("adb pull sdcard/MIUI/debug_log/ ",shell=True)
    subprocess.call("adb pull sdcard/DCIM/ScreenRecorder/ ",shell=True)
    subprocess.call("adb pull sdcard/diag_logs/ ",shell=True)

    old_name = r"debug_log"
    new_name = r"Bugreportlog"
    os.rename(old_name, new_name)

    old_name = r"diag_logs"
    new_name = r"Modemlog"
    os.rename(old_name, new_name)

    os.chdir('Bugreportlog')
    shutil.rmtree("com.miui.micloudsync")
    shutil.rmtree("com.miui.mishare")
    shutil.rmtree("com.miui.voiceassist.mvs")
    shutil.rmtree("com.xiaomi.account")
    shutil.rmtree("com.xiaomi.mi_connect_service")
    shutil.rmtree("common")
    shutil.rmtree("powerinfo")
    shutil.rmtree("tmp")
    
    files =  os.listdir()
    print(files)
    
    

    os.chdir ('C:\AutoGen')
    os.chdir (nameFolder)
 #   for filename in sorted(os.listdir("Bugreportlog"))[:-1]:
  #      filename_relPath = os.path.join("Bugreportlog",filename)
   # os.remove(filename_relPath)
    os.chdir ('Modemlog')
    os.remove("tcpdump.pcap1")
    os.remove("tcpdump.pcap0")
    files =  os.listdir()
    print(files)
    
    

    
    


if x == "2":
    print ('judul Bug ?')
    nameFolder = input()

    os.chdir ('C:\AutoGen')
    os.mkdir (nameFolder)
    os.chdir (nameFolder)
    os.mkdir ('Bugreportlog')
    os.mkdir ('Screenrecord')
    os.mkdir ('MTKLogger')
    import subprocess
    subprocess.call("adb pull sdcard/MIUI/debug_log Bugreportlog",shell=True)
    import subprocess
    subprocess.call("adb pull sdcard/DCIM/Screenshot Screenrecord",shell=True)
    import subprocess
    subprocess.call("adb pull sdcard/diag_logs MTKLogger",shell=True)
    
