#!/bin/bash
wget https://ysicing.net/sitemap.xml
grep loc  sitemap.xml | sed 's/<loc>//g' | sed 's/<.*//g' | sed 's/ //g' > urls.txt
rm -f sitemap.xml
curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=https://ysicing.net&token=your_key"

