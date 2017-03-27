title: linux命令之Crontab
date: 2016-05-16
tags: Linux
summary: Crontab，周期性执行任务工具
author: ysicing
secret: yes

## Install ##
----
Crontab默认是安装的,可以使用`crontab -l`检测是否安装  
使用`service cron status`是否启动
如果没安装

	Debian：apt-get install cron
    Centos: yum install vixie-cron
            yum install crontabs
    

## 基础格式 ##
----
参数:  
> -l 检查  
> -e 编辑  
> -u 指定用户  
> -r 删除

格式:  

	* * * * * cmd
	第一个* 0-59分钟
    第二个* 0-23小时
    第三个* 1-31日期
    第四个* 1-12月份
    第五个* 0-7星期[0\7都可以表示星期日]

重启nginx：  

	每晚23:30重启nginx
    30 21 * * * service nginx restart
    每月1，11，21日4:45重启nginx
    45 4 1,11,22 * * service nginx restart
    每月1到104:45重启nginx
    45 4 1-10 * * service nginx restart
    每隔2分钟重启nginx
    */2 * * * * service nginx restart
    1-59/2 * * * * service nginx restart
    晚上23点到早上7点每隔1h重启
    0 23-7/1 * * * service nginx restart
    每天18点-23点每隔30min重启
    0,30 18-23 * * * service nginx restart
    0-59/30 18-23 * * * service nginx restart
    
\*  表示任何都匹配  
A,B,C 表示A或B或C执行  
A-B 表示在A-B的区间内执行  
/A 表示每隔A执行一次

#### 查看是否执行 ####

	Debian：tail -f /var/spool/mail/xxx [xxx为非root用户]
    
另外Debian默认cron日志记录状态默认是关闭的  

	root@server:~# nano /etc/rsyslog.conf 
	默认在63行去掉注释
    root@server:~# /etc/init.d/rsyslog restart 
	root@server:~# tail -f /var/log/cron.log
    可以查看是否执行了
    
## 配置文件 ##
系统级和用户级  
系统级任务调度:/etc目录下有一个crontab文件，这个就是系统任务调度的配置文件系统周期性所要执行的工作，比如写缓存数据到硬盘、日志清理等  
用户级任务调度:/var/spool/cron/crontabs目录中。其文件名与用户名一致

## misc ##
<em>
每条任务调度执行完毕，系统都会将任务输出信息通过电子邮件的形式发送给当前系统用户，这样日积月累，日志信息会非常大，可能会影响系统的正常运行，因此，将每条任务进行重定向处理非常重要
</em>  
`0 */3 * * * cmd >/dev/null 2>&1`
忽略日志输出,`/dev/null 2>&1` 表示先将标准输出重定向到`/dev/null`，然后将标准错误重定向到标准输出.可以`/dev/null`看作"黑洞". 它非常等价于一个只写文件. 所有写入它的内容都会永远丢失. 而尝试从它那儿读取内容则什么也读不到  

#### ERROR之环境变量 ####
先在`/etc/profile`中add
```
Love=/etc
export Love
source /etc/profile
echo $Love
crontab -e
add这个 */1 * * * * echo $Love >> /tmp/love.log
tail -f /tmp/love.log
```
环境变量为未识别  

1.  传参方式
2.  在脚本中定义环境变量 
3.  在脚本中加载环境变量文件 ‘source /etc/profile'
4.  还有可以在crontab中加载环境变量

<em>1）新创建的cron job，不会马上执行，至少要过2分钟才执行。如果重启cron则马上执行。
2）每条 JOB 执行完毕之后，系统会自动将输出发送邮件给当前系统用户。日积月累，非常的多，甚至会撑爆整个系统。所以每条 JOB 命令后面进行重定向处理是非常必要的： >/dev/null 2>&1 。前提是对 Job 中的命令需要正常输出已经作了一定的处理, 比如追加到某个特定日志文件。
3）当crontab突然失效时，可以尝试/etc/init.d/crond restart解决问题。或者查看日志看某个job有没有执行/报错tail -f /var/log/cron。
4）千万别乱运行crontab -r。它从Crontab目录（/var/spool/cron）中删除用户的Crontab文件。删除了该用户的所有crontab都没了。
5）在crontab中%是有特殊含义的，表示换行的意思。如果要用的话必须进行转义\%，如经常用的date ‘+%Y%m%d’在crontab里是不会执行的，应该换成date ‘+\%Y\%m\%d’`。
</em>
#### ERROR之第三个和第五个域执行的是或操作 ####
<em>
四月的第一个星期日早晨1:59运行a.sh
	59 1 1-7 4 * test \`date +\%w ` -eq 0 && /root/a.sh
</em>
#### 半分钟执行 ####

	date;sleep 0.5s;date;
	*/1 * * * * date >> /tmp/datex.log
	*/1 * * * * sleep 30s;date >> /tmp/datex.log
    
    root@server:~# cat /tmp/datex.log 
	Sun May 15 15:20:01 EDT 2016
	Sun May 15 15:20:31 EDT 2016
	Sun May 15 15:21:01 EDT 2016
	Sun May 15 15:21:31 EDT 2016
	Sun May 15 15:22:01 EDT 2016
    



## 资料 ##
[crontab与环境变量，以及应该注意的一些问题](http://bbs.chinaunix.net/thread-2291457-1-1.html)

<!--2016/05/16 打卡,今天好想和她说声谢谢她的礼物 = = -->