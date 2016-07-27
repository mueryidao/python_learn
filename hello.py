#!/usr/bin/env python
# -*- coding: utf-8 -*-

#name=raw_input('What\'s your name?\n')
#print 'hello', name + '!'

#print u'中文测试正常'
print u'你好冒险者，我是穆，请问你是'
name = raw_input(u"请输入你的姓名:".encode('gbk').decode('gbk'))
print '%s你好，真是一个不错的名字，欢迎来到%s' %(name,"法兰城")

