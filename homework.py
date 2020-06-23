# 复制函数
def copy(old_file):
    """
    拷贝n个文件到当前目录下
    :param old_file: 要拷贝的文件
    :return: None
    """
    fr = open(old_file,'rb')
    # 边度编写
    while True:
        data = fr.read(1024*1024)
        if not data:
            break
        fw.write(data)
    fr.close()

fw = open('merge', 'wb')
copy('file.txt')
copy('hello.py')
fw.close()

if __name__ == '__main__':
    copy()