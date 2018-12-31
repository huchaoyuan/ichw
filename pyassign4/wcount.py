"""wcount.py: count words from an Internet file.

__author__ = "HuChaoyuan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
from collections import Counter


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    try:
        doc = bytes.decode(urlopen(lines).read())  #获取 lines 对应 url 的文本
        doc_1 = doc.split()#将文本拆分
        lines_1 = []  #定义一个空列表
        for i in doc_1:  #将去除标点符号的单词加入 lines_1
            lines_1.append(''.join(e for e in i if e.isalnum()).lower())
        print(Counter(lines_1).most_common(topn))  #对 lines_1 中的单词进行计数，并将前 topn 位的单词和数量输出
    except: #若出现异常则输出报错
        print('错误')


def main():
    """main module
    """
    if  len(sys.argv) == 1: #当用户输入 wcount.py 时给出输入提示
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    elif len(sys.argv) == 2: #用户没有输入前多少位单词，则默认为前10
        wcount(sys.argv[1])
    elif len(sys.argv) == 3:
        wcount(sys.argv[1],int(sys.argv[2]))


if __name__ == '__main__':
    main()
