#!\\usr\\bin\\python
# Filename: backup_ver1.py
'''
我们使用了os和time模块，所以我们输入它们。然后，我们在source列表中指定需要备份的文件和目录。目标目录是我们想要存储备份文件的地方，它由target_dir变量指定。zip归档的名称是目前的日期和时间，我们使用time.strftime()函数获得。它还包括.zip扩展名，将被保存在target_dir目录中。

time.strftime()函数需要我们在上面的程序中使用的那种定制。%Y会被无世纪的年份所替代。%m会被01到12之间的一个十进制月份数替代，其他依次类推。这些定制的详细情况可以在《Python参考手册》中获得。《Python参考手册》包含在你的Python发行版中。注意这些定制与用于print语句的定制（%后跟一个元组）类似（但不完全相同）

我们使用加法操作符来 级连 字符串，即把两个字符串连接在一起返回一个新的字符串。通过这种方式，我们创建了目标zip文件的名称。接着我们创建了zip_command字符串，它包含我们将要执行的命令。你可以在shell（Linux终端或者DOS提示符）中运行它，以检验它是否工作。

zip命令有一些选项和参数。-q选项用来表示zip命令安静地工作。-r选项表示zip命令对目录递归地工作，即它包括子目录以及子目录中的文件。两个选项可以组合成缩写形式-qr。选项后面跟着待创建的zip归档的名称，然后再是待备份的文件和目录列表。我们使用已经学习过的字符串join方法把source列表转换为字符串。

最后，我们使用os.system函数 运行 命令，利用这个函数就好像在 系统 中运行命令一样。即在shell中运行命令——如果命令成功运行，它返回0，否则它返回错误号。

根据命令的输出，我们打印对应的消息，显示备份是否创建成功。好了，就是这样我们已经创建了一个脚本来对我们的重要文件做备份！
'''
import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = [r'E:\360\Python\PythonCode\01Study\01-Blog', r'E:\360\Python\PythonCode\01Study\02-aByteOfPython']
# If you are using Windows, use source = [r'C:\\Documents', r'D:\\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = r'C:\Users\weiyq10580\Downloads\\' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix\\Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (target, ' '.join(source))
print(zip_command)
print('--')
# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')