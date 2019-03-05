# JebScripts

  JEB运行.py步骤
  1.搭建环境
  1.1. http://www.jython.org/downloads.html这个网站下载独立的jar文件jython-standalone-2.7.0.jar
  1.2. jython-standalone-2.7.0.jar放到程序目录的scripts目录下
  2.运行
     文件->脚本->运行脚本 然后点击的py脚本即可
     
     
* JEB2DeobscureClass.py
  使用Smali中`.source`字段(`JEB中称为Debug Directives`)作为源文件名进行反混淆.
  原理：许多APK开发商为了在崩溃时保存源文件类名、行号等信息会在APK混淆时添加以下规则保留源文件信息.
	-keepattributes SourceFile,LineNumberTable。
  说明：
  1. .source "Base64.java",JEB2.2.x是默认不显示这些调试信息的,根据以下步骤在设置中打开:Edit -> Options -> Engines -> 修改ShowDebugDirectives的值为true(点一下就好).
  2. 因为无法获取内部类名所以无法还原内部类.
  3. 因为是全项目的重命名,根据APK类名的数量可能会有些慢大概要等几分钟
  
* CollapseAll.py
  收起JEB的包名
