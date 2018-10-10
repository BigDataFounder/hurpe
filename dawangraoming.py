#-*- coding:utf-8 _*-  
'''
@file : dawangraoming.py
@auther : Ma
@time : 2018/09/21
'''

import re
import urllib2
import random

ua = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1",
      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
      'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/533.3',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/7.0.521.0 Safari/534.8',
      'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8',
      'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz'
      ]


def parse_novel_url(url,url_pat):
    req = urllib2.Request(url=url)
    req.add_header('User-Agent', random.choice(ua))
    open = urllib2.build_opener()
    f = open.open(req).read()
    url_key = re.compile(url_pat, re.S).findall(f)
    return url_key

# 将出问题的章节写入到文件 error.txt 中
def write_error(index,novel_chapter):
    with open('G:/pycode/Test/biquge/dawangraoming/error.txt','a') as ff:
        ff.write('index = ' + str(index) + ',novel_chapter = ' + novel_chapter + '\n')
        ff.close()

if __name__ == '__main__':
    novel_id = '38531'   # 小说的id

    # 小说的url和匹配的正则表达式，并返回小说具体章节的链接
    url = 'https://www.qu.la/book/' + novel_id + '/'
    url_pat = '<dd> <a style="" href="(.*?)">(.*?)</a></dd>'
    url_key = parse_novel_url(url,url_pat)

    # len(url_key)
    for i in range(1100,1200):
        # 因为前12个都是最近章节
        i = i + 11
        novel_url = 'https://www.qu.la' + url_key[i][0]
        novel_chapter = url_key[i][1].replace('?','')
        print novel_chapter
        novel_pat = '<div id="content">(.*?)</div>'
        novels = parse_novel_url(novel_url,novel_pat)
        novels = novels[0].replace('&nbsp;','')\
                          .replace('<br/>','\n')\
                          .replace('</br>','')\
                          .replace('<script>chaptererror();</script>','')

        try :
            # 保存到文件中
            file_name = 'G:/pycode/Test/biquge/dawangraoming/' + str(novel_chapter) + '.txt'
            # 将中文编码设置为 utf8
            file_name_utf8 = unicode(file_name,'utf8')
            with open(file_name_utf8,'a') as f:
                f.write(novels)
                f.close()
        except Exception as e:
            print e
            write_error(i, novel_chapter)



