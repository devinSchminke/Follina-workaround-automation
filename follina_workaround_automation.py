import os
import keyboard
import time

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Also add information on how to contact you by electronic and paper mail.

#this is going need to ran as admin probably. 
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