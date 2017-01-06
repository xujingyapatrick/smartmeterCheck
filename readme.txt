Author: Jingya Xu
Time:2017.1.5

1.environment requires: 
sendmail install:http://funtime.blog.51cto.com/8807074/1678580
sendmail module in python:http://www.runoob.com/python/python-email.html
MySQLdb module for python:http://blog.csdn.net/wklken/article/details/7271019 http://codingnow.cn/language/159.html
2.how to launch this script everyday:http://www.cnblogs.com/zichun-zeng/p/4235585.html
$:crontab -e
add:00 10 */1 * * python /home/zengzichun/python_script.py
this make the script run everyday at 10:00

