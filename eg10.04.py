进一步优化

对于大多数用户来说，第四个版本是一个满意的工作脚本了，但是它仍然有进一步改进的空间。比如，你可以在程序中包含 交互 程度——你可以用-v选项来使你的程序更具交互性。

另一个可能的改进是使文件和目录能够通过命令行直接传递给脚本。我们可以通过sys.argv列表来获取它们，然后我们可以使用list类提供的extend方法把它们加到source列表中去。

我还希望有的一个优化是使用tar命令替代zip命令。这样做的一个优势是在你结合使用tar和gzip命令的时候，备份会更快更小。如果你想要在Windows中使用这些归档，WinZip也能方便地处理这些.tar.gz文件。tar命令在大多数Linux/Unix系统中都是默认可用的。Windows用户也可以下载安装它。

命令字符串现在将称为：

tar = 'tar -cvzf %s %s -X /home/swaroop/excludes.txt' % (target, ' '.join(srcdir))
选项解释如下：

-c表示创建一个归档。

-v表示交互，即命令更具交互性。

-z表示使用gzip滤波器。

-f表示强迫创建归档，即如果已经有一个同名文件，它会被替换。

-X表示含在指定文件名列表中的文件会被排除在备份之外。例如，你可以在文件中指定*~，从而不让备份包括所有以~结尾的文件。

重要
最理想的创建这些归档的方法是分别使用zipfile和tarfile。它们是Python标准库的一部分，可以供你使用。使用这些库就避免了使用os.system这个不推荐使用的函数，它容易引发严重的错误。
然而，我在本节中使用os.system的方法来创建备份，这纯粹是为了教学的需要。这样的话，例子就可以简单到让每个人都能够理解，同时也已经足够用了。