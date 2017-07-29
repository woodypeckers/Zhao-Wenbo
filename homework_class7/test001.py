#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: zwb

#读取ini文件

import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('test001.ini'))
print config.get("global","processnum",)
print config.get("global","username",)
print config.get("global","password")
print config.get("testcase","login",)



# 创建ection段及对应的值

config.add_section("zwb")
config.set("zwb", "case2", "5")

#写入ini文件

config.set("testcase","case1","4")
config.write(open('test001.ini', "w"))
