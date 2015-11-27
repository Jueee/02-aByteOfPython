#!\\usr\\bin\\python
# Filename: backup_ver2.py
'''
第一个版本的脚本可以工作。然而，我们可以对它做些优化以便让它在我们的日常工作中变得更好。这称为软件的维护环节。

我认为优化之一是采用更好的文件名机制——使用 时间 作为文件名，而当前的 日期 作为目录名，存放在主备份目录中。
这样做的一个优势是你的备份会以等级结构存储，因此它就更加容易管理了。另外一个优势是文件名的长度也可以变短。
还有一个优势是采用各自独立的文件夹可以帮助你方便地检验你是否在每一天创建了备份，因为只有在你创建了备份，才会出现那天的目录。
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

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print ('Successfully created directory', today)
# os.sep变量的用法——这会根据你的操作系统给出目录分隔符，即在Linux、Unix下它是'/'，在Windows下它是'\\'，而在Mac OS下它是':'。
# 使用os.sep而非直接使用字符，会使我们的程序具有移植性，可以在上述这些系统下工作。
# The name of the zip file
target = today + os.sep + now + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')