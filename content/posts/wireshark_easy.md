title: 流量取证类题目
author: ysicing
date: 2015-12-03
update: 2016-03-30
tags: ctf
status: publish
summary: wireshark神器的简单应用.


## 0x00 基础知识
------
首先，`wireshark`不会像`burp suite`那样可以对数据包进行修改，它能做的只是监听网络流量信息并完整的记录下来。可以说，`wireshark`起到的是一个还原现场的作用。请记住，wireshark只是一个帮助你审计的工具，至于怎么去审计，只能考自己去分析。<br />
其次，说说`wireshark`在安全方面的作用。`Wiki`上是这样描述的：对于安全人员而言，网络安全工程师可以使用`wireshark`来检查讯息安全相关的问题。对于网络安全而言，现场很重要，黑客攻击的过程和服务器被攻击的过程都必须使用网络，`wireshark`完全可以记录下来，这也正是`wireshark`强大的地方。

>推荐阅读的book：`Wireshark网络分析实践`<br />
>参考实验 [wireshark之文件还原](http://www.hetianlab.com/?inviter=REG-d706-3880-47cc-8d79-1d6eee88b555)<br />
>[伯乐在线 --- 一站式学习Wireshark系列](http://blog.jobbole.com/70907/)<br />
>很有趣的东西，可惜不太会，慢慢Get it

## 0x01 NCTF-MISC
------
<del>简单题</del><br />
##### 类型1 直接导出HTTP对象就ok了
```
题：南邮nctf热身misc 1
easy wireshark
听说抓到他浏览网页的包,flag就在网页里
```
包： [题1](https://dn-ist-802.qbox.me/networkwireshark.pcapng)<br />
![ctf1](https://dn-ist-802.qbox.me/posts%2Fimg%2Fll-1024x550.png)
<br />
save保存，打开就ok `nctf{wireshark_is_easy}`<br />
##### 类型2 提取压缩包
```
题：南邮nctf热身misc 2
使用wireshark 分析流量包，获取flag，本题flag是 Flag-XxXx形式 提交flag的时候请全部转换成小写 如 flag-xxxxx
```
<br />
包：[题2](https://dn-ist-802.qbox.me/networkmisc.pcap)<br />

过滤：`http.request.method==GET`<br />
第一条Get 压缩包密码`the password for zip file is : ZipYourMouth`<br />
第二条Get 压缩包<br />
常规思路：<br />
![ctf2](https://dn-ist-802.qbox.me/posts%2Fimg%2F2015-11-26_153420.png)
跟随流-tcp流<br />
根据情况进行选择save为二进制文件，然后用winhex进行编辑提取出文件zip压缩包<br />
本题的还可以：<br />
`apt-get install tcpx`   （Tap补全为tcpxtract）<br />
`tcpxtract -f misc.pcap`<br />
![ctf3](https://dn-ist-802.qbox.me/posts%2Fimg%2F2015-11-26_152802.png)
得到两个文件打开第一个`get flag Flag-qscet5234diQ`<br />

## 0x02 华山杯 ##
----
<del>待续ing</del>
<!--包不见了哒好尴尬哈-->



