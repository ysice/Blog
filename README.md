基于Flask的博客开发需求分析文档  
## 主体  
博客前台：  
基于html5开发  

博客后端：  
基于python开发  

## 细节模块

1. 用户认证模块  
1.1实现管理员登入/登出功能  
1.2密码找回功能  

2. 用户资料及角色模块  
2.1博客信息管理  
2.2角色管理  

3. 博客文章模块  
3.1支持git管理文章  
3.2支持在线写博客  
3.3其他文章相关模块编写  

4. 后台管理模块  
4.1API模块管理  
4.2日志分析模块--流量分析及统计  
4.3博客监控模块  
4.4博客报警模块--邮件/短信报警  
4.5博客安全模块--基于Nginx  

5. 其他模块  
5.1评论模块-基于第三方评论实现  
5.2分享模块  

6. 容器化，支持docker[^1]  

## 待补充

	pip freeze > requirements.txt
	pip install -r requirements.txt -i https://pypi.douban.com/simple

	posts 存放.md文档
	wiki 存放git .md文档

[^1]:DOckerfile