import sys
import os


qualcomm = "1"
mediatek = "2"

x = (input(' Select Function 1.qualcomm 2.mediatek = '))

if x == "1":
    print ('judul Bug ?')
    nameFolder = input()

    os.chdir ('D:\Tata Sarana Mandiri')
    os.mkdir (nameFolder)
    os.chdir (nameFolder)
    os.mkdir ('Bugreportlog')
    os.mkdir ('Screenrecord')
    os.mkdir ('Modemlog')



if x == "2":
    print ('judul Bug ?')
    nameFolder = input()

    os.chdir ('D:\Tata Sarana Mandiri')
    os.mkdir (nameFolder)
    os.chdir (nameFolder)
    os.mkdir ('Bugreportlog')
    os.mkdir ('Screenrecord')
    os.mkdir ('MTKLogger')
