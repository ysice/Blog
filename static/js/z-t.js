/**
 * Created by gengtao on 16/8/4.
 */
/**
 * Created by ysicing on 2016/3/18.
 */

//change title
var changeTitle = {
	originTitle: document.title,
	change: function() {
		document.title = "草榴社區主論壇 - t66y.com ";
	},
	reset: function() {
		document.title = changeTitle.originTitle;
	}
};
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        changeTitle.change();
    } else {
        changeTitle.reset();
    }
});


//console.log
if (window.console) {
    var cons = console;
    if (cons) {
        cons.log("%c \n\
           _      _             \n\
 _   _ ___(_) ___(_)_ __   __ _ \n\
| | | / __| |/ __| | '_ \\ / _` |\n\
| |_| \\__ \\ | (__| | | | | (_| |\n\
 \\__, |___/_|\\___|_|_| |_|\\__, |\n\
 |___/                    |___/ \n\
\n\
By ysicing\n\
https://ysicing.net/\n\
希望可以结交更多的志同道合的朋友，@微博（http://weibo.com/caibaodoge/）或者Twitter（https://twitter.com/YsiCing）\n\
邮件root@ysicing.net or ops.ysicing@gmail.com(First) \n\
","color: #00adef;");

    }
}
//移动端识别
/*
if(/AppleWebKit.*mobile/i.test(navigator.userAgent) || (/MIDP|SymbianOS|NOKIA|SAMSUNG|LG|NEC|TCL|Alcatel|BIRD|DBTEL|Dopod|PHILIPS|HAIER|LENOVO|MOT-|Nokia|SonyEricsson|SIE-|Amoi|ZTE/.test(navigator.userAgent))){
    if(window.location.href.indexOf("?mobile")<0){
        try{
            if(/Android|webOS|iPhone|iPod|BlackBerry|iPad/i.test(navigator.userAgent)){
                window.location.href="/m/";
            }else{
                window.location.href="/api/other"
            }
        }catch(e){}
    }
}
*/


//自定义右键
	/*window.onload = function(){
		document.oncontextmenu = function(ev){
			var oEvent = ev || event;
			//鼠标点击坐标
			var l = oEvent.clientX;
			var t = oEvent.clientY;
			var oDiv = document.getElementById('contextmenu');
			//oDiv宽与高
			var w = oDiv.offsetWidth ? oDiv.offsetWidth : 152;
			var h = oDiv.offsetHeight ? oDiv.offsetHeight : 173;
			//判断是否到边界
			if(l + w < document.documentElement.clientWidth){
				oDiv.style.left = l + 'px';
			}else{
				oDiv.style.left = l - w + 'px';
			}
			if(t + h < document.documentElement.clientHeight){
				oDiv.style.top = t + 'px';
			}else{
				oDiv.style.top = t - h + 'px';
			}
			oDiv.style.display = 'block';
			// 阻止浏览器默认右键
			return false;
		}
    }
  onload=function(){
      var r = new mousemenu(document.getElementById("ibody"));
      r.setOptionCss({
          "color":"#666",
          "background":"#FFFFFF",
      });
      r.setOptionHoverCss({
			"background":"#FFFFFF",
			"color":"orange",
			"textIndent":"15px",
			"lineHeight":"30px"
		});
      r.setMenuCss({
          "background":"#FFFFFF",
          "boxShadow":"1px 1px 3px #666",
      });
      r.addOption("<a href='/posts/' style='text-decoration: none'><i class='fa fa-home'></i> 返回首页(B)</a>",function(){
          window.close();
      });
      r.addOption("<i class='fa fa-refresh'></i> 重新加载",function(){
         location.reload();
      });
      r.addOption("<i class='fa fa-bug'></i> 检查(N)",function(){
          alert("Thank you ， check it...");
      });
      r.addOption("<a href='/posts/' title='博客' style='text-decoration: none' ><i class='fa fa-bookmark'></i> 博客 </a> ");
      r.addOption(    "<a href='/google/' title='导航' style='text-decoration: none' ><i class='fa fa-thumbs-up'></i> 导航 </a> " );
      r.addOption(    "<a href='/wiki/' title='wiki' style='text-decoration: none' ><i class='fa fa-wikipedia-w'></i> Wiki </a>" );
      r.addOption(    "<a href='/link#友情链接说明' title='Doing'style='text-decoration: none' ><i class='fa fa-link'></i> Link</a> ");
  };
*/
//copy
//document.onselectstart=function(e){return   false;};
/*
function fuckyou(){
 window.close();
 window.location="about:blank";
}
 function ck() {
 console.profile();
 console.profileEnd();
if(console.clear) { console.clear() };
 if (typeof console.profiles =="object"){
 return console.profiles.length > 0;
 }
}
function hehe(){
if( (window.console && (console.firebug || console.table && /firebug/i.test(console.table()) )) || (typeof opera == 'object' && typeof opera.postError == 'function' && console.profile.length > 0)){
 fuckyou();
}
if(typeof console.profiles =="object"&&console.profiles.length > 0){
fuckyou();
}
}
hehe();
window.onresize = function(){
if((window.outerHeight-window.innerHeight)>200)
fuckyou();
}*/