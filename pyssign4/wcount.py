"""wcount.py: count words from an Internet file.

__author__ = "Xiang Yifan"
__pkuid__  = "1800011820"
__email__  = "1800011820@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import urllib.error


def wcount(lines, topn=10):
    for i in '!@#$%^&*()1234567890=_+{}|[]\:;<>?,./"`~':
        lines = lines.replace(i,' ')
    lines = lines.replace('--',' ')

    a = (lines.lower()).split()

    adict = {}

    for i in a:
        if i not in adict:
            adict[i] = 1
        else:
            adict[i] += 1
    k = sorted(adict.items(),key = lambda item:item[1],reverse = True)
    if topn > len(k):
        topn = len(k)
    for i in range(topn):
        print(k[i][0].ljust(15),k[i][1])


def main():
    try:
        doc = urllib.request.urlopen(sys.argv[1])
    except urllib.error.HTTPError :
        print('未找到网页！')
        return
    except urllib.error.URLError :
        print('网络未连接或网址有误！')
        return
    
    try:
        topn = int(sys.argv[2])
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode()
        wcount(jstr,topn)
    except :
        print('输入无效！默认以10运行程序！')
        topn = 10
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode()
        wcount(jstr,topn)

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('  用途: {} 是用来获取 url 上频率最高的前 topn 个单词.输入格式为：wcount.py url topn'.format(sys.argv[0]))
        print('  url: 需要分析的网址. ')
        print('  topn: 需要获取的频率最高的前topn个单词，如果缺省，默认为10.')
        sys.exit(1)
    else:
        main()
