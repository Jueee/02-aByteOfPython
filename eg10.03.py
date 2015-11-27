#!/usr/bin/python
# Filename: backup_ver3.py
'''
第二个版本在我做较多备份的时候还工作得不错，但是如果有极多备份的时候，我发现要区分每个备份是干什么的，会变得十分困难！
例如，我可能对程序或者演讲稿做了一些重要的改变，于是我想要把这些改变与zip归档的名称联系起来。

这可以通过在zip归档名上附带一个用户提供的注释来方便地实现。
'''
import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = [r'E:\360\Python\PythonCode\01Study\01-Blog', r'E:\360\Python\PythonCode\01Study\02-aByteOfPython']
# If you are using Windows, use source = [r'C:\\Documents', r'D:\\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = r'C:\Users\weiyq10580\Downloads\\' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%Y%m%d%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print ('Successfully created directory', today)

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print( 'Successful backup to', target)
else:
    print ('Backup FAILED')