/**
 * Created by root on 2016/3/15 0015.
 */
/**
 * Author:Smohan
 * Version:1.0.1
 * url: http://www.smohan.net/lab/smohan_share.html
 * 使用请保留以上信息
 */
global_share_image = (typeof global_share_image == "undefined") ? '' : global_share_image;
!function(a){
    a.fn.smohanShare=function(b){
        function q(a){
            var b="",c=[];
            switch(a){
                case"sina":c=u("sina"),b="http://v.t.sina.com.cn/share/share.php?"+c.join("&");
                    break;
                case"qzone":b="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url="+g+"&title="+f+"&desc="+h+"&pics="+i+"&summary=&site=\u6c34\u58a8\u5bd2WEB\u5de5\u4f5c\u5ba4";
                    break;
                case"tq":b="http://share.v.t.qq.com/index.php?c=share&a=index&title="+f+"&site="+d.from+"&pic="+i+"&url="+g;
                    break;
                case"renren":b="http://widget.renren.com/dialog/share?resourceUrl="+g+"&title="+f+"&images="+i;break;case"huaban":b="http://huaban.com/bookmarklet/?url="+g+"&title="+f+"&description="+h+"&media="+i+"&via=4";
                    break;
                case"facebook":b="http://www.facebook.com/sharer.php?u=="+g+"&t="+h+"&pic="+i;
                    break;
                case"twitter":b="http://twitter.com/share?text="+h+"&url=="+g+"&pic="+i}window.open(b,"newwindow","width="+d.openSize[0]+",height="+d.openSize[1]),d.autoClose&&v()}
        function r(){
            for(var a=document.getElementsByTagName("meta"),b=0;b<a.length;b++)
                if("description"==a[b].getAttribute("name"))
                    return a[b].getAttribute("content")
        }
        function s(){
            var b="";
            for(var c in d.btns)
                b+=t(d.btns[c]);return b}
        function t(a){
            var b={
                sina:"\u65b0\u6d6a\u5fae\u535a",
                qzone:"QQ\u7a7a\u95f4",
                tq:"\u817e\u8baf\u5fae\u535a",
                renren:"\u4eba\u4eba\u7f51",
                huaban:"\u82b1\u74e3\u7f51",
                facebook:"Facebook",
                twitter:"Twitter",
                fav:"\u52a0\u5165\u6536\u85cf"},c="fav"!==a?"\u5206\u4eab\u5230"+b[a]:"\u52a0\u5165\u6536\u85cf";return'<li title="'+c+'"><a class="share-'+a+'" data-value="'+a+'" style="cursor:pointer;"></a><span></span></li>'}function u(a){var b=d.app[a][0]?d.app[a][0]:null,c=d.app[a][1]?d.app[a][1]:null,j=[];"sina"==a?param={url:g,appkey:b,title:f,searchPic:!0,pic:i,ralateUid:c,rnd:(new Date).valueOf()}:"tq"==a&&(param={url:g,summary:h,title:f,site:d.from,pics:i});for(var k in param)j.push(k+"="+encodeURIComponent(param[k]||""));return j}function v(){a("#layer_shadow.share-layer-shadow").fadeOut("slow"),l.fadeOut("slow")}function w(){document.all?window.external.addFavorite(g,f):window.sidebar?window.sidebar.addPanel(f,g,""):alert("\u8bf7\u4f7f\u7528Ctrl+D\u952e\u5bfc\u5165\u5230\u4e66\u7b7e\uff01")}var f,g,h,i,j,c={event:"click",common:{title:"",url:"",texts:"",image:""},btns:["sina","qzone","tq","renren","huaban","facebook","twitter","fav"],shadow:[!0,!0],animate:!0,speed:300,autoClose:!1,title:"\u5206\u4eab\u6c34\u58a8\u5bd2\u5230\u5404\u5927\u793e\u533a",openSize:[650,460],app:{sina:["678438995","3061825921"],tq:["",""]},from:"\u6c34\u58a8\u5bd2WEB\u5de5\u4f5c\u5ba4",version:"smohanShare Version 2.0"},d=a.extend(c,b),e=a(this).eq(0);f=d.common.title?encodeURIComponent(d.common.title):encodeURIComponent(document.title),g=d.common.url?encodeURIComponent(d.common.url):encodeURIComponent(location.href),h=d.common.texts?encodeURIComponent(d.common.texts):r(),i=encodeURIComponent(d.common.image),j=d.title?d.title:"\u5206\u4eab\u6c34\u58a8\u5bd2\u5230\u5404\u5927\u793e\u533a",i||void 0==global_share_image||(i=global_share_image);var k="";d.shadow[0]&&(k+='<div id="layer_shadow" class="share-layer-shadow" style="display:none;width:100%;height:100%; position:fixed; left:0; top:0; background:rgba(0,0,0,.5);z-index:99990;zoom: 1;"></div>'),k+='<div id="SmohanShare-Wraper" style="z-index:999999">',k+='<div class="t"><strong>'+j+'</strong><a style="cursor:pointer;" title="\u5173\u95ed" class="close"></a></div>',k+="<ul>"+s()+"</ul>",a("body").append(k);var l=a("#SmohanShare-Wraper"),m=l.children("ul").outerWidth(),n=l.outerHeight(),o=l.find("li"),p=l.find("a.close");l.css({width:m,display:"none"}),l.hide(),e.on(d.event,function(){a("#layer_shadow.share-layer-shadow").show(),l.css({width:m,height:n,"margin-top":-(n/2+50),"margin-left":-m/2}).show(d.speed)}),d.shadow[1]&&a("#layer_shadow.share-layer-shadow").click(function(){v()}),p.click(function(){v()}),d.animate&&o.hover(function(){a(this).find("a").stop(!0,!0).animate({marginTop:2},"easeInOutExpo"),a(this).find("span").stop(!0,!0).animate({opacity:.2},"easeInOutExpo")},function(){a(this).find("a").stop(!0,!0).animate({marginTop:12},"easeInOutExpo"),a(this).find("span").stop(!0,!0).animate({opacity:1},"easeInOutExpo")}),o.on(d.event,function(){var b=a(this).children("a").attr("data-value");"fav"===b?w():q(b)})}}(jQuery);