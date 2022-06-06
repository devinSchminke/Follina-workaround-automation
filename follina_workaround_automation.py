import os
import keyboard
import time

#This is software has the MIT License.

#this is going to need to ran as admin probably. 

os.system(
    'cd C:\ ' + #this will navigate us to the C drive, and how we are there in the prompt
    '& mkdir FollinaRegBackup' + #this will create a folder on the C/ drive to save the backup in.
    '& attrib +h FollinaRegBackup'
    '& cd C:\FollinaRegBackup' +
    '& type nul > README.txt'
)

time.sleep(.5)

keyboard.press_and_release('windows+r')
time.sleep(.5)
keyboard.write('C:\FollinaRegBackup\README.txt')
keyboard.press('enter')
time.sleep(1.5)
keyboard.write('Hello!')
keyboard.press_and_release('return')
keyboard.write('This folder is housing the backup of regkeys needed to restore full msdt functionality') 
keyboard.press_and_release('return')
keyboard.write("PLEASE DO NOT DELETE THIS, or anything contained in it")
keyboard.press_and_release('return')
keyboard.write("that is all, tata for now.")
keyboard.press_and_release('ctrl+s')
keyboard.press_and_release('ctrl+w')

os.system('reg export HKEY_CLASSES_ROOT\ms-msdt C:\FollinaRegBackup\FollinaRegbackup.reg ') #This will back up the RegKeys to the newly created dir in C. 

time.sleep(2)

os.system('reg delete HKEY_CLASSES_ROOT\ms-msdt /f') #this should secure the machine/host according to microsoft documentation on the issue. 
