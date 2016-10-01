#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'tan9le'
import jpype


def main():
    jvmPath = jpype.getDefaultJVMPath()
    #Windows下默认读取的是注册表HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment下面的CurrentVersion值中的版本
    #并且会将对应子键值下的RuntimeLib键值作为默认JVM Path
    print(jvmPath)
    jpype.startJVM(jvmPath)
    #jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=/Users/tan9le/temp/some-lib.jar:")
    jpype.java.lang.System.out.println( " hello world! " )
    map = jpype.JClass("java.util.HashMap")()
    map.put(u"测试",u"测试中文")
    print(map.get(u"测试"))
    jpype.shutdownJVM()


if __name__ == '__main__':
    main()